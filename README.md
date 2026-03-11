# codex-agency-agents

这是一个面向 Codex 的技能仓库，用来把上游 `agency-agents` 改造成更适合 Codex 使用的版本。

当前重点不是保留原仓库的展示风格，而是把它整理成一套能直接安装、直接调用、适合工程项目持续使用的技能体系。

## 先看这个说明

这个仓库和业务项目仓库不是同一个仓库，职责分两层：

- `codex-agency-agents`
  这是技能仓库，用来存放 Codex 可用的技能、精选 bundle、项目级模板和安装脚本。

- 业务项目仓库
  例如 `local_agent_meme_arb_trading`。这类仓库负责真正的业务代码和运行逻辑，并消费这里提供的技能。

如果你在别的机器上要使用这套技能，流程是：

1. clone 这个仓库
2. 在仓库根目录执行：

```powershell
python scripts/install_codex.py --bundle engineering-codex --bundle ops-codex
```

3. 重启 Codex
4. 打开你的业务项目

一句话总结：

- 这个仓库提供技能
- 业务项目消费技能

## 这个仓库提供什么

当前仓库提供两类内容：

### 1. 全量转换结果

把原始 agent 批量转换成 Codex 可识别的 `SKILL.md` 结构，放在：

- `integrations/codex/skills/`

适合想保留完整 agent 池、自己筛选的人。

### 2. 精选插件式 bundle

为了让 Codex 在真实工程项目里更好用，当前已经整理出两套精选 bundle：

- `engineering-codex`
- `ops-codex`

它们不仅包含技能，还包含：

- `AGENTS.md` 项目级规则模板
- `commands/` 工作流模板
- `connectors/` 连接器与 MCP 模板说明

## 当前推荐用法

如果你主要用 Codex 做工程开发，不建议直接安装全量技能，而是优先安装精选 bundle。

### 默认安装

```powershell
python scripts/install_codex.py
```

默认会安装：

- `engineering-codex`

### 推荐安装

```powershell
python scripts/install_codex.py --bundle engineering-codex --bundle ops-codex
```

这套组合适合：

- 后端服务
- 调度器和守护进程
- 实时系统
- 交易系统
- 监控与可观测性
- 发布前检查和线上故障处理

### 全量安装

```powershell
python scripts/install_codex.py --bundle full
```

适合你明确知道自己需要完整 agent 池，并愿意自己筛选使用场景的情况。

安装完成后，重启 Codex 让新技能生效。

## 两套精选 bundle 的定位

### engineering-codex

适合：

- 系统设计
- 功能实现
- 代码审查
- 安全审查
- 发布前检查
- 工程事故处理

说明文档：

- [integrations/codex/engineering-codex/README.md](integrations/codex/engineering-codex/README.md)

### ops-codex

适合：

- 长时间运行服务
- 调度器和后台 worker
- 可观测性与健康检查
- 第三方 API 配额与成本保护
- 故障响应和回滚

说明文档：

- [integrations/codex/ops-codex/README.md](integrations/codex/ops-codex/README.md)

## 在 Codex 里怎么用

你可以直接显式点名技能：

```text
Use $engineering-codex-implementation to implement this feature.
Use $engineering-codex-code-review to review this patch.
Use $ops-codex-cost-guard to reduce wasted API requests.
Use $ops-codex-observability to redesign this runtime dashboard.
```

如果业务项目根目录有 `AGENTS.md`，Codex 也会优先遵循项目级规则和推荐技能。

## 目录结构

```text
integrations/codex/
  README.md
  AGENTS.template.md
  skills/                  全量转换结果
  engineering-codex/       精选工程 bundle
  ops-codex/               精选运维与稳定性 bundle
scripts/
  convert_codex.py         生成 Codex 技能
  install_codex.py         安装 Codex 技能
```

## 给业务项目接入时怎么做

建议在业务项目里做两件事：

1. 安装这里的精选 bundle 到本机 `Codex`
2. 在业务项目根目录放一份项目级 `AGENTS.md`

这样 Codex 在打开业务项目时，既能加载全局技能，也能遵循项目自己的运行规则。

## 适合什么，不适合什么

适合：

- 需要长期维护的工程项目
- 希望把 Codex 用成稳定工程助手的人
- 希望统一项目级规则、技能和工作流模板的人

不适合：

- 只想保留原仓库展示风格而不关心 Codex 集成的人
- 只做一次性提示词复制，不需要项目级约束的人

## 上游关系

这个仓库基于上游 `agency-agents` 继续整理，重点放在：

- Codex 可安装
- 中文安装说明
- 精选 bundle
- 项目级规则
- 更适合真实工程项目的工作流模板

如果你要看更底层的原始 agent 素材，可以回到上游仓库；如果你要直接在 Codex 中使用，优先看本仓库的 `integrations/codex/`。
