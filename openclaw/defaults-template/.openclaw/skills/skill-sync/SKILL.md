---
name: skill-sync
description: 根据每个agent的skills白名单，自动同步技能列表到各自的AGENTS.md和SOUL.md
trigger: auto
---

# 执行规则

当你完成 openclaw skill install/remove/update 后，必须立即执行：

1. 读取 `~/.openclaw/openclaw.json` 中的 `agents.list`
2. 对每个 agent：
   - 获取其 `workspace` 路径
   - 获取其 `skills` 白名单（空数组=全部允许）
3. 扫描 `~/.openclaw/skills/` 下所有 SKILL.md，过滤出白名单内的技能
4. 更新该 agent 的 `AGENTS.md`：将技能列表写入 `<!-- SKILL_LIST -->` 标记之间
5. 更新该 agent 的 `SOUL.md`：将技能列表写入 `<!-- ABILITY_LIST -->` 标记之间
6. 在 `~/.openclaw/workspace/memory/evolution/` 下创建日志

跳过 `skill-sync` 自己的条目。