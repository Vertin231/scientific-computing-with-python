"""A first NumPy experiment: norms and normalization of a qubit state.

Run from the repository root:
    python numpy/01_vector_norm_and_normalization.py
"""

import numpy as np


def normalize_qubit_state(state: np.ndarray) -> np.ndarray:
    """Return a normalized two-component complex state vector.

    Raises:
        ValueError: If the input is not a finite, non-zero vector of shape (2,).
    """
    state = np.asarray(state, dtype=np.complex128)

    if state.shape != (2,):
        raise ValueError("A single-qubit state must be a vector of shape (2,).")

    if not np.all(np.isfinite(state)):
        raise ValueError("The state vector must contain only finite values.")

    norm = np.linalg.norm(state)

    if np.isclose(norm, 0.0):
        raise ValueError("The zero vector cannot be normalized.")

    normalized_state = state / norm

    # Check <psi|psi> = 1. np.vdot conjugates its first argument.
    inner_product = np.vdot(normalized_state, normalized_state)
    if not np.isclose(inner_product, 1.0):
        raise ArithmeticError("Normalization check failed.")

    return normalized_state


def main() -> None:
    # Example 1: |phi> = [1, i*sqrt(3)]^T
    phi = np.array([1.0, 1j * np.sqrt(3.0)], dtype=np.complex128)

    print("Example 1")
    print("Original state:", phi)
    print("Original norm:", np.linalg.norm(phi))

    psi = normalize_qubit_state(phi)
    print("Normalized state:", psi)
    print("<psi|psi>:", np.vdot(psi, psi))
    print("Is normalized:", np.isclose(np.vdot(psi, psi), 1.0))

    # Example 2: a different complex vector
    chi = np.array([2.0 + 1j, 3.0 - 2j], dtype=np.complex128)
    chi_normalized = normalize_qubit_state(chi)

    print("\nExample 2")
    print("Normalized state:", chi_normalized)
    print("Norm after normalization:", np.linalg.norm(chi_normalized))
    print("<chi|chi>:", np.vdot(chi_normalized, chi_normalized))

    # A normalized state must have non-negative measurement probabilities
    # whose sum is one in the computational basis.
    probabilities = np.abs(psi) ** 2
    print("\nComputational-basis probabilities for Example 1:")
    print("P(0):", probabilities[0])
    print("P(1):", probabilities[1])
    print("Total probability:", probabilities.sum())

    assert np.all(probabilities >= 0.0)
    assert np.isclose(probabilities.sum(), 1.0)


if __name__ == "__main__":
    main()
