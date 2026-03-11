# ops-codex

这是一个面向 Codex 的精选运维与稳定性 bundle。

它适合有这些特点的项目：

- 服务需要长时间运行
- 有调度器、守护进程、后台 worker
- 依赖第三方 API、额度、配额或速率限制
- 需要明确的监控、告警、回滚和故障处置流程

## 包含内容

- `ops-codex-runtime-reliability`
- `ops-codex-observability`
- `ops-codex-incident-response`
- `ops-codex-release-safety`
- `ops-codex-cost-guard`

## 安装

单独安装：

```bash
python scripts/install_codex.py --bundle ops-codex
```

和工程包一起安装：

```bash
python scripts/install_codex.py --bundle engineering-codex --bundle ops-codex
```

安装完成后，重启 Codex 让新技能生效。

## 使用

在 Codex 中显式点名：

```text
Use $ops-codex-runtime-reliability to harden this scheduler.
Use $ops-codex-observability to redesign the dashboard and health checks.
Use $ops-codex-cost-guard to stop wasting credits on repeated 403 requests.
```

## commands 目录怎么用

`commands/` 里的文件是工作流模板，不是 Codex 原生命令。适合两种使用方式：

- 复制模板内容到当前对话，让 Codex 按模板执行
- 在项目根目录的 `AGENTS.md` 中引用这些模板，作为默认工作方式

## connectors 目录怎么用

`connectors/` 提供的是连接器模板和约束说明，方便你在不同项目中接入：

- GitHub
- Sentry
- Grafana / Prometheus
- Datadog
- Telegram / Slack
- 私有监控或日志系统

## 适用范围

适合：

- 线上系统稳定性
- 守护进程和调度器
- 实时系统与监控系统
- API 配额、credits、速率限制控制
- 发布安全与故障响应

不适合：

- 单纯的界面设计
- 以内容创作为主的任务
- 不涉及运行态约束的轻量脚本需求
