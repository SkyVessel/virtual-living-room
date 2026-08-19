# todo/ — 任务交接窗口

Mac agent(Yasmine)与 Windows agent 的任务交接板。**一个任务一个文件**，通过 git 同步。

## 文件命名

```
WIN-001-简短标题.md   # 给 Windows agent 的任务
MAC-001-简短标题.md   # 给 Mac agent 的任务
```

## 任务文件格式（七字段）

每个任务文件必须包含：**Goal / Context / Scope / Permissions / Constraints / Deliverable / Done**。

## 状态流转

文件头部 `status:` 字段，单向推进：

```
pending → doing → done / blocked
```

- 领取任务：把 `status` 改为 `doing`，填 `assignee` 和领取时间，commit 并 push
- 完成后：改 `done`，把结果（数字、日志摘要、结论）写进文件末尾的 `## 结果` 区，commit 并 push
- 卡住：改 `blocked`，写明需要什么（如"需要用户点 UAC"）

## 纪律

- 只改自己领取的任务文件；不替对方改状态
- 需要用户介入的事项（UAC、账号登录、手感验收）在文件里 @用户，并在结果区醒目标注
- 大段日志写进 `todo/logs/` 子目录，任务文件里只放结论和路径
