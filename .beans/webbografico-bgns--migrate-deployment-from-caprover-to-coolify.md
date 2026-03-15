---
# webbografico-bgns
title: Migrate deployment from Caprover to Coolify
status: completed
type: task
priority: normal
created_at: 2026-03-15T11:55:33Z
updated_at: 2026-03-15T11:56:44Z
---

Remove captain-definition, update Gitea CI workflow to use Coolify webhook, update SKILLS.md deploy section. Codeberg #49.

## Summary of Changes\n\n- Removed `captain-definition` (Caprover-specific)\n- Updated `.gitea/workflows/deploy.yml` to use Coolify webhook (HTTP GET with Bearer token)\n- Updated `SKILLS.md` /deploy section: Caprover → Coolify\n\n**Secrets needed in Gitea repo:** `COOLIFY_WEBHOOK_URL` e `COOLIFY_WEBHOOK_TOKEN`
