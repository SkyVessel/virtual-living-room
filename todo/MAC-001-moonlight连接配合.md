---
id: MAC-001
status: pending
assignee: （待领取）
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

（待填写）
