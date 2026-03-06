
# Define the default recipe
default:
    @just --list

# Bootstrap the project (UV and BUN needed)
bootstrap:
    uv venv
    source .venv/bin/activate
    uv sync
    bun add -D daisyui@latest

# Run the local development server
local:
    python manage.py tailwind runserver

[group: 'quality']
lint:
    uv run ruff check --fix --unsafe-fixes .
    uv run ruff format .
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

[group: 'quality']
secure:
    uv-secure

_pre-commit *args:
    uvx prek {{ args }}

# Install requirements
requirements:
    uv sync --all-extras

# Update all packages
update_all:
    uv sync --upgrade

# Update a specific package
update *package:
    uv sync --upgrade-package {{ package }}

# Run database migrations
migrate:
    python manage.py migrate

# Run tests
test:
    uv run pytest --reuse-db -s

# Run fast tests
ftest:
    uv run pytest -n 8 --reuse-db

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
# Codeberg Issues
# ============================================================================

# List issues (state: open|closed|all)
[group: 'codeberg']
issues state="open":
    ./bin/codeberg list {{state}}

# Show issue details
[group: 'codeberg']
issue number:
    ./bin/codeberg show {{number}}

# Add comment to issue
[group: 'codeberg']
issue-comment number text:
    ./bin/codeberg comment {{number}} "{{text}}"

# Mark a checkbox step as done in issue body
[group: 'codeberg']
issue-check number step:
    ./bin/codeberg check {{number}} "{{step}}"

# Close issue
[group: 'codeberg']
issue-close number:
    ./bin/codeberg close {{number}}

# Reopen issue
[group: 'codeberg']
issue-reopen number:
    ./bin/codeberg reopen {{number}}

# Add labels to issue (space-separated)
[group: 'codeberg']
issue-label number *labels:
    ./bin/codeberg label {{number}} {{labels}}

# Create new issue
[group: 'codeberg']
issue-create title body="":
    ./bin/codeberg create "{{title}}" {{ quote(body) }}

# ============================================================================
# Codeberg Releases
# ============================================================================

# List all releases
[group: 'codeberg']
release-list:
    #!/usr/bin/env bash
    set -euo pipefail
    TOKEN=$(grep "^CODEBERG_API_TOKEN=" .env | cut -d'=' -f2 | tr -d '"' | tr -d "'")
    echo -e "TAG\tNAME\tPUBLISHED\tDRAFT"
    curl -s "https://codeberg.org/api/v1/repos/webbografico/webbografico/releases" \
      -H "Authorization: token ${TOKEN}" | \
      jq -r '.[] | "\(.tag_name)\t\(.name)\t\(.published_at)\t\(.draft)"' | \
      column -t -s $'\t'

# Show release details
[group: 'codeberg']
release-show tag:
    #!/usr/bin/env bash
    set -euo pipefail
    TOKEN=$(grep "^CODEBERG_API_TOKEN=" .env | cut -d'=' -f2 | tr -d '"' | tr -d "'")
    curl -s "https://codeberg.org/api/v1/repos/webbografico/webbografico/releases/tags/{{tag}}" \
      -H "Authorization: token ${TOKEN}" | \
      jq -r '"\nTag: \(.tag_name)\nName: \(.name)\nPublished: \(.published_at)\nDraft: \(.draft)\nPrerelease: \(.prerelease)\n\nURL: \(.html_url)\n\nBody:\n\(.body)\n"'

