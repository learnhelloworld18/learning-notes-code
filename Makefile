.PHONY: all sync run pre-commit push

all: sync run

# Creates .venv/ automatically if missing, then installs deps
sync:
	uv sync

pre-commit:
	uv run -- pre-commit run --all-files

run:
	sync
	uv run -- python src/script.py

# usage -- make push MSG="Add feature X"
push: sync pre-commit
	git add .
	git commit -m "$(MSG)" || true
	git push --set-upstream origin $(git rev-parse --abbrev-ref HEAD)



# other commands

# $ uv add pandas numpy             # Add production dependencies
# $ uv add --dev pytest flake8	  # Add development dependencies
# $ uv remove pandas                # Remove a dependency
