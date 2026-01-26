# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m
import parameters

from subsystem import *
from geometry import *
from instantiation import vesicles

SEED = parameters.SEED
OUTPUT_EVERY_N_TIMESTEPS = parameters.OUTPUT_EVERY_N_TIMESTEPS
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

vesicles_list = [
    "1_1", "1_2", "2_1", "2_2", "3_1", "3_2",
    "4_1", "4_2", "5_1", "5_2", "6_1", "6_2"
]
num_pulses = 4
# ============================================================
# BOUND SENSOR (Syt1 and Syt7)
# ============================================================

bound_sensor = {}      # maps (base, pulse) → species
bound_sensor_Y = {}    # maps (base, pulse) → species

# base = f"{az}_1_{ch}" exactly like old mdl grouping
for az in range(1, 7):
    for ch in range(1, 5):

        base = f"{az}_1_{ch}"

        for ap in range(1, num_pulses + 1):

            name_s1 = f"bound_sensor_{az}_1_{ch}_{ap}"
            name_s7 = f"bound_sensor_Y_{az}_1_{ch}_{ap}"

            # Store the species object
            if name_s1 in globals():
                bound_sensor[(base, ap)] = globals()[name_s1]

            if name_s7 in globals():
                bound_sensor_Y[(base, ap)] = globals()[name_s7]

# ---- observables ----
observables = m.Observables()

# =====================================================================
# ####     VISUALIZATION SPECIES LIST
# =====================================================================

viz_species = []

# ----------------------------------
# 1. Calcium channels (all states)
# ----------------------------------
for az in range(1, 7):
    for ch in range(1, 5):
        for state in [
            "closed_channel",
            "closed2_channel",
            "closed3_channel",
            "open1_channel",
            "open2_channel"
        ]:
            name = f"{state}_{az}_1_{ch}"
            if name in globals():
                viz_species.append(globals()[name])

# ----------------------------------
# 2. Calcium ions (all APs)
# ----------------------------------
for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):
            name = f"ca_{az}_1_{ch}_{ap}"
            if name in globals():
                viz_species.append(globals()[name])

# ----------------------------------
# 3. Sensors (unbound + bound Syt1 + bound Syt7)
# ----------------------------------
# Unbound species
for name in ["unbound_sensor", "unbound_sensor_Y"]:
    if name in globals():
        viz_species.append(globals()[name])

# Bound species (3D grid AZ 1–6, CH 1–4, AP 1–4)
for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):
            for prefix in ["bound_sensor", "bound_sensor_Y"]:
                name = f"{prefix}_{az}_1_{ch}_{ap}"
                if name in globals():
                    viz_species.append(globals()[name])
'''
# ----------------------------------
# 4. Fixed buffers
# ----------------------------------
viz_species.append(unbound_fixed_buffer)
for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):
            name = f"bound_fixed_buffer_{az}_1_{ch}_{ap}"
            if name in globals():
                viz_species.append(globals()[name])
'''
# ----------------------------------
# 5. SK Channels (all states)
# ----------------------------------
for az in range(1, 7):
    for ch in range(1, 5):
        for state in [
            "closed_SK",
            "closed2_SK",
            "closed3_SK",
            "closed4_SK",
            "open1_SK",
            "open2_SK"
        ]:
            name = f"{state}_{az}_1_{ch}"
            if name in globals():
                viz_species.append(globals()[name])

# =====================================================================
# FINAL VIZ OUTPUT
# =====================================================================

viz_output = m.VizOutput(
    mode = m.VizMode.ASCII,
    output_files_prefix = f'./viz_data/seed_{str(SEED).zfill(4)}/Scene',
    species_list = viz_species,
    every_n_timesteps = 10000
)

# =====================================================================
# =====================================================================
# =====================================================================
# 
# END OF VISUALIZATION
# 
# =====================================================================
# =====================================================================
# =====================================================================