# Create a new release (auto-creates tag, pushes it, and generates notes from commits)
[group: 'codeberg']
release-create tag previous_tag="" draft="false" prerelease="false":
    #!/usr/bin/env bash
    set -euo pipefail

    # Check if tag already exists locally
    if git rev-parse "{{tag}}" >/dev/null 2>&1; then
        echo "✓ Tag {{tag}} already exists locally"
    else
        echo "📝 Creating tag {{tag}} on current commit..."
        git tag "{{tag}}"
        echo "✓ Tag {{tag}} created"
    fi

    # Push tag to origin
    echo "📤 Pushing tag {{tag}} to origin..."
    if git push origin "{{tag}}" 2>&1 | grep -q "already exists"; then
        echo "✓ Tag {{tag}} already exists on remote"
    else
        echo "✓ Tag {{tag}} pushed to origin"
    fi

    # Get token
    TOKEN=$(grep "^CODEBERG_API_TOKEN=" .env | cut -d'=' -f2 | tr -d '"' | tr -d "'")

    # Determine previous tag if not provided
    if [ "{{previous_tag}}" = "" ]; then
        PREV_TAG=$(git tag --sort=-version:refname | grep -v "{{tag}}" | head -1)
    else
        PREV_TAG="{{previous_tag}}"
    fi

    echo "🔍 Generating release notes (comparing with ${PREV_TAG})..."

    # Generate release notes from commits
    COMMITS=$(git log ${PREV_TAG}..{{tag}} --pretty=format:"- %s" --reverse 2>/dev/null || echo "- Initial release")

    # Parse commits into categories
    FEATURES=$(echo "$COMMITS" | grep -E "^- (✨|feat)" || true)
    FIXES=$(echo "$COMMITS" | grep -E "^- (🐛|fix)" || true)
    CHORES=$(echo "$COMMITS" | grep -E "^- (🔧|chore|📦|build|🎨)" || true)
    TESTS=$(echo "$COMMITS" | grep -E "^- (🧪|test|✅)" || true)
    DOCS=$(echo "$COMMITS" | grep -E "^- (📚|docs)" || true)

    # Build release body
    NL=$'\n'
    BODY="## What's New in {{tag}}${NL}${NL}"

    if [ -n "$FEATURES" ]; then
        BODY+="### 🚀 Features${NL}$FEATURES${NL}${NL}"
    fi

    if [ -n "$FIXES" ]; then
        BODY+="### 🐛 Bug Fixes${NL}$FIXES${NL}${NL}"
    fi

    if [ -n "$CHORES" ]; then
        BODY+="### 🛠️ Maintenance${NL}$CHORES${NL}${NL}"
    fi

    if [ -n "$TESTS" ]; then
        BODY+="### 🧪 Testing${NL}$TESTS${NL}${NL}"
    fi

    if [ -n "$DOCS" ]; then
        BODY+="### 📖 Documentation${NL}$DOCS${NL}${NL}"
    fi

    BODY+="### 📖 Full Changelog${NL}https://codeberg.org/webbografico/webbografico/compare/${PREV_TAG}...{{tag}}"

    # Create release via API
    echo "🚀 Creating release on Codeberg..."
    curl -s -X POST "https://codeberg.org/api/v1/repos/webbografico/webbografico/releases" \
      -H "Authorization: token ${TOKEN}" \
      -H "Content-Type: application/json" \
      -d "$(jq -n \
        --arg tag "{{tag}}" \
        --arg body "$BODY" \
        --argjson draft {{draft}} \
        --argjson prerelease {{prerelease}} \
        '{tag_name: $tag, name: $tag, body: $body, draft: $draft, prerelease: $prerelease}'
      )" | jq -r '"\n✓ Release created successfully!\nURL: \(.html_url)\n"'

# Delete a release (use with caution!)
[group: 'codeberg']
release-delete tag:
    #!/usr/bin/env bash
    set -euo pipefail
    TOKEN=$(grep "^CODEBERG_API_TOKEN=" .env | cut -d'=' -f2 | tr -d '"' | tr -d "'")
    echo "⚠️  Deleting release {{tag}}..."
    curl -X DELETE "https://codeberg.org/api/v1/repos/webbografico/webbografico/releases/tags/{{tag}}" \
      -H "Authorization: token ${TOKEN}"
    echo "✓ Release {{tag}} deleted"
