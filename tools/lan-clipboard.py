#!/usr/bin/env python3
"""局域网共享文本板:零依赖,两台机器浏览器互传文本。
用法: python3 lan-clipboard.py [端口,默认8765]
"""
import json
import socket
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

STORE = {"text": ""}

PAGE = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LAN 剪贴板</title>
<style>
  body { margin:0; background:#1e1f22; color:#dbdee1; font-family:system-ui; height:100vh; display:flex; flex-direction:column; }
  header { padding:10px 16px; background:#2b2d31; font-size:14px; display:flex; justify-content:space-between; align-items:center; }
  #status { font-size:12px; color:#949ba4; }
  textarea { flex:1; background:#1e1f22; color:#dbdee1; border:none; outline:none; resize:none; padding:16px; font-size:16px; font-family:ui-monospace,monospace; }
</style>
</head>
<body>
<header><b>📋 LAN 剪贴板</b><span id="status">已连接</span></header>
<textarea id="t" placeholder="在这里粘贴,另一台机器即时可见(双向同步)" autofocus></textarea>
<script>
const t = document.getElementById('t'), s = document.getElementById('status');
let last = '', dirty = false, timer = null;
t.addEventListener('input', () => {
  dirty = true;
  clearTimeout(timer);
  timer = setTimeout(push, 300);
});
async function push() {
  if (!dirty) return;
  dirty = false; last = t.value;
  await fetch('/text', {method:'POST', body: JSON.stringify({text: t.value})});
}
setInterval(async () => {
  try {
    const r = await fetch('/text');
    const d = await r.json();
    s.textContent = '已连接 ' + new Date().toLocaleTimeString();
    if (!dirty && d.text !== last) { last = d.text; t.value = d.text; }
  } catch(e) { s.textContent = '连接断开,重试中…'; }
}, 800);
</script>
</body>
</html>"""

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        if self.path == "/text":
            self._send(json.dumps(STORE).encode(), "application/json")
        else:
            self._send(PAGE.encode(), "text/html; charset=utf-8")
    def do_POST(self):
        if self.path == "/text":
            n = int(self.headers.get("Content-Length", 0))
            try:
                STORE["text"] = json.loads(self.rfile.read(n))["text"]
            except Exception:
                pass
            self._send(b"ok", "text/plain")
        else:
            self._send(b"not found", "text/plain", 404)
    def _send(self, body, ctype, code=200):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1)); ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"局域网剪贴板已启动:")
    print(f"  本机:   http://localhost:{port}")
    print(f"  局域网: http://{lan_ip()}:{port}   <- Windows 浏览器打开这个")
    ThreadingHTTPServer(("0.0.0.0", port), H).serve_forever()
