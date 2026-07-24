
# Define the default recipe
default:
    @just --list

# ============================================================================
# Hugo
# ============================================================================

# Start Hugo development server with live reload
[group: 'hugo']
serve:
    hugo server --buildDrafts

# Build production site
[group: 'hugo']
build:
    hugo --minify

# Recompile Tailwind CSS (run only when layouts/*.html templates change)
[group: 'hugo']
css:
    bin/tailwindcss-macos-arm64 -i static/src/input.css -o static/css/tailwind.css --minify

# Build and test Docker image locally
[group: 'hugo']
docker-build:
    docker build -t webbografico:local .
    @echo "✓ Build complete. Run: docker run -p 8080:80 webbografico:local"


[group: 'quality']
lint:
    just _pre-commit run --all-files
    @echo "\n✓ Lint completato"
    @echo "⚠️  Se ci sono file modificati, devono essere ri-staged:"
    @git status --short 2>/dev/null | head -10 || true

# Lint and auto-stage all changes (use before commit)
[group: 'quality']
lint-stage:
    just lint
    @echo "\n📦 Auto-staging delle modifiche..."
    git add -A
    @echo "\n🔍 Eseguo pre-commit sui file staged..."
    just _pre-commit run || true
    @echo "\n📦 Re-staging dopo pre-commit fixes..."
    git add -A
    @echo "✓ File staged. Pronto per il commit"
    @git status --short

_pre-commit *args:
    pre-commit {{ args }}

# ============================================================================
# Beans
# ============================================================================

# List active beans (excludes completed and scrapped)
[group: 'beans']
beans:
    beans list --ready

# List completed beans
[group: 'beans']
beans_completed:
    beans list -s completed

# ============================================================================
# GitHub Issues
# ============================================================================

# List issues (state: open|closed|all)
[group: 'github']
issues state="open":
    gh issue list -R applewebbo/webbografico --state {{state}}

# Show issue details (with comments)
[group: 'github']
issue number:
    gh issue view -R applewebbo/webbografico {{number}} --comments

# Print raw body of an issue (markdown)
[group: 'github']
issue-body number:
    gh issue view -R applewebbo/webbografico {{number}} --json body -q .body

# Add comment to issue
[group: 'github']
issue-comment number text:
    gh issue comment -R applewebbo/webbografico {{number}} -b "{{text}}"

# Close issue
[group: 'github']
issue-close number:
    gh issue close -R applewebbo/webbografico {{number}}

# Reopen issue
[group: 'github']
issue-reopen number:
    gh issue reopen -R applewebbo/webbografico {{number}}

# Add labels to issue (space-separated)
[group: 'github']
issue-label number *labels:
    #!/usr/bin/env bash
    set -euo pipefail
    for label in {{labels}}; do
        gh issue edit -R applewebbo/webbografico {{number}} --add-label "$label"
    done

# Create new issue
[group: 'github']
issue-create title body="":
    gh issue create -R applewebbo/webbografico --title "{{title}}" --body {{ quote(body) }}

# ============================================================================
# GitHub Releases
# ============================================================================

# List all releases
[group: 'github']
release-list:
    gh release list -R applewebbo/webbografico

# Show release details
[group: 'github']
release-show tag:
    gh release view -R applewebbo/webbografico {{tag}}

# Create a new release (auto-creates tag and generates notes from commits)
[group: 'github']
release-create tag previous_tag="" draft="false" prerelease="false":
    #!/usr/bin/env bash
    set -euo pipefail

    # Create tag on current commit if missing
    if git rev-parse "{{tag}}" >/dev/null 2>&1; then
        echo "✓ Tag {{tag}} already exists locally"
    else
        echo "📝 Creating tag {{tag}} on current commit..."
        git tag "{{tag}}"
    fi

    # Push tag to origin
    echo "📤 Pushing tag {{tag}} to origin..."
    git push origin "{{tag}}" || true

    # Build gh release flags
    FLAGS="--generate-notes"
    [ "{{previous_tag}}" != "" ] && FLAGS="$FLAGS --notes-start-tag {{previous_tag}}"
    [ "{{draft}}" = "true" ] && FLAGS="$FLAGS --draft"
    [ "{{prerelease}}" = "true" ] && FLAGS="$FLAGS --prerelease"

    echo "🚀 Creating release on GitHub..."
    gh release create "{{tag}}" -R applewebbo/webbografico --title "{{tag}}" $FLAGS

# Delete a release (use with caution!)
[group: 'github']
release-delete tag:
    gh release delete -R applewebbo/webbografico "{{tag}}" --yes
