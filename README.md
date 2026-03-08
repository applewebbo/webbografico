# webbografico.com

Personal website and portfolio at [webbografico.com](https://webbografico.com).

## Stack

- [Hugo](https://gohugo.io/) — static site generator
- [Tailwind CSS v4](https://tailwindcss.com/) + [DaisyUI v5](https://daisyui.com/) — standalone binaries, zero Node/npm
- [AlpineJS](https://alpinejs.dev/) — dark mode toggle, gallery modal
- [Nginx](https://nginx.org/) — production server
- [Caprover](https://caprover.com/) — deployment

## Development

```bash
just serve        # Hugo dev server with live reload
just build        # Production build (hugo --minify)
just css          # Recompile Tailwind CSS (only when layouts change)
just docker-build # Build and test Docker image locally
```

## Content

Content is managed as Hugo Page Bundles in `content/`:

```
content/
  projects/<slug>/
    index.md      # frontmatter + description
    hero.jpg      # images live alongside the content
  blog/
    .gitkeep      # ready for future posts
```

Edit content in [Obsidian](https://obsidian.md/) by opening `content/` as a vault.

## Content Editing (Obsidian)

Open the `content/` folder as an Obsidian vault. No Hugo knowledge required.

### Add a new project

1. Create a folder: `content/projects/<slug>/`
2. Create `index.md` with this frontmatter:
   ```yaml
   ---
   title: "Project Name"
   date: 2025-01-01
   weight: 1
   short_desc: "Short description for the card"
   live_url: "https://example.com"
   source_code_url: "https://codeberg.org/..."
   technologies: ["Django", "HTMX", "Tailwind"]
   hero_image: "hero.jpg"
   gallery:
     - image: "screenshot-1.jpg"
       caption: "Caption"
   ---
   ```
3. Drag images into the same folder (alongside `index.md`)
4. Optimize images with [ImageOptim](https://imageoptim.com/) before committing

### Edit a static page (About, etc.)

Static pages live directly in `content/` as single `.md` files:

```yaml
---
title: "About"
---

Page content here.
```

The file `content/about.md` is served at `/about/`.

### Add a blog post

Create `content/blog/<slug>.md`:
```yaml
---
title: "Post title"
date: 2025-01-01
draft: false
tags: ["django", "tutorial"]
description: "Excerpt shown in the list"
---

Post content here.
```

### Preview locally

```bash
just serve
# open http://localhost:1313
```

### When to recompile CSS

Only when HTML files in `layouts/` change:
```bash
just css
git add static/css/tailwind.css
```

### Publish

```bash
git add .
git commit -m "add project: <name>"
git push
# Caprover auto-rebuilds from Codeberg
```

## Deployment

Multi-stage Dockerfile: Hugo builds the static site → Nginx serves it. No Python, no Node in the final image.

### Deploy via CLI (current)

```bash
caprover deploy --host https://captain.<your-domain> --appName webbografico --branch main
```

Or interactively:
```bash
caprover deploy
```

### Deploy via Webhook (recommended)

Set up once, then every push to `main` on Codeberg triggers an automatic deploy.

**1. Enable webhook in Caprover**
- Open Caprover dashboard → Apps → `webbografico` → Deployment tab
- Enable "Trigger Build on Push" → copy the webhook URL

**2. Add webhook in Codeberg**
- Go to repo Settings → Webhooks → Add Webhook
- Payload URL: paste the Caprover webhook URL
- Content type: `application/json`
- Trigger: "Push events" on branch `main`
- Save

From that point, `git push origin main` automatically rebuilds and deploys.

### Before any deploy

If HTML templates in `layouts/` changed, recompile CSS first:
```bash
just css
git add static/css/tailwind.css
git commit -m "chore(css): recompile tailwind"
git push origin main
```
