"""Monte Carlo simulation for a simple stochastic supply-chain reaction."""

from __future__ import annotations

from dataclasses import dataclass
import random


@dataclass
class State:
    supplier_a: int
    supplier_b: int
    product_c: int = 0
    byproduct_d: int = 0


def simulate(initial_a: int = 100, initial_b: int = 100, steps: int = 1_000,
             completion_probability: float = 0.9, seed: int | None = None) -> State:
    """Run one discrete-time simulation and return its final inventory state."""
    if min(initial_a, initial_b, steps) < 0:
        raise ValueError("initial stock and steps must be non-negative")
    if not 0 <= completion_probability <= 1:
        raise ValueError("completion_probability must be between 0 and 1")

    rng = random.Random(seed)
    state = State(initial_a, initial_b)
    for _ in range(steps):
        if state.supplier_a and state.supplier_b and rng.random() < completion_probability:
            state.supplier_a -= 1
            state.supplier_b -= 1
            state.product_c += 2
            state.byproduct_d += 1
    return state


def run_experiment(runs: int = 500, **kwargs) -> list[State]:
    """Run independent simulations with deterministic per-run seeds."""
    return [simulate(seed=seed, **kwargs) for seed in range(runs)]


if __name__ == "__main__":
    results = run_experiment()
    completed = [state.product_c for state in results]
    print(f"mean products: {sum(completed) / len(completed):.2f}")