'''
# ==========================================
# BOUND FIXED BUFFER COUNTS
# ==========================================

buffer_terms = []

for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):
            name = f"bound_fixed_buffer_{az}_1_{ch}_{ap}"
            species = globals().get(name)
            if species is None:
                print(f"WARNING: missing species {name}")
                continue

            term_name = f"cterm_{name}"
            globals()[term_name] = m.CountTerm(molecules_pattern=species.inst())
            buffer_terms.append(term_name)

# Construct expression EXACTLY like other blocks:
# "cterm_a + cterm_b + cterm_c + ..."
expr_string = " + ".join(buffer_terms)

# Evaluate into actual CountTerm expression
expression = eval(expr_string)

if expression is None:
    expression = m.CountTerm(molecules_pattern=unbound_fixed_buffer.inst())*0

count_buffer_bound = m.Count(
    name=f'buffer_bound.{str(SEED).zfill(4)}',
    expression=expression,
    file_name=f'./react_data/seed_{str(SEED).zfill(4)}/buffer_bound.{str(SEED).zfill(4)}.dat',
    every_n_timesteps = OUTPUT_EVERY_N_TIMESTEPS
)

observables.add_count(count_buffer_bound)
'''


# =====================================================================
# CALCIUM COUNTS 
# =====================================================================

# Convenience constant for output interval


# ---------------------------------------------------------------------
# 1. Individual Ca ions: ca_{az}_1_{ch}_{ap}
#    Total = 6 AZ × 4 CH × 4 AP = 96 count files
# ---------------------------------------------------------------------
for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):
            sp = globals()[f"ca_{az}_1_{ch}_{ap}"]
            ct = m.CountTerm(molecules_pattern=sp.inst())

            observables.add_count(
                m.Count(
                    name=f"ca_ions_{az}_1_{ch}_{ap}",
                    expression=ct,
                    file_name=f"./react_data/seed_{str(SEED).zfill(4)}/ca_ions_{az}_1_{ch}_{ap}.0001.dat",
                    every_n_timesteps=OUTPUT_EVERY_N_TIMESTEPS
                )
            )

# ---------------------------------------------------------------------
# 2. Summed calcium per AP (AP 1..4)
# ---------------------------------------------------------------------
for ap in range(1, 5):
    expr_sum_ap = None

    for az in range(1, 7):
        for ch in range(1, 5):
            sp = globals()[f"ca_{az}_1_{ch}_{ap}"]
            term = m.CountTerm(molecules_pattern=sp.inst())
            expr_sum_ap = term if expr_sum_ap is None else expr_sum_ap + term

    observables.add_count(
        m.Count(
            name=f"summed_ca_ions_{ap}",
            expression=expr_sum_ap,
            file_name=f"./react_data/seed_{str(SEED).zfill(4)}/summed_ca_ions_{ap}.0001.dat",
            every_n_timesteps=OUTPUT_EVERY_N_TIMESTEPS
        )
    )

# ---------------------------------------------------------------------
# 3. Global summed calcium (all AZ, all CH, all AP)
# ---------------------------------------------------------------------
expr_sum_all = None

for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):
            sp = globals()[f"ca_{az}_1_{ch}_{ap}"]
            term = m.CountTerm(molecules_pattern=sp.inst())
            expr_sum_all = term if expr_sum_all is None else expr_sum_all + term

observables.add_count(
    m.Count(
        name="summed_ca_ions",
        expression=expr_sum_all,
        file_name=f"./react_data/seed_{str(SEED).zfill(4)}/summed_ca_ions.0001.dat",
        every_n_timesteps=OUTPUT_EVERY_N_TIMESTEPS
    )
)

# =====================================================================
# VGCC OPEN STATES (open1, open2, total)
# =====================================================================
# =====================================================================
# PER-CHANNEL SUMMED VGCC OPEN STATES (open1 + open2)
# =====================================================================

