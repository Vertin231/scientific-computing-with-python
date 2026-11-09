# NumPy

This directory contains small, focused experiments using NumPy.

## Topics

- Array creation and data types
- Shape, dimensions, indexing, and slicing
- Boolean and fancy indexing
- Array operations and broadcasting
- Universal functions and aggregation
- Linear algebra
- Complex-valued vectors used in introductory quantum mechanics

## First experiment

Run from the repository root:

```bash
python numpy/01_vector_norm_and_normalization.py
```

The script demonstrates vector norms, complex inner products, and normalization of a two-component complex vector.

For a complex vector, the inner product must conjugate one argument. In NumPy, `np.vdot(a, b)` conjugates the first argument.
