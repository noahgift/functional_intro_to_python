.PHONY: install fmt fmt-check lint type test cover comply notebooks \
        rust depyler snippets snippets-extract snippets-rust \
        run-part-1 run-part-2 \
        run-part-3 run-part-4 run-part-5 clean all

install:
	uv sync

fmt:
	uv run ruff format .

fmt-check:
	uv run ruff format --check .

lint:
	uv run ruff check .

type:
	uv run ty check funclib tests

test:
	uv run coverage run -m pytest

cover: test
	uv run coverage report

comply:
	pmat comply check

rust:
	cargo fmt --manifest-path rust/Cargo.toml --all -- --check
	cargo clippy --manifest-path rust/Cargo.toml --all-targets -- -D warnings
	cargo test --manifest-path rust/Cargo.toml -p funclib

depyler:
	depyler transpile funclib/funcmod.py -o rust/funclib/src/funcmod.depyler.rs

snippets-extract:
	uv run python scripts/extract_snippets.py
	uv run ruff format notebooks/_snippets

snippets:
	uv run ruff format --check notebooks/_snippets
	uv run ruff check notebooks/_snippets

snippets-rust:
	uv run python scripts/transpile_snippets.py

notebooks:
	uv run pytest --nbval-lax notebooks/*.ipynb

run-part-1:
	uv run jupyter nbconvert notebooks/Functional_Introduction_To_Python_Section_1\(Introductory_Concepts\).ipynb --to slides --post serve

run-part-2:
	uv run jupyter nbconvert notebooks/Functional_Introduction_To_Python_Section_2\(Functions\).ipynb --to slides --post serve

run-part-3:
	uv run jupyter nbconvert notebooks/Functional_Introduction_To_Python_Section_3\(Control_Structures\).ipynb --to slides --post serve

run-part-4:
	uv run jupyter nbconvert notebooks/Functional_Introduction_To_Python_Section_4\(Intermediate_Topics\).ipynb --to slides --post serve

run-part-5:
	uv run jupyter nbconvert notebooks/IO\ Python.ipynb --to slides --post serve

clean:
	rm -rf .coverage .pytest_cache .ruff_cache

all: install fmt-check lint type cover rust snippets
