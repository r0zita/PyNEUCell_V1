# PyNEUCell_V1
PyNEUCell is a Python framework for coupling NEURON electrophysiology with MCell4 reaction–diffusion simulations to model nerve terminal function for mouse NMJ
The current reference model targets the mouse neuromuscular junction, while the framework is designed to support other species and synaptic systems.


## Overview

Traditional reaction–diffusion simulations often rely on simplified or static stimulation protocols.  
In contrast, <PROJECT_NAME> uses **physiologically realistic, dynamically changing action potentials** to control molecular simulations, enabling a tight coupling between membrane electrophysiology and stochastic chemical dynamics.

The current reference implementation models the **mouse neuromuscular junction (NMJ)**, where precise spike timing and waveform shape critically influence synaptic transmission.  
While the present models focus on the mouse NMJ, the framework itself is **species-agnostic** and designed to be extended to other synaptic systems.

---

## Repository Structure

```text
.
├── model.py              # Main entry point
├── parameters.py         # Global parameters and constants
├── shared.py             # Shared utilities and helpers
├── instantiation.py      # Object and species instantiation
├── subsystem.py          # Reaction–diffusion subsystem definitions
├── customization.py      # Simulation-specific customization hooks
├── observables.py        # Output definitions and observables
│
├── geometry/             # MCell geometry files
└── NEURON_RATES/         # Precomputed NEURON-derived rate tables
