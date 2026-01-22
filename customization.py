# This file contains hooks to override default MCell4 model
# code behavior for models generated from CellBlender
# WARNING: do not import file parameters.py at the top level of this file,
# only from individual functions if needed, parameters such as SEED
# will not be set correctly if parameters are imported too early
import sys
import os
import shared
import mcell as m
import time

"""
def custom_argparse_and_parameters():
    # When uncommented, this function is called to parse 
    # custom commandline arguments.
    # It is executed before any of the automatically generated 
    # parameter values are set so one can override the parameter 
    # values here as well.
    # To override parameter values, add or overwrite an item in dictionary
    # shared.parameter_overrides, e.g. shared.parameter_overrides['SEED'] = 10
    pass
"""

"""
def custom_config(model):
    # When uncommented, this function is called to set custom
    # model configuration.
    # It is executed after basic parameter setup is done and 
    # before any components are added to the model. 
    pass
"""

"""
def custom_init_and_run(model):
    # When uncommented, this function is called after all the model
    # components defined in CellBlender were added to the model.
    # It allows to add additional model components before initialization 
    # is done and then to customize how simulation is ran.
    # The module parameters must be imported locally otherwise
    # changes to shared.parameter_overrides done elsewhere won't be applied.
    import parameters as parameters
    model.initialize()
    model.run_iterations(parameters.ITERATIONS)
    model.end_simulation()
"""
def custom_init_and_run(model):
    import parameters
    import os, time

    model.initialize()

    seed_str = str(parameters.SEED).zfill(4)
    sk_file = f"./react_data/seed_{seed_str}/summed_SK_channels.0001.dat"

    print("[INIT] custom run active")
    print(f"[INIT] Expecting SK file at: {sk_file}")
    print(f"[INIT] TIME_STEP = {parameters.TIME_STEP}")

    for step in range(parameters.ITERATIONS):

        model.run_iterations(1)

        if step % 2000 != 0:
            continue

        if not os.path.exists(sk_file):
            print(f"[WARN] step={step}, SK FILE NOT FOUND")
            continue

        with open(sk_file) as f:
            lines = f.readlines()

        if not lines:
            SK = 0.0
        else:
            _, last_sk = lines[-1].split()
            SK = float(last_sk)

        # ---------------------------
        # SK → BIN
        # ---------------------------
        if SK <= 1:
            SK_bin = 0
        else:
            SK_bin = (int(SK) // 2) * 2

        # ---------------------------
        # SWITCH GATING RATE TABLES
        # ---------------------------
        parameters.ac1c2 = parameters.ac1c2_tables[SK_bin]
        parameters.bc2c1 = parameters.bc2c1_tables[SK_bin]
        parameters.ac2c3 = parameters.ac2c3_tables[SK_bin]
        parameters.bc3c2 = parameters.bc3c2_tables[SK_bin]
        parameters.ac3o1 = parameters.ac3o1_tables[SK_bin]
        parameters.bo1c3 = parameters.bo1c3_tables[SK_bin]

        # ---------------------------
        # SWITCH K3 (Ca RELEASE) TABLES
        # ---------------------------
        parameters.k3_control_short_1 = parameters.k3_control_short_1_tables[SK_bin]
        parameters.k3_control_short_2 = parameters.k3_control_short_2_tables[SK_bin]
        parameters.k3_control_short_3 = parameters.k3_control_short_3_tables[SK_bin]
        parameters.k3_control_short_4 = parameters.k3_control_short_4_tables[SK_bin]

        # ---------------------------
        # DEBUG
        # ---------------------------
        import bisect

        sim_t = step * parameters.TIME_STEP

        def rate_at_time(table, t):
            times = [row[0] for row in table]
            idx = bisect.bisect_right(times, t) - 1
            if idx < 0:
                idx = 0
            return idx, table[idx]

        i1, r1 = rate_at_time(parameters.ac1c2, sim_t)
        i2, r2 = rate_at_time(parameters.bc2c1, sim_t)
        i3, r3 = rate_at_time(parameters.ac2c3, sim_t)
        i4, r4 = rate_at_time(parameters.bc3c2, sim_t)
        i5, r5 = rate_at_time(parameters.ac3o1, sim_t)
        i6, r6 = rate_at_time(parameters.bo1c3, sim_t)

        #print(
        #    f"[UPDATE] step={step} sim_t={sim_t:.6f} SK={SK:.2f} bin={SK_bin} | "
        #    f"ac1c2 idx={i1} rate={r1[1]:.4f} | "
        #    f"bc2c1 idx={i2} rate={r2[1]:.4f} | "
        #    f"ac2c3 idx={i3} rate={r3[1]:.4f}"
        #)

        time.sleep(0.0002)

        time.sleep(0.0002)

    #print("[END] Simulation done")
    model.end_simulation()


