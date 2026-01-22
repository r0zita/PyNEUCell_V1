# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import sys
import os
import math
import shared
import mcell as m

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


def load_table(fname):
    tbl = []
    full = os.path.join(MODEL_PATH, "NEURON_RATES", fname)
    with open(full) as f:
        for line in f:
            if line.strip():
                t, v = line.split()
                tbl.append([float(t), float(v)])
    return tbl


# =========================================================
# SK BINS
# =========================================================

SK_BINS = list(range(0, 50, 2))   # SK0 .. SK48


# =========================================================
# LOAD RATE TABLES (ORIGINAL NAMES)
# =========================================================

def load_rate_tables(rate):
    return {sk: load_table(f"{rate}_SK{sk}.txt") for sk in SK_BINS}


ac1c2_tables = load_rate_tables("ac1c2")
bc2c1_tables = load_rate_tables("bc2c1")
ac2c3_tables = load_rate_tables("ac2c3")
bc3c2_tables = load_rate_tables("bc3c2")
ac3o1_tables = load_rate_tables("ac3o1")
bo1c3_tables = load_rate_tables("bo1c3")


# ===============================
# K3 (Ca RELEASE) TABLES
# filenames: k3_control_short_{ap}_SK{sk}.txt
# ===============================

def load_k3_tables(ap):
    return {
        sk: load_table(f"k3_control_short_{ap}_SK{sk}.txt")
        for sk in SK_BINS
    }


k3_control_short_1_tables = load_k3_tables(1)
k3_control_short_2_tables = load_k3_tables(2)
k3_control_short_3_tables = load_k3_tables(3)
k3_control_short_4_tables = load_k3_tables(4)


""" 
# ===============================
# SANITY PRINT: K3 FIRST ROW
# ===============================

for sk in SK_BINS:
    print(
        f"[K3 FIRST] SK{sk} | "
        f"AP1:{k3_control_short_1_tables[sk][0]} "
        f"AP2:{k3_control_short_2_tables[sk][0]} "
        f"AP3:{k3_control_short_3_tables[sk][0]} "
        f"AP4:{k3_control_short_4_tables[sk][0]}"
    )

# =========================================================
# SANITY PRINT (CONFIRM LOAD)
# =========================================================

for sk in SK_BINS:
    print(
        f"[FIRST] SK{sk} | "
        f"ac1c2:{ac1c2_tables[sk][0]} "
        f"bc2c1:{bc2c1_tables[sk][0]} "
        f"ac2c3:{ac2c3_tables[sk][0]} "
        f"bc3c2:{bc3c2_tables[sk][0]} "
        f"ac3o1:{ac3o1_tables[sk][0]} "
        f"bo1c3:{bo1c3_tables[sk][0]}"
    )
 """

# =========================================================
# INITIAL VARIABLE RATE TABLES (USED BY SUBSYSTEM)
# =========================================================

ac1c2 = ac1c2_tables[0]
bc2c1 = bc2c1_tables[0]
ac2c3 = ac2c3_tables[0]
bc3c2 = bc3c2_tables[0]
ac3o1 = ac3o1_tables[0]
bo1c3 = bo1c3_tables[0]

k3_control_short_1 = k3_control_short_1_tables[0]
k3_control_short_2 = k3_control_short_2_tables[0]
k3_control_short_3 = k3_control_short_3_tables[0]
k3_control_short_4 = k3_control_short_4_tables[0]


# =========================================================
# INITIAL SCALAR VALUES (FOR DEBUG / OPTIONAL USE)
# =========================================================

ac1c2_scalar = ac1c2_tables[0][0][1]
bc2c1_scalar = bc2c1_tables[0][0][1]
ac2c3_scalar = ac2c3_tables[0][0][1]
bc3c2_scalar = bc3c2_tables[0][0][1]
ac3o1_scalar = ac3o1_tables[0][0][1]
bo1c3_scalar = bo1c3_tables[0][0][1]


# =========================================================
# STANDARD MCELL PARAMETERS
# =========================================================

# declare all items from parameter_overrides as variables
for parameter_name, value in shared.parameter_overrides.items():
    setattr(sys.modules[__name__], parameter_name, value)

def not_defined(name):
    return name not in globals()

if not_defined("ITERATIONS"):
    ITERATIONS = 6300000

if not_defined("TIME_STEP"):
    TIME_STEP = 1e-08

if not_defined("DUMP"):
    DUMP = False

OUTPUT_EVERY_N_TIMESTEPS = 5.0e-07 / TIME_STEP
VIZ_EVERY_N_TIMESTEPS = 10000

if not_defined("EXPORT_DATA_MODEL"):
    EXPORT_DATA_MODEL = True

if not_defined("SEED"):
    SEED = 1
elif len(sys.argv) == 3 and sys.argv[1] == "-seed":
    shared.parameter_overrides["SEED"] = int(sys.argv[2])


# ---- model parameters ----

# declare all items from parameter_overrides as variables
for parameter_name, value in shared.parameter_overrides.items():
    setattr(sys.modules[__name__], parameter_name, value)

# auxiliary function used to determine whether a parameter was defined
def not_defined(parameter_name):
    return parameter_name not in globals()


# ---- simulation setup ----

if not_defined('ITERATIONS'):
    ITERATIONS = 6300000

if not_defined('TIME_STEP'):
    TIME_STEP = 1e-08

if not_defined('DUMP'):
    DUMP = False
# Output sampling interval (in timesteps)
OUTPUT_EVERY_N_TIMESTEPS = 5.0e-07 / 1e-08    # equals 50
# Output sampling interval for visualization (in timesteps)
VIZ_EVERY_N_TIMESTEPS = 10000

if not_defined('EXPORT_DATA_MODEL'):
    EXPORT_DATA_MODEL = True

if not_defined('SEED'):
    SEED = 1
elif len(sys.argv) == 3 and sys.argv[1] == '-seed':
    shared.parameter_overrides['SEED'] = int(sys.argv[2])



