---
# webbografico-g8ul
title: Multilingual IT/EN site with Hugo i18n
status: completed
type: feature
priority: normal
created_at: 2026-04-14T13:25:36Z
updated_at: 2026-04-14T13:40:26Z
---

Implement full Hugo multilingual support for IT and EN versions of the site. Closes issue #52.

## Plan

- [x] Configure `hugo.toml` with `[languages]` block (it/en, both with URL prefix, separate menus)
- [x] Create `i18n/it.yaml` and `i18n/en.yaml` with all UI strings
- [x] Replace hardcoded strings in layouts with `i18n "key"` calls
- [x] Add language toggle (IT|EN) in navbar using `.Translations`
- [x] Use `index.it.md` / `index.en.md` pattern in page bundles (no subdir needed)
- [x] Translate project pages (short_desc + body) into English
- [x] Translate about.md into English
- [x] Recompile Tailwind CSS
- [x] Test both language versions

## Summary of Changes

- `hugo.toml`: added `[languages]` block with IT/EN, `defaultContentLanguageInSubdir = true`, separate menus per language
- `i18n/it.yaml` + `i18n/en.yaml`: all UI strings externalized
- Layouts updated with `i18n "key"` calls: navbar, index, projects/single, projects/list, blog/list, project-card
- Navbar: language toggle IT|EN using `.Translations` (avoids deprecated `.Site.Languages`)
- Content: renamed `index.md` → `index.it.md`, added `index.en.md` for all 4 projects
- `about.md` → `about.it.md` + `about.en.md`
- Fixed `max-w-screen-lg` → `max-w-5xl` in navbar
