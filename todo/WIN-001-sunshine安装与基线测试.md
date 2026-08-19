---
id: WIN-001
status: pending
assignee: （待领取）
created: 2025-XX-XX
---

# WIN-001:安装并配置 Sunshine,完成 Moonlight 配对,测出基线延迟

## Goal

在 Windows 机上装好 Sunshine 串流主机，与 Mac 上的 Moonlight 客户端完成一次局域网连接，输出画面延迟与手柄注入是否可用的结论。

## Context

- 项目"虚拟客厅"选定 Sunshine(GPLv3)作为视频 + 虚拟手柄注入引擎，本任务是整机链路的第一次点火
- Sunshine 官方仓库:https://github.com/LizardByte/Sunshine(下载 Windows 安装包或用 winget)
- Sunshine 自带 REST API（文档:仓库 docs/api.md),Web 管理界面在 `https://localhost:47990`(首次启动需设置管理员账号密码)
- Mac 侧 Moonlight 客户端由 Mac agent 负责安装（`brew install --cask moonlight`),配对需要两端配合
- Sunshine 的手柄注入底层是 ViGEmBus 驱动，安装时会带 UAC 弹窗

## Scope

只做：安装 Sunshine → 启动服务 → 设管理员账号 → 与 Mac Moonlight 配对 → 串流一次桌面 → 手柄输入验证 → 延迟粗测。
不做:任何代码开发、任何 Sunshine 配置深度调优、任何非局域网连接。

## Permissions

可写：可下载安装软件、修改 Sunshine 配置、运行命令行。
**需要 @用户 介入**:UAC 弹窗（预计 1-3 次）、可能的驱动安装确认、手感验收。

## Constraints

- 不修改系统其他设置；不装与本任务无关的软件
- 若安装器要求重启，先 @用户 确认再重启
- **本仓库是公开的：密码/凭证一律不入库、不写进任何文件**。Sunshine 管理员密码设置后直接当面告诉用户，任务文件里只记录“已设置”

## Deliverable

在本文件末尾 `## 结果` 区写：
1. Sunshine 版本号、安装方式
2. 配对是否成功、串流是否点亮
3. 手柄注入结论（游戏里手柄动没动）
4. 延迟粗测数字（方法：游戏里开一个毫秒级计时器画面或拍屏对比，记录估计值）
5. 遇到的坑与残留风险

## Done

- Mac Moonlight 能看到并操作 Windows 桌面，手柄输入在 Windows 侧生效
- 结果区五项全部填写
- 状态置为 done 并 push；若卡在 UAC/重启等待，置 blocked 并 @用户

## 结果

（待填写）
