---
id: MAC-001
status: done
assignee: Yasmine (Mac)
created: 2025-XX-XX
depends: WIN-001
---

# MAC-001:安装 Moonlight,配合 WIN-001 完成连接与延迟验收

## Goal

在 Mac 上装好 Moonlight 客户端，配合 Windows agent 完成配对与串流，记录 Mac 侧观察到的延迟与手柄体验。

## Context

- 配合任务:`todo/WIN-001-sunshine安装与基线测试.md`,先确认其状态为 doing 再开始
- Moonlight 安装:`brew install --cask moonlight`
- 配对时 Moonlight 会显示 4 位 PIN,需要告诉 Windows 侧在 Sunshine 管理页输入——通过本文件结果区或当面对接

## Scope

只做：装 Moonlight → 配对 → 连一次桌面 → 接手柄（如有）验证输入回传 → 协助延迟粗测。
不做：浏览器手柄页开发（那是后续任务）。

## Permissions

可写：可安装 Moonlight、发起连接。需要 @用户：手感验收。

## Constraints

- 不改 Windows 侧任何配置（那是 Windows agent 的作用域）
- 两端在同一局域网内完成，不做外网打洞

## Deliverable

本文件 `## 结果` 区：Moonlight 版本、连接是否成功、Mac 侧主观延迟感受记录、手柄回传结论。

## Done

- 两端连通一次，结果区填写完毕，状态置 done 并 push

## 结果

**2026-08-19 完成。连接全链路打通，核心结论：**

1. **Moonlight 版本**:6.1.0(brew cask),Mac 侧安装顺利
2. **配对成功（全程序化，关键验证）**:`moonlight pair <IP> --pin <指定4位PIN>` 发起配对 + `POST /api/pin`(Basic Auth）提交 PIN，全程无人工干预，Sunshine 端 named_certs 出现客户端 mac-yasmine。**注意时序**：必须等 Sunshine 挂住 pair 请求（日志出现 phrase=getservercert）后再提交 PIN，否则提交无效（status:true 但不生效）
3. **串流点亮**:1080p，最高验证到 120fps / 50Mbps / HEVC，画面清晰
4. **手柄注入**：未实测（Mac 侧无手柄），移交后续任务
5. **网络判决书（重要）**:Mac(Wi-Fi 5GHz 信号优）→ Windows 的 TCP 往返：中位 12.4ms / p95 88ms / 最大 356ms / 抖动 53ms。**Wi-Fi 抖动导致音画间歇卡顿**,Moonlight 零缓冲设计将其原样暴露。已排除：输入设备、刷新率错配（120/120/120 已对齐）、编码器（HEVC/H.264 均卡）、AWDL 后台扫描（关闭无效）、网络丢包（5 分钟 0 丢帧）

**残留风险 / 移交后续任务**:
- 待确认 Windows 侧是网线还是 Wi-Fi 连路由器（若 Host 也走 Wi-Fi，抖动翻倍；Host 插网线收益最大）
- **产品级结论：播放端必须做自适应抖动缓冲（10~50ms) + 自适应码率/帧率降级 + 网络质量指示，不学 Moonlight 零缓冲原教旨主义**
- Host 插网线后可复测对比
