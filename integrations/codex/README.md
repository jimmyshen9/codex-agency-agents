# Codex 集成说明

这个仓库已经补齐了面向 Codex 的两类用法：

- 全量技能集：把原始 agent 批量转换成 Codex 可识别的 `SKILL.md`
- 精选插件式 bundle：按实际工程工作流整理成更容易直接使用的技能包

如果你的目标是日常开发、调试、审查、发布和线上稳定性，建议优先安装精选 bundle，而不是一次性装全量技能。

## 默认安装方式

在仓库根目录执行：

```bash
python scripts/convert_codex.py
python scripts/install_codex.py
```

默认会安装 `engineering-codex`。

安装完成后，重启 Codex 让新技能生效。

## 常用安装命令

只安装工程精选包：

```bash
python scripts/install_codex.py --bundle engineering-codex
```

同时安装工程包和运维包：

```bash
python scripts/install_codex.py --bundle engineering-codex --bundle ops-codex
```

安装全量技能集：

```bash
python scripts/install_codex.py --bundle full
```

如果你想先装到临时目录验证：

```bash
python scripts/install_codex.py --bundle engineering-codex --dest .tmp-codex
```

## 推荐安装组合

### 只做开发

```bash
python scripts/install_codex.py
```

适合常规工程实现、代码审查、发布前检查。

### 做长时间运行服务或线上系统

```bash
python scripts/install_codex.py --bundle engineering-codex --bundle ops-codex
```

适合后端服务、监控、调度器、风控系统、交易系统、SRE 类项目。

### 做研究或横向参考

```bash
python scripts/install_codex.py --bundle full
```

适合想要完整 agent 池，自己筛选使用场景的人。

## 在 Codex 里怎么用

你可以显式点名技能：

```text
Use $engineering-codex-implementation to implement this feature.
Use $engineering-codex-code-review to review this patch.
Use $ops-codex-runtime-reliability to harden this long-running service.
Use $ops-codex-cost-guard to reduce wasted API requests.
```

如果项目根目录有 `AGENTS.md`，Codex 也会优先遵循项目级规则和推荐技能。

## 目录结构

```text
integrations/codex/
  README.md
  AGENTS.template.md
  skills/                  # 全量转换结果
  engineering-codex/       # 精选工程 bundle
  ops-codex/               # 精选运维与稳定性 bundle
```

## 精选 bundle 说明

### engineering-codex

适合：

- 系统设计
- 功能实现
- 代码审查
- 安全审查
- 发布检查
- 工程事故处理

说明文档见 [engineering-codex/README.md](engineering-codex/README.md)。

### ops-codex

适合：

- 长时间运行服务
- 调度器和守护进程
- 监控与可观测性
- 额度、配额、成本保护
- 故障响应与回滚

说明文档见 [ops-codex/README.md](ops-codex/README.md)。

## 项目级 AGENTS.md

如果你希望某个项目默认优先使用精选技能，把对应 bundle 里的 `AGENTS.md` 复制到项目根目录即可。

也可以把多个 bundle 的规则合并成一个项目级 `AGENTS.md`，让 Codex 在同一个项目里同时具备工程实现和运行稳定性约束。
