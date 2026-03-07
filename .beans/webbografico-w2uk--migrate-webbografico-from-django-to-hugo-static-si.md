---
# webbografico-w2uk
title: Migrate webbografico from Django to Hugo static site
status: in-progress
type: epic
priority: normal
created_at: 2026-03-06T15:28:34Z
updated_at: 2026-03-07T14:33:02Z
---

Full migration from Django 5.1 to Hugo static site generator. Remove contact form, keep Tailwind CSS + DaisyUI + AlpineJS, deploy via Caprover with Nginx. Content managed via markdown files edited in Obsidian on macOS.


## Vincoli

- **Zero Node/npm/bun ovunque**: Tailwind CSS standalone CLI + DaisyUI `.mjs` standalone
- AlpineJS servito come file locale da `static/js/` (già presente)
- Hugo installato come singolo binario — nessuna dipendenza di runtime
- **Docker build**: scarica binari standalone → `tailwindcss --minify` + `hugo --minify` → Nginx serve `public/`
- `bin/tailwindcss-macos-arm64` (locale) e `daisyui.mjs`/`daisyui-theme.mjs` in `static/src/`

## Fasi

### Fase 1 — Setup Hugo
- [x] Installare Hugo (`brew install hugo`)
- [x] Inizializzare struttura Hugo nel repo esistente (sostituisce Django)
- [x] Configurare `hugo.toml` (baseURL, lingua italiana, menu, sezioni)
- [x] Scaricare Tailwind CSS standalone binary (`tailwindcss-macos-arm64`) in `bin/`
- [x] Scaricare DaisyUI standalone files (`daisyui.mjs`, `daisyui-theme.mjs`) in `static/src/`
- [x] Aggiornare `static/src/input.css` con sintassi Tailwind v4 + DaisyUI v5 standalone
- [x] Rimuovere `node_modules/`, dipendenze npm, `bun.lockb`
- [x] Aggiungere `just css` che usa il binario standalone
- [x] Compilare CSS una volta e committare `static/css/tailwind.css`

### Fase 2 — Layout / Templates
Convertire template Django → layout Hugo:
- [x] `layouts/_default/baseof.html` ← `base.html` (AlpineJS dark mode, CSS locale, fonts Bunny)
- [x] `layouts/index.html` ← `core/index.html` (hero + lista progetti + sezione blog)
- [x] `layouts/projects/list.html` ← `projects/projects-list.html` (grid card)
- [x] `layouts/projects/single.html` ← `project-detail.html` (gallery modal AlpineJS)
- [x] `layouts/blog/list.html` ← `article-list.html` (mostra "coming soon" se nessun post)
- [x] `layouts/blog/single.html` ← template articolo singolo (pronto per il futuro)
- [x] `layouts/partials/navbar.html` ← `navbar.html` (rimuovere link Contatti)
- [x] `layouts/partials/footer.html` ← `footer.html`
- [x] `layouts/partials/gallery-modal.html` ← `gallery-modal.html` (AlpineJS invariato)
- [x] `layouts/shortcodes/tech-badge.html` per i badge tecnologie

### Fase 3 — Struttura Contenuti
- [x] Creare `content/projects/` con Page Bundles (ogni progetto = cartella con `index.md` + immagini)
- [x] Creare `content/blog/.gitkeep` (sezione pronta, vuota)
- [x] Definire frontmatter progetti:
  ```yaml
  title: "Nome Progetto"
  slug: "nome-progetto"
  short_desc: "Descrizione breve per la card"
  live_url: "https://..."
  source_code_url: "https://..."
  technologies: ["Django", "HTMX", "Tailwind"]
  hero_image: "hero.jpg"
  weight: 1
  ```
- [x] Definire frontmatter blog post:
  ```yaml
  title: "Titolo articolo"
  date: 2025-01-01
  draft: false
  tags: ["django", "tutorial"]
  description: "Excerpt mostrato nella lista"
  ```