for az in range(1, 7):
    for ch in range(1, 5):

        sp1 = globals().get(f"open1_channel_{az}_1_{ch}")
        sp2 = globals().get(f"open2_channel_{az}_1_{ch}")

        # Only proceed if both states exist
        if sp1 is not None and sp2 is not None:
            ct1 = m.CountTerm(molecules_pattern=sp1.inst())
            ct2 = m.CountTerm(molecules_pattern=sp2.inst())

            observables.add_count(
                m.Count(
                    name=f"open_channel_{az}_1_{ch}",
                    expression=ct1 + ct2,
                    file_name=f"./react_data/seed_{str(SEED).zfill(4)}/open_channel_{az}_1_{ch}.0001.dat",
                    every_n_timesteps=OUTPUT_EVERY_N_TIMESTEPS
                )
            )
# =====================================================================
# GLOBAL SUM OF ALL VGCC OPEN STATES (all AZ, all CH)
# =====================================================================

expr_open_global = None

for az in range(1, 7):
    for ch in range(1, 5):

        sp1 = globals().get(f"open1_channel_{az}_1_{ch}")
        if sp1 is not None:
            term1 = m.CountTerm(molecules_pattern=sp1.inst())
            expr_open_global = term1 if expr_open_global is None else expr_open_global + term1

        sp2 = globals().get(f"open2_channel_{az}_1_{ch}")
        if sp2 is not None:
            term2 = m.CountTerm(molecules_pattern=sp2.inst())
            expr_open_global = term2 if expr_open_global is None else expr_open_global + term2

observables.add_count(
    m.Count(
        name="summed_open_channels",
        expression=expr_open_global,
        file_name=f"./react_data/seed_{str(SEED).zfill(4)}/summed_open_channels.0001.dat",
        every_n_timesteps=OUTPUT_EVERY_N_TIMESTEPS
    )
)
# =====================================================================
# PER-CHANNEL SUMMED SK OPEN STATES (open1_SK + open2_SK)
# =====================================================================

for az in range(1, 7):
    for ch in range(1, 5):

        sp1 = globals().get(f"open1_SK_{az}_1_{ch}")
        sp2 = globals().get(f"open2_SK_{az}_1_{ch}")

        if sp1 is not None and sp2 is not None:
            ct1 = m.CountTerm(molecules_pattern=sp1.inst())
            ct2 = m.CountTerm(molecules_pattern=sp2.inst())

            observables.add_count(
                m.Count(
                    name=f"open_SK_{az}_1_{ch}",
                    expression=ct1 + ct2,
                    file_name=f"./react_data/seed_{str(SEED).zfill(4)}/open_SK_{az}_1_{ch}.0001.dat",
                    every_n_timesteps=OUTPUT_EVERY_N_TIMESTEPS
                )
            )

# =====================================================================
# GLOBAL SUM OF ALL SK OPEN STATES (all AZ, all CH)
# =====================================================================

expr_SK_global = None

for az in range(1, 7):
    for ch in range(1, 5):

        sp1 = globals().get(f"open1_SK_{az}_1_{ch}")
        if sp1 is not None:
            term1 = m.CountTerm(molecules_pattern=sp1.inst())
            expr_SK_global = term1 if expr_SK_global is None else expr_SK_global + term1

        sp2 = globals().get(f"open2_SK_{az}_1_{ch}")
        if sp2 is not None:
            term2 = m.CountTerm(molecules_pattern=sp2.inst())
            expr_SK_global = term2 if expr_SK_global is None else expr_SK_global + term2

observables.add_count(
    m.Count(
        name="summed_SK_channels",
        expression=expr_SK_global,
        file_name=f"./react_data/seed_{str(SEED).zfill(4)}/summed_SK_channels.0001.dat",
        every_n_timesteps=OUTPUT_EVERY_N_TIMESTEPS
    )
)


