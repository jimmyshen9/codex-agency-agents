# AGENTS.md

本项目优先使用 `ops-codex` 处理运行稳定性、监控、发布安全和额度保护问题。

## 默认原则

- 先保证服务可持续运行，再做展示层优化。
- 调试信息、状态说明、风险提示优先使用中文。
- 不使用 emoji。
- 状态说明优先使用 `[说明]`、`[风险]`、`[处置]`、`[下一步]` 这类规范标签。
- 对第三方 API 的失败要优先考虑退避、冷却和熔断，避免无效重试。
- 线上改动优先考虑回滚路径、持久化状态和副作用。

## 推荐技能

- `ops-codex-runtime-reliability`
  适用于调度器、守护进程、后台 worker、重试、锁和状态机。

- `ops-codex-observability`
  适用于日志、指标、仪表盘、健康检查和延迟分解。

- `ops-codex-incident-response`
  适用于线上故障、止血、证据收集、时间线和复盘。

- `ops-codex-release-safety`
  适用于发布开关、配置变更、回滚、迁移和上线检查。

- `ops-codex-cost-guard`
  适用于 credits、配额、速率限制、API 成本和无效请求保护。

## 推荐工作流模板

- 运行态调试：`commands/runtime-debug.md`
- 成本与配额保护：`commands/cost-budget.md`
- 故障处理：`commands/incident.md`
- 发布门槛：`commands/release-gate.md`
- 可观测性收口：`commands/observability.md`

## 输出要求

- 先写当前风险，再写处理动作。
- 如果需要降级，明确说明降级范围和恢复条件。
- 如果需要等待外部资源恢复，明确说明系统在等待什么。
- 不要把临时止血方案包装成长期正确方案。
