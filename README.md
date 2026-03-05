# TensorTonic Solutions

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Required-orange.svg)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A comprehensive collection of machine learning and deep learning algorithms implemented from scratch in Python, featuring optimization techniques, loss functions, statistical methods, and data preprocessing utilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Catalog](#algorithm-catalog)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## 🎯 Overview

This repository contains pure NumPy implementations of fundamental machine learning algorithms and utilities sourced from [TensorTonic](https://tensortonic.com) — a platform dedicated to hands-on implementation of ML/DL concepts from first principles.

Each implementation focuses on:
- **Clarity**: Well-documented, readable code
- **Correctness**: Mathematically rigorous implementations
- **Educational Value**: Learning through implementation
- **Minimal Dependencies**: Using only NumPy for core computations

## ✨ Features

- **30+ Algorithm Implementations**: Covering optimization, loss functions, metrics, and preprocessing
- **From-Scratch Approach**: No high-level ML libraries, pure mathematical implementations
- **Modular Design**: Each algorithm in its own directory for easy exploration
- **Production-Ready Code**: Vectorized operations using NumPy for efficiency
- **Comprehensive Coverage**: From basic statistics to advanced optimization techniques

## 📁 Project Structure

```
TensorTonic-Solutions/
├── README.md
│
├── Optimization Algorithms/
│   ├── adagrad-optimizer/           # Adaptive Gradient Algorithm
│   ├── adamw-optimizer/             # Adam with Weight Decay
│   ├── rmsprop-optimizer/           # Root Mean Square Propagation
│   └── nesterov-momentum/           # Nesterov Accelerated Gradient
│
├── Loss Functions/
│   ├── huber-loss/                  # Robust regression loss
│   ├── hinge-loss/                  # SVM classification loss
│   ├── mean-squared-error/          # L2 regression loss
│   └── wasserstein-critic-loss/     # GAN discriminator loss
│
├── Distance & Similarity Metrics/
│   ├── cosine-similarity/           # Angular similarity measure
│   ├── euclidean-distance/          # L2 distance metric
│   └── manhattan-distance/          # L1 distance metric
│
├── Statistical Methods/
│   ├── mean-median-mode/            # Central tendency measures
│   ├── sample-var-std/              # Sample variance & std deviation
│   ├── percentiles/                 # Quantile calculations
│   ├── entropy-node/                # Shannon entropy for decision trees
│   └── expected-value-discrete/     # Discrete probability distributions
│
├── Probability Distributions/
│   ├── bernoulli-pmf/               # Binary outcome distribution
│   ├── binomial-pmf-cdf/            # Binomial probabilities
│   └── geometric-pmf-mean/          # Geometric distribution
│
├── Data Preprocessing/
│   ├── one-hot-encoding/            # Categorical variable encoding
│   ├── pad-sequences/               # Sequence padding for RNNs
│   ├── differencing/                # Time series stationarity
│   ├── log-transform/               # Logarithmic transformation
│   └── streaming-minmax/            # Online normalization
│
├── Linear Algebra Operations/
│   ├── dot-product/                 # Vector inner product
│   ├── matrix-trace/                # Trace of square matrices
│   └── make-diagonal/               # Diagonal matrix construction
│
├── Learning Rate Schedulers/
│   ├── cosine-annealing-lr/         # Cosine annealing schedule
│   └── warmup-decay-lr/             # Warmup + decay schedule
│
└── Evaluation Metrics/
    └── precision-recall-at-k/       # Top-K recommendation metrics
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/TensorTonic-Solutions.git
   cd TensorTonic-Solutions
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install numpy
   ```

## 💻 Usage

Each algorithm is self-contained in its directory. Navigate to any folder and run the Python script:

### Example 1: Cosine Similarity

```python
import numpy as np
from cosine_similarity import cosine_similarity

a = np.array([1, 2, 3])
b = np.array([2, 4, 6])

similarity = cosine_similarity(a, b)
print(f"Cosine Similarity: {similarity:.4f}")  # Output: 1.0000
```

### Example 2: AdaGrad Optimizer

```python
import numpy as np
from adagrad_step import adagrad_step

w = np.array([1.0])      # Parameters
g = np.array([1.0])      # Gradient
G = np.array([0.0])      # Accumulated squared gradients
lr = 0.1                 # Learning rate

w_new, G_new = adagrad_step(w, g, G, lr=lr, eps=1e-8)
print(f"Updated weights: {w_new}")
```

### Example 3: One-Hot Encoding

```python
import numpy as np
from one_hot import one_hot

labels = [0, 1, 2, 1, 0]
encoded = one_hot(labels, num_classes=3)
print(encoded)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [0. 1. 0.]
#  [1. 0. 0.]]
```

## 📚 Algorithm Catalog

### Optimization Algorithms

| Algorithm | Description | Key Features |
|-----------|-------------|--------------|
| **AdaGrad** | Adaptive learning rates per parameter | Good for sparse data |
| **AdamW** | Adam with decoupled weight decay | Better generalization |
| **RMSprop** | Moving average of squared gradients | Handles non-stationary objectives |
| **Nesterov** | Momentum with lookahead | Faster convergence |

### Loss Functions

| Function | Type | Use Case |
|----------|------|----------|
| **Huber Loss** | Regression | Robust to outliers |
| **Hinge Loss** | Classification | Support Vector Machines |
| **MSE** | Regression | Standard squared error |
| **Wasserstein** | GAN | Critic loss for WGANs |

### Preprocessing & Feature Engineering

- **One-Hot Encoding**: Convert categorical variables to binary vectors
- **Pad Sequences**: Uniform length sequences for RNN input
- **Differencing**: Remove trends in time series data
- **Log Transform**: Reduce skewness in distributions
- **Streaming MinMax**: Online feature scaling

### Statistical & Probability Tools

- **Entropy**: Information gain for decision trees
- **Percentiles**: Robust outlier detection
- **Expected Value**: Discrete probability calculations
- **Bernoulli/Binomial/Geometric**: Probability distributions

## 📦 Requirements

```
numpy>=1.19.0
```

For development:
```
pytest>=6.0.0      # For testing
black>=21.0        # For code formatting
flake8>=3.9.0      # For linting
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue describing the problem
2. **Suggest Enhancements**: Share ideas for new algorithms or improvements
3. **Submit Pull Requests**: 
   - Fork the repository
   - Create a feature branch (`git checkout -b feature/new-algorithm`)
   - Commit your changes (`git commit -m 'Add XYZ algorithm'`)
   - Push to the branch (`git push origin feature/new-algorithm`)
   - Open a Pull Request

### Code Style Guidelines

- Follow PEP 8 conventions
- Include docstrings for all functions
- Add type hints where applicable
- Write unit tests for new implementations
- Keep implementations dependency-minimal (NumPy only)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[TensorTonic](https://tensortonic.com)**: For providing the platform and algorithmic challenges
- **NumPy Community**: For the foundational numerical computing library
- **ML Community**: For open-source educational resources

## 📧 Contact

For questions or discussions, feel free to open an issue or reach out through GitHub.

---

**⭐ Star this repository if you find it helpful!**

*Last Updated: March 2026*
