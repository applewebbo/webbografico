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

## Deployment

Push to Codeberg → Caprover rebuilds via multi-stage Dockerfile (Hugo build → Nginx serve).

```bash
# CSS must be recompiled and committed before deploy if templates changed
just css
git add static/css/tailwind.css
# then commit and push
```
