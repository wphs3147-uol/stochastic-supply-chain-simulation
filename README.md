# Stochastic supply-chain simulation

An educational Monte Carlo model of a supply process in which one unit of A
and one unit of B probabilistically become two units of product C and one unit
of by-product D.

The original notebook was a useful sketch but mixed parameters, simulation,
and plotting in one cell. The public entry points are now
`stochastic_supply_chain.py` and
[`notebooks/stochastic_supply_chain_demo.ipynb`](notebooks/stochastic_supply_chain_demo.ipynb),
which separate the state model from the experiment runner and make each run
reproducible with a seed.

## What it demonstrates

- state transitions in a discrete-time stochastic process;
- validation of model parameters;
- Monte Carlo repetition and reproducibility;
- a clear boundary between simulation logic and reporting.

This is a teaching model, not a forecast of a real supply chain.

```bash
python stochastic_supply_chain.py
```
