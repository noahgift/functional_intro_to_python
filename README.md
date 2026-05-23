# 🎓 Pragmatic AI Labs | Functional Intro to Python (& Rust)

[![uv](https://img.shields.io/badge/packaging-uv-DE5FE9)](https://github.com/astral-sh/uv)
[![ruff](https://img.shields.io/badge/lint-ruff-261230)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/types-ty-3776AB)](https://github.com/astral-sh/ty)
[![pmat comply](https://img.shields.io/badge/pmat-comply-2E8B57)](#quality-gates)
[![coverage 100%](https://img.shields.io/badge/coverage-100%25-brightgreen)](#quality-gates)
[![depyler](https://img.shields.io/badge/Py%E2%86%92Rust-depyler-orange)](https://crates.io/crates/depyler)

> Modernized: `uv` + `ruff` + `ty` only · 100% branch coverage · `icontract`
> + `hypothesis` provable contracts · every example transpilable to Rust via
> `depyler` and held to `clippy -D warnings` + `proptest` parity.
> See [`docs/specifications/upgrade-spec.md`](docs/specifications/upgrade-spec.md).

---

## 🎓 Courses — Coursera + Duke

If this tutorial helps you, please ⭐ the repo and enroll in the
**Building Cloud Computing Solutions at Scale** specialization (4 courses,
Coursera + Duke University):

* [Take the Specialization](https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale)
* [Cloud Computing Foundations](https://www.coursera.org/learn/cloud-computing-foundations-duke?specialization=building-cloud-computing-solutions-at-scale)
* [Cloud Virtualization, Containers & APIs](https://www.coursera.org/learn/cloud-virtualization-containers-api-duke?specialization=building-cloud-computing-solutions-at-scale)
* [Cloud Data Engineering](https://www.coursera.org/learn/cloud-data-engineering-duke?specialization=building-cloud-computing-solutions-at-scale)
* [Cloud Machine Learning Engineering & MLOps](https://www.coursera.org/learn/cloud-machine-learning-engineering-mlops-duke?specialization=building-cloud-computing-solutions-at-scale)

---

<a id="quality-gates"></a>
## 🔒 Quality Gates (this repo)

Single source of truth for the toolchain. **No `pip`, no `pylint`, no
`black`, no `mypy`, no `poetry`** — enforced by CI grep.

| Concern        | Tool                  | Make target |
|----------------|-----------------------|-------------|
| Env + deps     | `uv`                  | `make install` |
| Lint + format  | `ruff`                | `make lint`, `make fmt-check` |
| Type check     | `ty`                  | `make type` |
| Tests + cov    | `pytest` + `coverage` | `make cover` (100% required) |
| Contracts      | `icontract` + `hypothesis` | runs via `make cover` |
| Compliance     | `pmat comply`         | `make comply` |
| Py → Rust      | `depyler`             | `make depyler` |
| Rust gate      | `cargo fmt` + `clippy -D warnings` + `proptest` | `make rust` |

Run everything: `make all`.

---

# Functional, Data Science Intro To Python

The first section is an intentionally brief, functional, data-science-centric
introduction to Python. The assumption is that someone with zero programming
experience can follow this tutorial and learn Python with the smallest
amount of information possible.

The sections after that vary in difficulty and cover Machine Learning,
Linear Optimization, build systems, commandline tools, recommendation
engines, Sentiment Analysis, and Cloud Computing.

## Lessons

* [Lesson 1: Introductory Concepts](notebooks/)
* [Lesson 2: Functions](notebooks/)
* [Lesson 3: Control Structures](notebooks/)
* [Lesson 4: Intermediate Topics — Classes, Modules, Libraries](notebooks/)
* [Lesson 5: IO in Python](notebooks/)

The notebook files live under [`notebooks/`](notebooks/). Run them with
`uv run jupyter lab` after `make install`.

## License

The text content of these notebooks is released under the
[CC-BY-NC-ND license](license.md).
