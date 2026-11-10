# Scientific Computing with Python

A personal learning repository for scientific computing, numerical experiments, and computational physics.

The goal is to build reliable programming habits while connecting mathematical and physical ideas with numerical implementation. This repository is a learning portfolio: code, explanations, experiments, and observations will be added as the study progresses.

## Current focus

- Python fundamentals
- NumPy: arrays, indexing, broadcasting, vectorization, and linear algebra
- Numerical experiments connected to mathematics and physics

## Planned topics

- SciPy: numerical algorithms and scientific routines
- Pandas: tabular data analysis
- Matplotlib: scientific visualization
- Numerical linear algebra
- Classical mechanics simulations
- Later extensions: quantum information and computational physics

## Repository structure

```text
scientific-computing-with-python/
├── README.md
├── requirements.txt
├── python_basics/
│   └── README.md
├── numpy/
│   ├── README.md
│   └── 01_vector_norm_and_normalization.py
├── notebooks/
│   ├── 00_numpy_basic_concepts.ipynb
│   ├── 01_numpy_qubit_states.ipynb
│   └── 02_born_rule_measurement.ipynb
└── projects/
    └── numerical_linear_algebra/
        └── README.md
```

## Notebooks

- [00 — NumPy Fundamentals](notebooks/00_numpy_basic_concepts.ipynb)
- [01 — NumPy and Qubit States](notebooks/01_numpy_qubit_states.ipynb)
- [02 — Born Rule and Quantum Measurement](notebooks/02_born_rule_measurement.ipynb)

## Jupyter notebooks

VS Code users can install the Microsoft Python and Jupyter extensions, select this project's `.venv` interpreter, and open files in `notebooks/`. Install notebook kernel support with the requirements below.

## Getting started

Use Python 3.10 or newer.

Create and activate a virtual environment:

**Windows PowerShell**

```powershell
py -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the current dependency:

```bash
python -m pip install -r requirements.txt
```

Run the first NumPy example from the repository root:

```bash
python numpy/01_vector_norm_and_normalization.py
```

## How each experiment is documented

For each topic, I aim to record:

1. The mathematical or physical idea.
2. The numerical method and implementation.
3. Checks that validate the result.
4. Experiments, observations, and limitations.
5. References where relevant.

## Learning status

This repository is under active development. Completed topics and experiments will be documented as they are studied. Planned topics are not presented as completed work.

## Language

Code comments and project documentation may use English to build technical communication skills. Learning notes may also include Chinese explanations.
