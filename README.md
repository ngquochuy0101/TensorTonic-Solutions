# TensorTonic Solutions

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Required-orange.svg)](https://numpy.org/)

A practical collection of machine learning and deep learning exercises implemented from scratch with NumPy.

The repository currently contains **47 standalone implementations**, each in its own directory.

## Table of Contents

- [Overview](#overview)
- [What Is Included](#what-is-included)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [How to Run](#how-to-run)
- [Algorithm Catalog](#algorithm-catalog)
- [Development Notes](#development-notes)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository focuses on implementation-first learning:

- Core ML and DL concepts written with NumPy
- No high-level ML frameworks required
- One concept per folder for easy exploration
- Script-style files that can be run directly

## What Is Included

| Area | Count | Examples |
|---|---:|---|
| Optimizers, training, and LR schedules | 10 | `adagrad-optimizer`, `adamw-optimizer`, `nadam-optimizer`, `cosine-annealing-lr` |
| Losses and objectives | 5 | `hinge-loss`, `huber-loss`, `mean-squared-error`, `log-loss-per-sample` |
| Distances and linear algebra | 6 | `cosine-similarity`, `euclidean-distance`, `dot-product`, `matrix-trace` |
| Statistics and probability | 10 | `mean-median-mode`, `sample-var-std`, `binomial-pmf-cdf`, `entropy-node` |
| Preprocessing and feature engineering | 13 | `one-hot-encoding`, `tfidf-vectorizer`, `zscore-standardization`, `impute-missing` |
| Models and evaluation helpers | 3 | `linear-regression-closed-form`, `random-forest-vote`, `precision-recall-at-k` |

## Project Structure

The repository uses a flat folder layout:

```text
TensorTonic-Solutions/
|-- README.md
|-- adadelta-optimizer/
|   `-- adadelta-optimizer.py
|-- adagrad-optimizer/
|   `-- adagrad-optimizer.py
|-- ...
|-- warmup-decay-lr/
|   `-- warmup-decay-lr.py
`-- zscore-standardization/
    `-- zscore-standardization.py
```

Convention: each folder contains one Python file with the same base name as the folder.

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/your-username/TensorTonic-Solutions.git
cd TensorTonic-Solutions
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install numpy
```

## How to Run

Each implementation is runnable as a script.

Example:

```bash
cd cosine-similarity
python cosine-similarity.py
```

Another example:

```bash
cd adagrad-optimizer
python adagrad-optimizer.py
```

Notes:

- Many files include sample input and `print(...)` output directly in the script body.
- File names use hyphens, so direct `import module_name` is not always convenient without renaming or dynamic imports.

## Algorithm Catalog

### Optimizers, Training, and Schedules

- `adadelta-optimizer`
- `adagrad-optimizer`
- `adamw-optimizer`
- `nadam-optimizer`
- `nesterov-momentum`
- `rmsprop-optimizer`
- `gradient-clipping`
- `cosine-annealing-lr`
- `warmup-decay-lr`
- `logistic-regression-training`

### Losses and Objectives

- `hinge-loss`
- `huber-loss`
- `mean-squared-error`
- `log-loss-per-sample`
- `wasserstein-critic-loss`

### Distances and Linear Algebra

- `cosine-similarity`
- `euclidean-distance`
- `manhattan-distance`
- `dot-product`
- `matrix-trace`
- `make-diagonal`

### Statistics, Probability, and Tree Metrics

- `mean-median-mode`
- `sample-var-std`
- `percentiles`
- `expected-value-discrete`
- `bernoulli-pmf`
- `binomial-pmf-cdf`
- `geometric-pmf-mean`
- `entropy-node`
- `gini-impurity`
- `information-gain`

### Preprocessing and Feature Engineering

- `one-hot-encoding`
- `ordinal-encoding`
- `frequency-encoding`
- `tfidf-vectorizer`
- `zscore-standardization`
- `log-transform`
- `differencing`
- `binning`
- `rank-transform`
- `impute-missing`
- `streaming-minmax`
- `pad-sequences`
- `kfold-split`

### Models and Evaluation Helpers

- `linear-regression-closed-form`
- `random-forest-vote`
- `precision-recall-at-k`

## Development Notes

- This repository is educational and implementation-oriented.
- Some scripts include debug or demonstration prints by default.
- If you want import-friendly modules, consider renaming files from `kebab-case.py` to `snake_case.py` and moving sample run code under:

```python
if __name__ == "__main__":
    ...
```

## Requirements

Minimum runtime dependency:

```text
numpy>=1.19.0
```

## Contributing

Contributions are welcome.

Suggested contribution checklist:

1. Keep functions deterministic and documented.
2. Add edge-case handling where relevant.
3. Prefer vectorized NumPy operations.
4. Include a small usage example in the script.

## License

No `LICENSE` file is currently present in this repository.

If you plan to distribute or accept external contributions, add a license file (for example MIT) at the repository root.

---

Last updated: March 19, 2026