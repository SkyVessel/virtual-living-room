# 虚拟客厅

## 产品边界

- 定位：Discord 原生的 Remote Couch Activity；Discord 负责社交、语音和社区，我们负责本地游戏的座位、虚拟手柄与控制权交接。
- 客户端：Host 安装 Windows Agent（GPL）；访客从 Discord Activity 加入，首次加入自动下载安装伴侣软件。Activity iframe 仅作客厅状态展示与加入入口，视频与主要功能全部由伴侣软件承载。
- V0：Windows Host、Discord Desktop 访客、2 个座位、旁观、手动交接、P2P 优先。
- 不做：战绩记录、排行榜、游戏录像与独立语音系统。

## 参与者动线

- **Activity iframe（轻壳）**：只显示客厅状态——在线人数、座位占用、当前操作者；不做视频、不做手柄、不做主要交互。
- **加入按钮**：点击后打开伴侣软件（安装时自动下载）；首次使用引导下载安装，安装后经按钮直接唤起。
- **伴侣软件（视频与主功能）**：视频画面、虚拟手柄、控制权交接与旁观全部在此；通过 WebRTC 与 Host 建立 P2P 连接。

## Cloudflare 规划

| 服务 | 用途 | 初期策略 |
| --- | --- | --- |
| Pages | 托管 Discord Activity 静态前端（状态轻壳） | 使用 |
| Workers | Discord OAuth、房间 API、邀请与临时 ICE 凭证 | 使用；免费计划 10 万请求/日 |
| Durable Objects | 每个房间的实时状态、座位权限与信令连接 | 使用；免费计划 10 万请求/日、13,000 GB-s/日；付费计划（月最低 $5）含 100 万请求与 40 万 GB-s |
| D1 | 后续用户数据；不存战绩或排行榜 | 暂不接入 V0；免费计划 5 GB、500 万行读取/日、10 万行写入/日 |
| Realtime SFU + TURN | P2P 失败时 TURN 中继；多人观看/群组媒体再启用 SFU | 暂不作为默认路径；每账户每月前 1,000 GB 免费，之后 $0.05/GB 出站流量 |
| STUN | ICE 候选发现与直连打洞 | P2P 默认路径；接入前复核 Cloudflare 当期服务条款 |

## 运行原则

- 视频与手柄默认 Host ↔ 访客伴侣软件 P2P；Realtime 只做连接失败兜底，避免中继带宽成为默认成本。
- Activity iframe 只承担状态展示与加入入口，不承载媒体流；避免把视频/手柄塞进 iframe 的沙箱网络路径。
- 所有服务地址通过自有域名配置，不能写死供应商 IP 或用量假设。
- Cloudflare 价格与限额会变化；上线或开通付费前，以官方文档为准：
  - https://developers.cloudflare.com/workers/platform/limits/
  - https://developers.cloudflare.com/durable-objects/platform/pricing/
  - https://developers.cloudflare.com/d1/platform/pricing/
  - https://developers.cloudflare.com/realtime/sfu/pricing/
