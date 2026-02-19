init:
	uv sync

format:
	uv run ruff check --fix .
	uv run ruff format .

lint:
	uv run ruff check .
	uv run mypy .

test:
	uv run pytest
	
run:
	uv run python src/main.py

gdoc:
	uv run mkdocs serve

