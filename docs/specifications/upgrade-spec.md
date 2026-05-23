# Upgrade Specification: Functional Intro to Python

**Status:** Draft
**Owner:** Noah Gift
**Date:** 2026-05-23

## 1. Goals

Modernize this repository to a strict, reproducible, provably-correct
teaching codebase that doubles as a showcase for the Pragmatic AI Labs
course catalog. Every Python example must be transpilable to Rust via
`depyler` and meet the same quality bar in both languages.

### 1.1 Non-negotiable outcomes

1. **`pmat comply`** passes with zero findings on every commit.
2. **100% line + branch test coverage** across `funclib/` and any new
   modules (enforced in CI; no exemptions, no `# pragma: no cover`).
3. **Provable contracts** on every public function: pre/postconditions,
   property-based tests, and (where applicable) formal invariants checked
   by `icontract` + `hypothesis`.
4. **Toolchain lockdown:** `uv`, `ruff`, and `ty` — and ONLY these.
   No `pip`, no `poetry`, no `pipenv`, no `pylint`, no `black`, no `mypy`,
   no `pytest-cov` invoked via `pip`. Period.
5. **Rust parity:** every example in `funclib/` and every notebook code
   cell has a `depyler`-generated Rust twin under `rust/` that passes the
   equivalent quality gates.
6. **README** promotes the full PAIML course catalog above the fold.

## 2. Toolchain (ALLOWED LIST — exhaustive)

| Concern              | Tool      | Invocation                          |
|----------------------|-----------|-------------------------------------|
| Env + deps           | `uv`      | `uv sync`, `uv add`, `uv run`       |
| Lint + format        | `ruff`    | `uv run ruff check`, `ruff format`  |
| Type check           | `ty`      | `uv run ty check`                   |
| Test + coverage      | `pytest` via `uv` with `coverage.py` (run as `uv run`) |
| Property tests       | `hypothesis` (via `uv`)             |
| Contracts            | `icontract` (via `uv`)              |
| Quality gate         | `pmat comply`                       |
| Py→Rust transpile    | `depyler`                           |
| Rust quality         | `cargo fmt`, `cargo clippy -D warnings`, `cargo test`, `cargo llvm-cov` |

**Banned:** `pip`, `pip-tools`, `poetry`, `pipenv`, `conda`, `setup.py`,
`pylint`, `black`, `isort`, `flake8`, `mypy`, `pyright`, `tarpaulin`.

Remove `requirements.txt` and the `pip`/`pylint` Makefile targets. Replace
with `pyproject.toml` managed by `uv` and a uv-lockfile (`uv.lock`)
committed to the repo.

## 3. Repository Layout (target)

```
.
├── pyproject.toml           # uv-managed, single source of truth
├── uv.lock                  # committed
├── Makefile                 # uv-only targets
├── funclib/                 # Python source (typed, contracts)
├── tests/                   # 100% coverage, property + unit
├── rust/                    # depyler output + hand-curated Cargo workspace
│   ├── Cargo.toml
│   └── funclib/
├── notebooks/               # unchanged surface, but cells must pass ruff+ty
├── docs/specifications/
│   └── upgrade-spec.md      # this file
└── README.md                # course-catalog-forward
```

## 4. Quality Gates (CI)

All gates run via `uv run` or `cargo` — never via system Python.

### 4.1 Python gate

```bash
uv sync --frozen
uv run ruff format --check .
uv run ruff check .
uv run ty check funclib tests
uv run coverage run -m pytest --hypothesis-show-statistics
uv run coverage report --fail-under=100 --show-missing
pmat comply --strict
```

### 4.2 Rust gate (per crate in `rust/`)

```bash
cargo fmt --all -- --check
cargo clippy --all-targets -- -D warnings
cargo llvm-cov --fail-under-lines 100 --fail-under-functions 100
```

### 4.3 Depyler parity gate

```bash
depyler transpile funclib/ --out rust/funclib/src/
# Re-run Rust gate; transpiled output must compile and pass tests.
```

A CI job diffs `rust/` against a fresh `depyler` run and fails on drift.

## 5. Contracts & Properties

Every public function in `funclib/` MUST have:

