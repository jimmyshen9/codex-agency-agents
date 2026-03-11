# AGENTS.md

本项目优先使用 `engineering-codex` 精选技能，而不是全量 The Agency 技能。

## 默认原则

- 优先选择最少的技能完成任务，不要同时加载过多角色。
- 结论、调试说明、执行反馈优先使用中文。
- 不使用 emoji。
- 调试输出、检查项、状态说明用 `[说明]`、`[风险]`、`[下一步]` 这类规范化标签表达。
- 先做能直接改变结果的事情，再做包装和展示。
- 先收敛后扩展。不要把简单任务做成多角色表演。

## 推荐技能

- `engineering-codex-system-design`
  适用于系统设计、服务拆分、数据模型、接口边界。

- `engineering-codex-implementation`
  适用于功能实现、重构、修复、测试补齐。

- `engineering-codex-code-review`
  适用于补丁审查、风险识别、回归分析。

- `engineering-codex-release-check`
  适用于发布前检查、验收、证据收集、上线门槛判断。

- `engineering-codex-security-review`
  适用于安全风险识别、鉴权、输入校验、密钥和权限边界。

- `engineering-codex-devops-delivery`
  适用于 CI/CD、部署、环境配置、监控、回滚设计。

- `engineering-codex-incident-response`
  适用于线上事故、故障定位、止血、时间线整理和复盘。

## 推荐工作流模板

- 架构讨论：`commands/architecture.md`
- 日常调试：`commands/debug.md`
- 代码审查：`commands/review.md`
- 发布检查：`commands/deploy-checklist.md`
- 线上事故：`commands/incident.md`

## 输出要求

- 先给结论，再给证据。
- 发现问题时，优先给出可执行修复路径。
- 代码修改前说明要改什么。
- 如果没有充分证据，不要给过度确定的判断。
