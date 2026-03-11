# engineering-codex

这是一个面向 Codex 的精选工程插件式 bundle。

设计思路借鉴了 Anthropic 的 `knowledge-work-plugins` 工程插件分层方式：

- `skills/` 放高质量精选技能
- `commands/` 放可复用的工程工作流模板
- `connectors/` 放连接器和 MCP 配置模板
- `AGENTS.md` 放项目级选择规则

但实现方式改成了 Codex 可直接使用的形式：

- 所有技能都是 `SKILL.md`
- 所有说明优先中文
- 不使用 emoji
- 面向 Codex 的代码编辑、调试、审查、发布和事故处理

## 包含内容

- `engineering-codex-system-design`
- `engineering-codex-implementation`
- `engineering-codex-code-review`
- `engineering-codex-release-check`
- `engineering-codex-security-review`
- `engineering-codex-devops-delivery`
- `engineering-codex-incident-response`

## 安装

在仓库根目录执行：

```bash
python scripts/install_codex.py --bundle engineering-codex
```

如果只想安装到临时目录测试：

```bash
python scripts/install_codex.py --bundle engineering-codex --dest .tmp-engineering-codex
```

## 使用

在 Codex 中可以显式点名：

```text
Use $engineering-codex-system-design to design this service.
Use $engineering-codex-code-review to review this patch.
Use $engineering-codex-incident-response to drive this outage response.
```

也可以把本目录下的 [AGENTS.md](D:/Coding/量化/codex-agency-agents/integrations/codex/engineering-codex/AGENTS.md) 复制到项目根目录，作为项目级默认工程规则。

## commands 目录怎么用

`commands/` 里的文件不是 Codex 原生命令，而是工作流模板。适合两种用法：

- 复制文件内容到当前对话，要求 Codex 按模板执行
- 在项目 `AGENTS.md` 中引用这些模板，作为默认流程

## connectors 目录怎么用

`connectors/` 里只放模板，不绑定具体厂商或私有地址。你可以按项目情况接：

- GitHub
- Jira / Linear
- Sentry
- Datadog / Grafana
- 内部文档或知识库

## 适用范围

这个 bundle 适合：

- 日常开发
- 架构设计
- 代码实现
- 代码审查
- 发布前检查
- 安全审查
- 线上事故处理

不适合：

- 市场、设计、内容、游戏等非工程工作
- 需要大量人格化表达的演示型 agent 场景