1. **Type annotations** accepted by `ty` with zero warnings.
2. **`@icontract.require` / `@icontract.ensure`** clauses for any
   non-trivial precondition or postcondition. Pure-total functions still
   declare a postcondition (even if it's a type/range assertion).
3. **At least one `hypothesis` property test** exercising the contract
   across the input domain.
4. **Docstring** with a `Contract:` section restating the invariants in
   plain English (for the teaching audience).

Example shape:

```python
import icontract

@icontract.require(lambda xs: all(isinstance(x, int) for x in xs))
@icontract.ensure(lambda result, xs: result == sum(xs))
def total(xs: list[int]) -> int:
    """Sum a list of ints.

    Contract:
      - Requires: every element is an int.
      - Ensures:  result equals the mathematical sum.
    """
    return sum(xs)
```

## 6. Depyler-ization of Examples

### 6.1 Scope

- All modules under `funclib/`.
- Every executable code cell in `notebooks/*.ipynb` is extracted to a
  `.py` snippet under `notebooks/_snippets/` and transpiled.

### 6.2 Process per example

1. Refactor the Python source to a depyler-friendly subset (explicit
   types, no dynamic dispatch on untyped values, no `*args/**kwargs` in
   hot paths).
2. Run `depyler transpile <file>.py -o rust/.../<file>.rs`.
3. Hand-write idiomatic Rust tests mirroring the Python `hypothesis`
   properties (using `proptest`).
4. Ensure parity: same inputs → same outputs, asserted by a small
   cross-language fixture runner under `tests/parity/`.

### 6.3 Standards mirror

| Python standard            | Rust equivalent                          |
|----------------------------|------------------------------------------|
| `ruff` lint clean          | `clippy -D warnings` clean               |
| `ty` type-clean            | `rustc` (already enforced)               |
| `icontract` pre/post       | `debug_assert!` + `proptest` invariants  |
| 100% coverage              | `cargo llvm-cov --fail-under-lines 100`  |
| `pmat comply`              | `pmat comply` (Rust-aware)               |

## 7. Makefile (target shape)

```make
.PHONY: install fmt lint type test cover comply rust all

install:
	uv sync --frozen

fmt:
	uv run ruff format .

lint:
	uv run ruff check .

type:
	uv run ty check funclib tests

test:
	uv run coverage run -m pytest

cover: test
	uv run coverage report --fail-under=100 --show-missing

comply:
	pmat comply --strict

rust:
	cd rust && cargo fmt --all -- --check && \
	  cargo clippy --all-targets -- -D warnings && \
	  cargo llvm-cov --fail-under-lines 100

all: install fmt lint type cover comply rust
```

## 8. README Changes

Rewrite the top of `README.md` to lead with the PAIML course catalog
(GenAI, Professional Rust, AWS AI & Analytics, Production GenAI on AWS,
Rust DevOps Mastery, Production ML Program) plus the Coursera/Duke Cloud
Computing specialization and any current O'Reilly live trainings. The
functional Python tutorial becomes section 2.

Add badges for: `uv`, `ruff`, `ty`, `pmat comply`, coverage 100%,
`depyler` Rust parity.

## 9. Migration Plan (phased)

1. **P0 — Toolchain swap.** Delete `requirements.txt`, add
   `pyproject.toml` + `uv.lock`, rewrite `Makefile`, wire CI. Verify all
   notebooks still execute under `uv run jupyter`.
2. **P1 — Type + lint clean.** Annotate `funclib/funcmod.py`; get
   `ruff` and `ty` to zero. Add `pmat comply` gate.
3. **P2 — Contracts + 100% coverage.** Add `icontract` + `hypothesis`;
   raise coverage gate to 100%.
4. **P3 — Depyler pass.** Stand up `rust/` workspace; transpile and
   add Rust quality gates; add parity tests.
5. **P4 — README refresh.** Course catalog forward; add badges.
6. **P5 — Notebook extraction.** Extract notebook cells to snippets,
   transpile, gate.

Each phase ships as its own PR against `main` and must pass the full
gate set before merge.

## 10. Acceptance Criteria

- `make all` is green on a clean clone with only `uv`, `cargo`, `pmat`,
  and `depyler` installed.
- CI shows: `pmat comply` ✅, coverage 100% ✅, `ty` ✅, `ruff` ✅,
  Rust gate ✅, depyler-drift ✅.
- README's first screen advertises the PAIML course catalog.
- No reference to `pip`, `pylint`, `black`, `mypy`, or `poetry` remains
  in the repo (grep-enforced in CI).
