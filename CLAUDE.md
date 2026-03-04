# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website/portfolio hosted at https://webbografico.com. Built with Django 5.1, HTMX, Tailwind CSS (via django-tailwind-cli with DaisyUI), and Cloudinary for media.

## Tech Stack

- **Backend**: Django 5.1+ + Python 3.12+
- **Frontend**: HTMX + Tailwind CSS + DaisyUI
- **Database**: SQLite with WAL mode enabled
- **Server**: Granian (WSGI)
- **Package Management**: uv for Python
- **Task Runner**: just (see justfile)
- **Repository**: Codeberg (https://codeberg.org/webbografico/webbografico)

## Development Commands

### Setup
```bash
just install  # Install/sync Python dependencies
```

### Running the App
```bash
just local  # Run dev server with Tailwind watch mode
```

### Database
```bash
just migrate   # Run migrations
just manage makemigrations  # Create migrations
```

### Testing
```bash
just test   # Run pytest
just ftest  # Fast parallel tests (pytest -n 8 --reuse-db, 100% coverage required)
```

### Code Quality
```bash
just lint        # Run ruff check, ruff format, and pre-commit hooks
just lint-stage  # Lint and auto-stage all changes (use before commit)
just secure      # Run uv-secure for security checks
```

### Updates
```bash
just update_all          # Upgrade all packages
just update <package>    # Upgrade specific package
just lock                # Rebuild lock file
```

### Docker
```bash
just docker_up     # Start containers
just docker_build  # Build and start
just docker_down   # Stop and remove volumes
```

### Issue Management (Codeberg)
```bash
just issues [state]              # List issues (state: open|closed|all, default: open)
just issue <number>              # Show issue details
just issue-create <title> [body] # Create new issue
just issue-comment <number> <text> # Add comment to issue
just issue-close <number>        # Close issue
just issue-reopen <number>       # Reopen issue
just issue-label <number> <labels> # Add labels (space-separated)
```

**Note**: The project is hosted on Codeberg. Use the justfile commands above to manage issues.

## Architecture

### Apps Structure
- **core/**: Project settings, URLs, WSGI/ASGI config, contact form views
- **projects/**: Portfolio projects management with images (Cloudinary)

### Key Components

**Projects App** (projects/):
- `models.py`: `Project`, `ProjectImage` models with Cloudinary media
- `views.py`: HTMX-powered project list/detail views
- `admin.py`: Project and image administration

**Core App** (core/):
- Contact form with reCAPTCHA
- Custom views and URL routing

### Settings Configuration

Uses django-environ for environment variables. Key settings:
- **Media**: Cloudinary for image storage
- Mailgun email backend (django-anymail)
- SQLite with WAL mode
- Locale: Italian

### Frontend

- Templates in `templates/` directory
- HTMX for dynamic interactions
- Tailwind CSS with DaisyUI components
- django-browser-reload for live reloading in development

### Production Deployment

- Dockerfile uses Python 3.12-slim with uv
- Granian WSGI server
- WhiteNoise for static files
- entrypoint.sh: migrate → tailwind build → collectstatic → granian

## Pre-commit Hooks

Configured hooks:
- pyupgrade (--py312-plus)
- django-upgrade (Django 5.1)
- djade (Django template linting)
- ruff (check + format)
- bandit (security)
- rustywind (Tailwind class sorting)
- YAML/TOML formatting

## Testing Strategy

- Use pytest with `--reuse-db` flag
- Test files: `tests/` directory
- Coverage must be 100%

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

Available skills: `/commit`, `/makemigrations`, `/check-all`, `/review`, `/release`, `/pre-deploy`, `/db-backup`, `/deps-update`, `/cleanup`
