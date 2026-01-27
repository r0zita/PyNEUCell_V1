# SynAPCell_V1

SynAPCell is a Python framework for coupling NEURON electrophysiology with MCell4 reaction–diffusion simulations to model nerve terminal function for the mouse neuromuscular junction (NMJ).

---
## What SynAPCell Simulates

SynAPCell simulates spike-driven calcium entry, diffusion, buffering, and
calcium-dependent channel and sensor kinetics at presynaptic active zones
of the mouse neuromuscular junction, using NEURON-derived action potentials
to dynamically control MCell4 reaction–diffusion processes.

---
## Overview

Here we use **physiologically realistic, dynamically changing action potentials** to control molecular simulations, enabling a tight coupling between membrane electrophysiology and stochastic chemical dynamics.

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
├── geometry/             # geometry files
└── NEURON_RATES/         # Precomputed NEURON-derived rate tables
```
## References

1. **Laghaei R**, **Meriney SD**.  
   *Microphysiological Modeling of the Structure and Function of Neuromuscular Transmitter Release Sites.*  
   **Frontiers in Synaptic Neuroscience**, 14:917285, 2022.  
   DOI: 10.3389/fnsyn.2022.917285

2. **Ginebaugh SP**, **Cyphers ED**, **Lanka V**, **Ortiz G**, **Miller EW**, **Laghaei R**, **Meriney SD**.  
   *The Frog Motor Nerve Terminal Has Very Brief Action Potentials and Three Electrical Regions Predicted to Differentially Control Transmitter Release.*  
   **Journal of Neuroscience**, 40(18):3504–3516, 2020.  
   DOI: 10.1523/JNEUROSCI.2415-19.2020

3. **Ginebaugh SP**, **Badawi Y**, **Laghaei R**, **Mersky G**, **Wallace CJ**, **Tarr TB**, **Kaufhold C**, **Reddel S**, **Meriney SD**.  
   *Simulations of active zone structure and function at mammalian NMJs predict that loss of calcium channels alone is not sufficient to replicate LEMS effects.*  
   **Journal of Neurophysiology**, 129(5):1259–1277, 2023.  
   DOI: 10.1152/jn.00404.2022

## Ion Channel Model

The presynaptic active zone is modeled using an explicit, state-based description of voltage-gated calcium channels (VGCCs) and calcium-activated potassium (SK) channels.

### Active Zone Organization

- **6 active zones**
- Each active zone contains:
  - **4 voltage-gated calcium channels (VGCCs)**
  - **4 SK channels**
  - **2 docked synaptic vesicles**

All channels are immobile and confined to the presynaptic membrane.

---
## Action Potential Protocol

The current implementation simulates **four presynaptic action potentials**.
Each action potential produces a distinct calcium species, allowing temporal
separation of calcium influx and downstream reactions across spikes.

Action-potential–dependent gating and calcium release rates are read from
precomputed NEURON tables stored in `NEURON_RATES/`.

---
### Voltage-Gated Calcium Channels (VGCCs)

Each VGCC is represented by a multi-state Markov model with the following membrane-bound states:

- `closed`
- `closed2`
- `closed3`
- `open1`
- `open2`

State transitions between closed and open states are governed by **time-dependent rate functions** derived from NEURON-simulated action potentials.

#### Gating Transitions

For each active zone and channel, the following transitions are defined:

- `closed ⇄ closed2`
- `closed2 ⇄ closed3`
- `closed3 ⇄ open1`
- `open1 ⇄ open2`

Transitions among closed states and the initial opening transition are controlled by **NEURON-derived variable rates**, while transitions between open states use fixed rate constants.

---

### Action Potential–Driven Calcium Release

Calcium entry occurs when a VGCC is in an open state (`open1` or `open2`).  
Each action potential waveform produces a **distinct calcium species**, allowing multiple spikes to be tracked independently.

For each channel and action potential index:

- `open → open + Ca²⁺`

Calcium release rates are **time-varying** and are read from precomputed NEURON rate tables stored in `NEURON_RATES/`.

This design allows realistic action potential waveforms—not square pulses—to directly control calcium influx.



## VGCC Kinetics and Calcium Influx Model

The VGCC gating and calcium influx model implemented in **SynAPCell** is based on the following study:

Dittrich M, Pattillo JM, King JD, Cho S, Stiles JR, Meriney SD.  
**An Excess-Calcium-Binding-Site Model Predicts Neurotransmitter Release at the Neuromuscular Junction.**  
*Biophysical Journal*, 104(12):2751–2763, 2013.  
DOI: https://doi.org/10.1016/j.bpj.2013.05.023

---

### Voltage-Dependent VGCC Gating Rates

VGCCs are modeled using a four-state kinetic scheme (three closed states and one open state), driven by a time-dependent membrane voltage waveform \( V_m(t) \).

The voltage-dependent transition rates are given by:

### Voltage-Dependent VGCC Gating Rates

alpha(Vm) = 0.06 * exp((Vm + 24) / 14.5)

beta(Vm) = 1.7 / (exp((Vm + 34) / 16.9) + 1)

where Vm(t) is the membrane potential (mV) corresponding to the presynaptic action potential waveform.

The time-dependent rate constants alpha(t) and beta(t) are precomputed and read by MCell at simulation startup.

---

### Calcium Influx Through Open VGCCs

k(t) = gamma * (G / (2 * e)) * (Vm(t) - E_Ca)

gamma = [Ca2+]_ext / (2 mM)


### VGCC Calcium Influx Parameters

- **G = 2.4 pS**  
  Single-channel conductance of the VGCC, measured in 2 mM external Ca²⁺  
  (from experimental recordings).

- **e** Elementary charge.

- **E_Ca = +60 mV**  
  Calcium reversal potential, defining the driving force  
  Vm(t) − E_Ca.

- **γ = [Ca²⁺]_ext / (2 mM)**  
  Scaling factor accounting for deviations from the 2 mM external Ca²⁺
  concentration used to measure VGCC conductance.

The time-dependent rate **k(t)** is precomputed from the membrane voltage
waveform and used to generate stochastic Ca²⁺ release events from open
VGCCs during the simulation.

---
## SK Channel Kinetics and Rate Constants

The calcium-dependent gating of SK (small-conductance Ca²⁺-activated K⁺) channels is modeled using a multi-state kinetic scheme derived from experimental measurements of recombinant SK channels.

The reaction scheme and rate constants are based on:

Hirschberg B, Maylie J, Adelman JP, Marrion NV.  
Gating of recombinant small-conductance Ca-activated K⁺ channels by calcium.  
*Journal of General Physiology*, 111(4):565–581, 1998.  
DOI: 10.1085/jgp.111.4.565


### SK (Small-Conductance Potassium) Channels

Each active zone also contains **4 SK channels**, positioned with a small lateral offset (5 nm) from the corresponding VGCCs. 

The maximum number of simultaneously open SK channel states in the model is fixed by geometry and channel stoichiometry:

- **6 active zones**
- **4 SK channels per active zone**
- **Maximum of 2 open states per SK channel**

This yields a hard upper bound of **48 SK open states** in the model. 
Any value exceeding this bound indicates an internal inconsistency and triggers a runtime error.

SK channels are modeled using a calcium-dependent gating scheme with the following states:

- `closed`
- `closed2`
- `closed3`
- `closed4`
- `open1`
- `open2`

#### Calcium-Dependent Gating

SK channel activation is driven by local calcium concentration:
- Forward transitions between closed states require calcium binding
- Reverse transitions release calcium back into the local pool
This allows SK channels to respond dynamically to calcium microdomains generated by nearby VGCCs.

#### Calcium-Independent Gating
Final transitions between closed and open states are calcium-independent and governed by fixed rate constants.

---

### Functional Coupling

Together, VGCCs and SK channels form a tightly coupled system in which:
- Action potentials control VGCC gating and calcium entry
- Local calcium activates SK channels
- SK channel opening provides feedback regulation of excitability

This channel model enables realistic simulation of spike-driven calcium dynamics and local feedback at the neuromuscular junction.

### Calcium-Dependent Transitions

Forward transitions between closed states are calcium-dependent and modeled as second-order reactions:

- `closed  + Ca²⁺ → closed2`
- `closed2 + Ca²⁺ → closed3`
- `closed3 + Ca²⁺ → closed4`

Reverse transitions release calcium back into the local pool:

- `closed2 → closed  + Ca²⁺`
- `closed3 → closed2 + Ca²⁺`
- `closed4 → closed3 + Ca²⁺`

---

### Rate Constants

Calcium-dependent forward rates:

- `k(c1 → c2) = 2.0 × 10⁸ M⁻¹ s⁻¹`
- `k(c2 → c3) = 1.6 × 10⁸ M⁻¹ s⁻¹`
- `k(c3 → c4) = 8.0 × 10⁷ M⁻¹ s⁻¹`

Calcium-independent reverse rates:

- `k(c2 → c1) = 80 s⁻¹`
- `k(c3 → c2) = 80 s⁻¹`
- `k(c4 → c3) = 200 s⁻¹`

---

### Calcium-Independent Gating Transitions

Final opening and closing transitions are calcium-independent:

- `closed3 ⇄ open1`
- `closed4 ⇄ open2`

With fixed rate constants:

- `k(c3 → o1) = 160 s⁻¹`
- `k(o1 → c3) = 1000 s⁻¹`
- `k(c4 → o2) = 1200 s⁻¹`
- `k(o2 → c4) = 100 s⁻¹`

---

## Customization

Simulation length, time step, and test runs can be modified via
`shared.parameter_overrides` without editing model files.

Dynamic model behavior (e.g., SK-dependent rate switching) is implemented
in `customization.py`.

## Endogenous Calcium Buffering (in subsystem.py)

Presynaptic calcium buffering is modeled using an immobile (fixed) buffer
to represent the effective buffering capacity of endogenous proteins and
structural binding sites near active zones.

Fixed Buffer Parameters (defined in subsystem.py)

### Buffer concentration:
    100 µM (1.0 × 10⁻⁴ M)

### Diffusion constant:
    0 (immobile buffer)

### Buffer Kinetics

Calcium binding and unbinding:

    Ca²⁺ + unbound_fixed_buffer ⇄ bound_fixed_buffer

with rate constants:

    k_on  = 1 × 10⁸ M⁻¹ s⁻¹   (diffusion-limited)
    k_off = 1 × 10³ s⁻¹

This yields an effective dissociation constant:

    K_d = k_off / k_on = 10 µM

### Rationale

These parameters were chosen to approximate physiologically realistic
presynaptic calcium buffering at the neuromuscular junction:

- Strong enough to restrict calcium microdomains near VGCCs
- Weak enough to allow rapid calcium signaling and SK channel activation
- Consistent with experimental and modeling estimates for presynaptic terminals

The fixed buffer primarily shapes:
- local calcium amplitude
- calcium decay kinetics
- coupling between VGCCs, SK channels, and calcium sensors

## Synaptotagmin Calcium Sensors (Syt1 and Syt7) (in subsystem.py)

The model includes two classes of presynaptic calcium sensors representing
synaptotagmin isoforms with distinct calcium affinities and kinetics.

### Sensor Species
- Syt1: fast, low-affinity calcium sensor
- Syt7: slow, high-affinity calcium sensor

Both sensors are immobile and localized to vesicle-associated membrane sites.

### Calcium Binding Reactions

Calcium binding is modeled using simple mass-action kinetics:

    Ca²⁺ + unbound_sensor   ⇄ bound_sensor     (Syt1)
    Ca²⁺ + unbound_sensor_Y ⇄ bound_sensor_Y   (Syt7)

### Rate Constants (defined in subsystem.py)

Syt1 (fast sensor):
    k_on  = 2.2 × 10⁷ M⁻¹ s⁻¹
    k_off = 9.1 × 10² s⁻¹

Syt7 (high-affinity sensor):
    k_on  = 1.0 × 10⁷ M⁻¹ s⁻¹
    k_off = 1.5 × 10¹ s⁻¹

### Functional Roles

- Syt1 responds rapidly to brief, high-amplitude calcium microdomains
- Syt7 integrates residual calcium across action potentials
- Together, Syt1 and Syt7 enable fast synchronous and slower facilitation-like
  components of neurotransmitter release

### References

- Chapman ER. Synaptotagmin: a Ca²⁺ sensor that triggers exocytosis?
  Nat Rev Mol Cell Biol. 2002;3:498–508.
- Südhof TC. The synaptic vesicle cycle.
  Annu Rev Neurosci. 2004;27:509–547.
- Jackman SL, Regehr WG. The mechanisms and functions of synaptic facilitation.
  Neuron. 2017;94:447–464.

## Running the Model and Output Files

### Running the Simulation

The model is executed from the top-level directory using:
    python model.py -seed [seed number]

The seed value controls the stochastic realization and determines the
output directory name.

### Output Structure

All reaction and count outputs are written to:

    react_data/
    └── seed_XXXX/

where XXXX is the zero-padded seed number used for the run.

This directory contains time-series files for:
- calcium ions (per AZ, channel, and action potential)
- summed calcium signals
- VGCC open states
- SK channel open states
- synaptotagmin binding states (if enabled, located in observables.py)

### Visualization outputs are written to:

    viz_data/seed_XXXX/

### File Descriptor Limit (Important)

Because the model generates a large number of output files, some systems
may exceed the default open-file limit.

If you encounter file descriptor errors, increase the limit before running:

    ulimit -n 10000

(or higher, depending on system limits)

### Visualization and Performance Notes

Spatial visualization output is written to:

    viz_data/seed_XXXX/

These files can be visualized using **CellBlender** (Blender + MCell plugin)
to inspect calcium diffusion, channel states, and sensor binding.

Disabling Visualization for Speed

Visualization can significantly increase I/O load and slow down simulations.
For faster runs, visualization output can be disabled by commenting out or
removing the VizOutput block in `observables.py`.

Disabling visualization is recommended for:
- long simulations
- parameter sweeps
- batch runs across many seeds

Notes

- Each run produces one set of outputs per seed.
- Output file names are consistent across seeds and differ by directory.
- Reducing the number of observables can significantly lower I/O load.
- Visualization is intended primarily for debugging and qualitative inspection.
- Quantitative analysis should rely on files in `react_data/`.

