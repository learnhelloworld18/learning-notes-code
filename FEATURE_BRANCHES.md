# Working with Feature Branches

## Why Feature Branches?

Feature branches keep your work isolated from the main codebase until it's ready. This allows:
- Parallel development without conflicts
- Code review before merging
- Easy rollback if something breaks
- Clear history of changes

## Basic Workflow

### 1. Start from main
```bash
git checkout main
git pull origin main
```

### 2. Create a feature branch
```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/add-pandas-analysis`
- `fix/data-loading-bug`
- `docs/update-readme`
- `refactor/cleanup-script`

### 3. Make your changes
Edit files, test locally (e.g., `make run`), commit regularly:

```bash
git add .
git commit -m "Add data loading function"
git commit -m "Implement check_data statistics"
```

### 4. Push to remote
```bash
git push origin feature/your-feature-name
```

### 5. Create a Pull Request (PR)
On GitHub/GitLab/Gitea, create a PR from `feature/your-feature-name` → `main`.
Add description, request reviews, address feedback.

### 6. Merge to main
Once approved:
```bash
git checkout main
git pull origin main
git merge feature/your-feature-name
git push origin main
```

Or use the "Squash and merge" option in the PR UI to keep history clean.

### 7. Delete the branch
```bash
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

## Never on main

❌ **Don't do this:**
```bash
git checkout main
git add .
git commit -m "quick fix"
git push origin main
```

✅ **Do this instead:**
```bash
git checkout -b feature/quick-fix
git add .
git commit -m "quick fix"
git push origin feature/quick-fix
# Then create a PR
```

## Keeping your branch updated

If main has new changes:
```bash
git fetch origin
git rebase origin/main
# or merge: git merge origin/main
git push origin feature/your-feature-name --force-with-lease
```

## Summary

- Always create a feature branch for new work
- Keep main stable and deployable
- Use PRs for code review
- Delete branches after merging
