---
name: push-and-create-pr
description: Push the current feature branch to GitHub remote and create a Pull Request using the gh CLI. Use when the user asks to push a branch and open a PR, submit a PR, push to GitHub and create PR, or any workflow involving pushing a feature branch and creating a pull request.
---

# Push Feature Branch & Create PR

## Workflow

### Step 1 — Pre-flight checks

Run these in parallel:

```bash
git status
git log --oneline origin/$(git rev-parse --abbrev-ref HEAD)..HEAD 2>/dev/null || git log --oneline -10
git branch -a
```

Confirm:
- There are commits to push
- The current branch is NOT `main` or `develop`
- The `gh` CLI is available (`gh --version`)

### Step 2 — Determine base branch

Default base branch selection:
- If branch name starts with `feature/`, `fix/`, `chore/`, `refactor/` → base is `develop`
- If branch name starts with `hotfix/`, `release/` → base is `main`
- If unsure, ask the user

### Step 3 — Push to remote

```bash
git push -u origin HEAD
```

If the push fails due to diverged history, report the error and **stop**. Do not force push without explicit user permission.

### Step 4 — Gather PR context

Before writing the PR, collect:

```bash
git log --oneline origin/<base-branch>...HEAD
git diff origin/<base-branch>...HEAD --stat
```

Use this to write:
- **Title**: concise one-line summary (in English)
- **Body**: Summary bullets + test plan checklist

### Step 5 — Create PR

```bash
gh pr create \
  --title "<title>" \
  --base <base-branch> \
  --body "$(cat <<'EOF'
## Summary
- <bullet 1>
- <bullet 2>

## Test plan
- [ ] <test item 1>
- [ ] <test item 2>
EOF
)"
```

### Step 6 — Confirm & report

After success, output the PR URL from `gh pr create` output and show it to the user.

---

## Rules

- **Never force push** unless the user explicitly asks
- **All PR content (title, body, commit messages) must be in English**
- If `gh` is not authenticated, run `gh auth status` to diagnose and tell the user to run `gh auth login`
- If there are uncommitted changes, remind the user to commit or stash them first

## Quick reference

| Command | Purpose |
|---------|---------|
| `git push -u origin HEAD` | Push current branch and set upstream |
| `gh pr create` | Create PR interactively or with flags |
| `gh pr view --web` | Open the PR in the browser |
| `gh auth status` | Check GitHub CLI authentication |
