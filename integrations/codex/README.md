# Codex Integration

The Agency can be used with Codex by packaging each agent as a Codex skill.
This integration generates one skill per agent under `integrations/codex/skills/`
and installs them into `~/.codex/skills/`.

## Install

```bash
# Generate Codex skills
./scripts/convert.sh --tool codex

# Install them into ~/.codex/skills/
./scripts/install.sh --tool codex
```

For Windows or environments without a working Bash setup, use the Python entry points from the repository root:

```bash
python scripts/convert_codex.py
python scripts/install_codex.py
```

## Use in Codex

After installation, Codex can:

- auto-trigger a matching Agency skill when the task matches its description
- use a skill explicitly when you mention its skill name in a prompt

Examples:

```text
Use $agency-backend-architect to design this API.
```

```text
Use $agency-reality-checker to review whether this feature is production ready.
```

## Project-Scoped AGENTS.md

Codex also supports project-level instruction files. This repo ships an example
template at `integrations/codex/AGENTS.template.md` that you can copy into a
project as `AGENTS.md` when you want to recommend a subset of Agency skills or
set project-specific operating rules.

## Skill Layout

Each generated Codex skill looks like this:

```text
integrations/codex/skills/
  agency-backend-architect/
    SKILL.md
```

The generated `SKILL.md` keeps the original Agency persona, rules, workflows,
and deliverables, while wrapping them in Codex-compatible skill frontmatter.

## Curated Bundle

If you do not want the full 112-skill set, use the curated engineering bundle:

```bash
python scripts/install_codex.py --bundle engineering-codex
```

It lives under `integrations/codex/engineering-codex/` and includes:

- a smaller high-quality engineering skill set
- project-level `AGENTS.md`
- `commands/` workflow templates for review, debug, architecture, release, and incidents
- `connectors/` MCP and external system templates

See [engineering-codex/README.md](engineering-codex/README.md) for details.