### Fase 4 — Migrazione Contenuti da Django
- [x] Script Python one-shot: esporta progetti da SQLite → file `.md` con frontmatter
- [x] Script Python one-shot: scarica immagini da Cloudinary → `content/projects/<slug>/`
- [x] Copiare `static/img/logo-panda.png` e `hero_image.jpg` (già presenti)
- [x] Copiare `static/js/alpine*.min.js` (già presenti)

### Fase 5 — Deployment Caprover
- [x] Nuovo `Dockerfile` multi-stage senza bun/Node:
  ```dockerfile
  # Stage 1: build Hugo
  FROM hugomods/hugo:latest AS builder
  WORKDIR /src
  COPY . .
  RUN hugo --minify

  # Stage 2: serve con Nginx
  FROM nginx:alpine
  COPY --from=builder /src/public /usr/share/nginx/html
  COPY nginx.conf /etc/nginx/conf.d/default.conf
  EXPOSE 80
  ```
- [x] Creare `nginx.conf` (gzip, cache headers statici, custom 404)
- [x] Aggiornare `captain-definition` (rimane puntato a Dockerfile)
- [x] Testare build Docker in locale

### Fase 6 — Giustfile aggiornato
- [x] `just serve` → `hugo server` (dev locale con live reload)
- [x] `just build` → `hugo --minify`
- [x] `just css` → `bin/tailwindcss-macos-arm64 -i static/src/input.css -o static/css/tailwind.css --minify`
- [x] `just docker-build` → build e test Docker in locale
- [x] Rimuovere tutti i comandi Django

### Fase 7 — Pulizia Django
- [x] Rimuovere `core/`, `projects/`, `tests/`, `conftest.py`
- [x] Rimuovere `manage.py`, `pyproject.toml`, `uv.lock`
- [x] Rimuovere `package.json`, `package-lock.json`, `node_modules/`, `bun.lockb`
- [x] Rimuovere `entrypoint.sh`, `db/`, `media/`, `staticfiles/`
- [x] Aggiornare `.gitignore` (ignorare `public/`, mantenere `static/css/tailwind.css`)
- [x] Aggiornare `README.md` e `CLAUDE.md`

### Fase 8 — Workflow Obsidian (documentazione)
- [ ] Documentare: aprire `content/` come vault Obsidian
- [ ] Documentare: aggiungere nuovo progetto (crea cartella, `index.md` con frontmatter, drag-drop immagini)
- [ ] Documentare: aggiungere post blog
- [ ] Documentare: quando ricompilare il CSS (solo se si modificano template `.html`)
- [ ] Raccomandare ImageOptim per ottimizzare immagini prima del commit

## Struttura repo post-migrazione

```
content/
  projects/
    webbografico/
      index.md
      hero.jpg
      screenshot-1.jpg
  blog/
    .gitkeep
layouts/
  _default/
    baseof.html
    single.html
  projects/
    list.html
    single.html
  blog/
    list.html
    single.html
  partials/
    navbar.html
    footer.html
    gallery-modal.html
  shortcodes/
    tech-badge.html
static/
  css/
    tailwind.css        ← compilato e committato, NON generato in Docker
  js/
    alpine.min.js
    alpine-collapse.min.js
    alpine-persist.min.js
  img/
    logo-panda.png
    hero_image.jpg
  src/
    input.css           ← sorgente Tailwind (per ricompilare in locale)
  src/
    input.css           ← sorgente Tailwind v4 standalone
    daisyui.mjs         ← DaisyUI v5 standalone plugin
    daisyui-theme.mjs   ← DaisyUI v5 theme plugin
bin/
  tailwindcss-macos-arm64  ← standalone CLI (gitignored per arch, scaricato con just install)
hugo.toml
Dockerfile              ← multi-stage: hugo build + nginx serve
nginx.conf
captain-definition
justfile
```

## Workflow CSS (quando cambiano i template)

```bash
just css    # standalone binary compila, aggiorna static/css/tailwind.css
git add static/css/tailwind.css
# poi commit e push → Caprover rebuilda
```

