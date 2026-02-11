.PHONY: all sync run

all: sync run

sync:
	uv sync

run:
	sync
	uv run -- python src/script.py
