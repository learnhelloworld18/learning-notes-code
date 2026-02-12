
# learning-notes-code

This repository contains Python code and notes for learning data analysis, best practices, and modern development workflows.

## Features
- Data analysis with pandas and numpy
- Automated testing with pytest
- Pre-commit hooks for linting and formatting (Black, Ruff)
- SAST (Static Application Security Testing) with CodeQL and Bandit (via GitHub Actions)
- CI workflows for linting, testing, and building
- Example Makefile for common tasks

## Project Structure
```
├── src/                  # Source code
│   └── script.py
├── data.csv              # Example dataset
├── tests/                # Test files
├── Makefile              # Common automation commands
├── pyproject.toml        # Project dependencies and config
├── .pre-commit-config.yaml  # Pre-commit hooks
├── .github/              # GitHub Actions and templates
│   ├── workflows/
│   │   └── sast.yml      # SAST workflow (CodeQL, Bandit)
│   └── ...
```

## Setup
1. Install [uv](https://github.com/astral-sh/uv) (or use pip):
	 ```bash
	 pip install uv
	 ```
2. Install dependencies (including dev tools):
	 ```bash
	 uv sync --dev
	 ```
3. (Optional) Install pre-commit hooks:
	 ```bash
	 uv run -- pre-commit install
	 ```

## Usage
- Run the main script:
	```bash
	uv run -- python src/script.py
	```
- Run all pre-commit checks:
	```bash
	make pre-commit
	```
- Run tests:
	```bash
	pytest
	```

## Contributing
- Use feature branches for new work
- Open pull requests for review
- Fill out issue and PR templates
- All code is checked by pre-commit and SAST workflows

## License
MIT