### Fase 7b — Pulizia pre-commit hooks Django
- [ ] Rimuovere hook Python/Django: pyupgrade, django-upgrade, djade, ruff, bandit
- [ ] Valutare rustywind (Tailwind class sorting — ancora utile per template Hugo)
- [ ] Mantenere hook generici: trim whitespace, fix end of files, check yaml, large files, toml/yaml formatting
- [ ] Aggiornare comandi lint nel justfile
- [ ] Fare insieme alla Fase 7

## Summary Phase 1
- Hugo v0.157.0 initialized in repo (hugo new site . --force)
- hugo.toml configured: baseURL webbografico.com, language it, menus Home/About
- Tailwind CSS v4 + DaisyUI v5 fully standalone: bin/tailwindcss-macos-arm64 + static/src/daisyui.mjs
- input.css migrated to Tailwind v4 syntax with @plugin directives
- tailwind.config.js removed (config now in CSS)
- package.json, node_modules, bun.lockb removed
- .gitignore updated: bin/tailwindcss-* ignored, public/ ignored, static/css/tailwind.css tracked
- just css, just serve, just build, just docker-build added to justfile
- CSS compiled and committed (static/css/tailwind.css)

## Summary Phase 2
- Converted all Django/Cotton templates to Hugo layouts
- Heroicons replaced with inline SVGs
- HTMX removed: projects rendered statically via Hugo range
- Cotton components converted to Hugo partials (project-card, blog-excerpt)
- gallery-modal.html: AlpineJS unchanged
- Added _default/terms.html for tags taxonomy
- Hugo builds cleanly in ~18ms with zero warnings

## Summary Phase 3
- content/projects/ created with .gitkeep (ready for Page Bundles)
- content/blog/ created with .gitkeep (empty, ready for future posts)
- archetypes/projects.md: frontmatter with title, date, weight, short_desc, live_url, source_code_url, hero_image, technologies, gallery
- archetypes/blog.md: frontmatter with title, date, draft, tags, description
- Hugo builds cleanly (4 pages)

## Summary Phase 4
- Migrated 3 projects from production SQLite DB (db/db_prod.sqlite3)
- Downloaded all images from Cloudinary to content/projects/<slug>/
- Projects: webbografico (5 gallery imgs), menu-scolastico-old (3), menu (4)
- Static assets (logo, hero, alpine JS) already in place
- Hugo builds cleanly: 8 pages, 15 non-page files in 51ms

## Summary Phase 5
- Dockerfile: hugomods/hugo:exts AS builder → nginx:alpine, no Python/Node/bun
- nginx.conf: gzip, 1yr cache on static assets, try_files routing, custom 404
- captain-definition unchanged (points to Dockerfile)
- Docker build: Hugo v0.154.5, 8 pages in 21ms
- Container smoke test: / and /projects/webbografico/ return HTTP 200

## Summary Phase 6
- Removed Django-specific commands: bootstrap, local, secure, requirements, update_all, update, migrate, test, ftest
- Kept: lint, lint-stage, _pre-commit (used by lint, will be updated in Phase 7b)
- Added `just issue-body <number>`: prints raw markdown body of a Codeberg issue
- Added `just issue-check-all <number>`: checks all unchecked items in an issue (via new `check-all` command in bin/codeberg)
- justfile now only contains: hugo, quality (lint/lint-stage), beans, codeberg commands

## Summary Phase 7
- Removed Django codebase: core/, projects/, tests/, conftest.py
- Removed: manage.py, pyproject.toml, uv.lock, bun.lockb, entrypoint.sh
- Removed: db/ (sqlite3 files), media/, staticfiles/, htmlcov/
- .gitignore rewritten: removed Python/Django boilerplate, kept macOS/Hugo/Tailwind/env entries
- README.md rewritten: Hugo stack, development commands, content workflow
- CLAUDE.md rewritten: Hugo stack, new just commands, updated architecture
