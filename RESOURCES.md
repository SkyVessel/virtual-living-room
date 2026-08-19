# 资源与环境

> 本文件记录项目的开发资源、机器分工与协作方式，供 AI agent 和开发者快速对齐。

## 机器分工

| 机器 | 角色 | 说明 |
| --- | --- | --- |
| Mac（本机） | 主开发机 | 项目仓库、文档、后端（Cloudflare）、Activity 前端开发 |
| Windows 电脑 | 测试与协助开发 | 运行 Host Agent、虚拟手柄、Sunshine 等 Windows 专属组件的实测环境；同样配有一个 AI agent 协助开发 |

## AI 协作资源

| 工具 | 位置 | 用途 |
| --- | --- | --- |
| Yasmine (pi) | Mac 本机 | 主开发 agent，负责整体推进 |
| Codex（含 GPT5.6 sol 模型，最强） | Mac 本机 | **代码审查**与 **bug 修复协助**；需要 review 或疑难 bug 时由 Yasmine 主动调用/请求用户调用 Codex 检查 |
| AI agent（待命名） | Windows 电脑 | Windows 侧测试与协助开发 |

## 平台与账号

- GitHub：账号 `SkyVessel`，仓库公开
- Cloudflare：Pages / Workers / Durable Objects（规划见 agent.md，价格以其官方文档为准）
- Discord 开发者平台：Activity 应用（待创建）

## 调研结论索引（已完成，2025）

| 主题 | 结论 | 出处 |
| --- | --- | --- |
| 虚拟手柄驱动 | ViGEmBus 已于 2023 年退休（归档），原型可用、长期靠 Sunshine 生态共担；备胎 HIDMaestro（MIT，纯用户态） | 对话调研 + 商业化-全开源模式.md |
| Discord Activity 网络 | iframe 沙箱内 WebRTC 被禁、流量全走 Discord 代理，仅支持 WebSocket | Discord 官方 Networking 文档 |
| Go Live 延迟 | 面向观众设计（0.5~2s 玻璃到玻璃），客户端 de-jitter 缓冲是最大延迟源；不适合操作者 | Discord 工程博客 + discord-plays-mario-kart 实测 |
| 低延迟参照 | Parsec（BUD 协议，UDP+DTLS，视频零缓冲，延迟>帧率>画质）、Steam Remote Play（NvFBC/NvIFR 零拷贝采集 + SDR 骨干网） | Parsec 官方博客 / SSTIC 2023 逆向论文 |
| 视频引擎复用 | Sunshine（GPLv3，4 万 star，REST API 可编排）+ moonlight-web-stream（GPLv3，浏览器 WebRTC 客户端） | GitHub 核实 |
| 商业模式 | 全开源成立：服务端 AGPLv3、客户端 GPLv3、商标保留；收入走 Discord 内购与托管订阅 | 商业化-全开源模式.md |
| 输入路由参考 | PassTheStick（MIT，.NET 8，消息协议/键盘注入/交接 UX 可借鉴） | GitHub 尽调 |

## 关键架构决策（当前基线）

1. **Activity iframe 是轻壳**：只显示客厅状态 + 加入入口；不做视频、不做手柄
2. **访客首次加入自动下载伴侣软件**；视频、虚拟手柄、交接、旁观全部在伴侣软件内
3. **伴侣软件 ↔ Host 走 WebRTC P2P**；TURN 仅兜底
4. **语音永远留在 Discord 客户端**，不自建
5. **旁观者优先看 Go Live**；操作者走低延迟直连

## 原型验证路径（Claude 方案，分步验收）

- Step 0：单机 vgamepad 虚拟手柄画圈，证明游戏认得到（Windows 机上做）
- Step 1：浏览器 Gamepad API → WebSocket → 另一台机器 vgamepad 注入
- Step 2：换 WebRTC DataChannel（`ordered:false, maxRetransmits:0`），手机拍屏测延迟
- Step 3：多槽位路由表 + 交接
- Step 4：拿到延迟数字后定最终语言（倾向 .NET：HIDMaestro/伴侣软件/Host Agent 同栈）