'''
# ======================================================================
# ALL-SITES SENSOR COUNTS (MDL: sites_all)
# ======================================================================
#
# ===============================
# Syt1 (sensor) – sites_all block
# ===============================
#

for v in vesicles_list:          # e.g. "1_1", "1_2", ..., "6_2"
    region_all = getattr(vesicles, f"sensor_{v}_sites_all")

    for az in range(1, 7):
        for ch in range(1, 5):
            for ap in range(1, 5):

                sp_name = f"bound_sensor_{az}_1_{ch}_{ap}"
                sp = globals()[sp_name]

                # Build CountTerm
                ct = m.CountTerm(
                    molecules_pattern = sp.inst(),
                    region = region_all
                )

                # Output name
                out_name  = f"vesicle_{v}_ca_{az}_1_{ch}_{ap}.0001"
                file_name = f"./react_data/seed_{str(SEED).zfill(4)}/{out_name}.dat"

                # Add count
                observables.add_count(
                    m.Count(
                        name = out_name,
                        expression = ct,
                        file_name = file_name,
                        every_n_timesteps = OUTPUT_EVERY_N_TIMESTEPS
                    )
                )



# =====================================================================
# SUMMED BOUND SENSORS (Syt1) PER VESICLE - SITE - PULSE
# =====================================================================

for v in vesicles_list:
    for site in range(0, 51):
        for pulse in range(1, num_pulses + 1):

            expr = None

            # Loop over all channels (az,ch)
            for az in range(1, 7):
                for ch in range(1, 5):

                    base = f"{az}_1_{ch}"
                    key = (base, pulse)

                    # Check if this bound sensor exists
                    if key in bound_sensor:

                        try:
                            # Vesicle-site-specific region
                            region = getattr(vesicles, f"sensor_{v}_site_{site}")

                            # Region-restricted count term
                            term = m.CountTerm(
                                molecules_pattern=bound_sensor[key].inst(),
                                region=region
                            )

                            # Sum the CountTerms
                            expr = term if expr is None else expr + term

                        except AttributeError:
                            # Region missing (can happen for unused or pruned sites)
                            continue

            # Add count if any channel contributed
            if expr is not None:
                observables.add_count(
                    m.Count(
                        name=f"bound_sensor_{v}_site_{site}_pulse_{pulse}",
                        expression=expr,
                        file_name=(
                            f"./react_data/seed_{str(SEED).zfill(4)}"
                            f"/bound_vesicle_{v}_sensor_{site}_{pulse}."
                            f"{str(SEED).zfill(4)}.dat"
                        ),
                        every_n_timesteps=OUTPUT_EVERY_N_TIMESTEPS
                    )
                )
            else:
                print(f"Missing region: sensor_{v}_site_{site}")

# =====================================================================
# SUMMED BOUND Y-SENSORS (Syt7) PER VESICLE - SITE - PULSE
# =====================================================================

for v in vesicles_list:
    for site in range(0, 35):   # Syt7 sites: 0–35
        for pulse in range(1, num_pulses + 1):

            expr = None

            # Loop over all channels (az,ch)
            for az in range(1, 7):
                for ch in range(1, 5):

                    base = f"{az}_1_{ch}"
                    key = (base, pulse)

                    if key in bound_sensor_Y:

                        try:
                            region = getattr(vesicles, f"sensor_Y_{v}_site_{site}")

                            term = m.CountTerm(
                                molecules_pattern=bound_sensor_Y[key].inst(),
                                region=region
                            )

                            expr = term if expr is None else expr + term

                        except AttributeError:
                            continue

            # Write file if at least one CountTerm was added
            if expr is not None:
                observables.add_count(
                    m.Count(
                        name=f"bound_vesicle_{v}_sensor_Y_{site}_{pulse}",
                        expression=expr,
                        file_name=(
                            f"./react_data/seed_{str(SEED).zfill(4)}"
                            f"/bound_vesicle_{v}_sensor_Y_{site}_{pulse}."
                            f"{str(SEED).zfill(4)}.dat"
                        ),
                        every_n_timesteps=OUTPUT_EVERY_N_TIMESTEPS
                    )
                )
            else:
                print(f"Missing region: sensor_Y_{v}_site_{site}")
'''

# ---- create observables object and add components ----

observables.add_viz_output(viz_output)
