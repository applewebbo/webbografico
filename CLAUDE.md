# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website/portfolio hosted at https://webbografico.com. Built with Hugo, Tailwind CSS v4 + DaisyUI v5 (standalone binaries), and AlpineJS. Deployed via Caprover with a multi-stage Dockerfile (Hugo build → Nginx serve).

## Tech Stack

- **Static Site Generator**: Hugo
- **CSS**: Tailwind CSS v4 + DaisyUI v5 via standalone CLI (`bin/tailwindcss-macos-arm64`)
- **JS**: AlpineJS (local files in `static/js/`)
- **Server**: Nginx
- **Task Runner**: just (see justfile)
- **Repository**: Codeberg (https://codeberg.org/webbografico/webbografico)

## Development Commands

### Hugo
```bash
just serve        # Hugo dev server with live reload (--buildDrafts)
just build        # Production build (hugo --minify)
just css          # Recompile Tailwind CSS (only when layouts/*.html change)
just docker-build # Build and test Docker image locally
```

### Code Quality
```bash
just lint        # Run pre-commit hooks
just lint-stage  # Lint and auto-stage all changes (use before commit)
```

### Issue Management (Codeberg)
```bash
just issues [state]                  # List issues (open|closed|all)
just issue <number>                  # Show issue details
just issue-body <number>             # Print raw markdown body
just issue-create <title> [body]     # Create new issue
just issue-comment <number> <text>   # Add comment
just issue-check <number> <step>     # Check a single task by text
just issue-check-all <number>        # Check all unchecked tasks
just issue-close <number>            # Close issue
just issue-reopen <number>           # Reopen issue
just issue-label <number> <labels>   # Add labels
```

**Note**: The project is hosted on Codeberg. Use the justfile commands above to manage issues.

## Architecture

### Content Structure
```
content/
  projects/<slug>/
    index.md        # frontmatter + body
    hero.jpg        # images alongside content (Page Bundle)
  blog/
    .gitkeep        # empty, ready for future posts
```

### Layouts
```
layouts/
  _default/baseof.html     # base template (AlpineJS dark mode, local CSS, Bunny fonts)
  index.html               # homepage (hero + projects + blog sections)
  projects/list.html       # projects grid
  projects/single.html     # project detail with gallery modal
  blog/list.html           # blog list (shows coming soon when empty)
  blog/single.html         # single post template
  partials/
    navbar.html
    footer.html
    gallery-modal.html     # AlpineJS gallery
  shortcodes/
    tech-badge.html
```

### CSS Workflow
Tailwind CSS is compiled once and committed (`static/css/tailwind.css`). Only recompile when HTML templates change:
```bash
just css
git add static/css/tailwind.css
```

### Production Deployment
- Multi-stage Dockerfile: `hugomods/hugo:exts` builds → `nginx:alpine` serves
- `nginx.conf`: gzip, 1yr cache on static assets, custom 404
- `captain-definition` points to Dockerfile

## Pre-commit Hooks

Configured hooks (`.pre-commit-config.yaml`):
- trim whitespace, fix end of files, check yaml, large files check
- rustywind (Tailwind class sorting)
- YAML/TOML formatting

## Git Commit Guidelines

- **ALWAYS USE `/commit` SKILL**: Never run `git commit` manually. The skill handles everything:
  - For **full commits** (all changes): Runs `just lint-stage` (lint + auto-stage + pre-commit hooks)
  - For **partial commits** (selected files only): Runs `just lint`, then user manually stages desired files
  - Creates conventional commit with Gitmoji
  - Handles all edge cases (new files, pre-commit fixes, etc.)
- **Partial vs Full Commits**:
  - **Full commit**: All modified files should be included → use `just lint-stage`
  - **Partial commit**: Only specific files should be included → use `just lint`, then `git add <files>` manually
  - ⚠️ **NEVER use `just lint-stage` for partial commits** as it stages ALL files with `git add -A`
- **Conventional Commits**: Format is `<emoji> <type>(<scope>): <description>`
- **Issue References**: Use "for #<number>" in commit message, or "fix #<number>" if closing the issue
- **Language**: Commit messages MUST be in English
- **NO CLAUDE IN COMMITS**: Never cite Claude or AI assistance in commit messages
- **NO AUTO-COMMITS**: Never execute `git commit` autonomously during coding tasks
- **EXCLUSIVE COMMAND**: Only create commits when user explicitly runs `/commit` or asks "please commit"
- **NO PUSH**: Never run `git push` unless explicitly requested

## Claude Code Skills

For detailed skill documentation, workflows, and best practices, read and follow the instructions in `SKILLS.md`.

Available skills: `/commit`, `/review`, `/release`
