#!/usr/bin/env python3
import sys
import numpy as np
import glob
import os


# =========================
# USER INPUT
# =========================
if len(sys.argv) != 3:
    print("Usage: python make_AP_rates.py <interval_sec> <num_pulses>")
    sys.exit(1)

interval = float(sys.argv[1])
num_of_pulses = int(sys.argv[2])

if interval < 0.003:
    raise ValueError("Interval cannot be shorter than 0.003 s")

parameter_change_time_step = 0.00002000

# =========================
# CONSTANTS (do not change)
# =========================
ac1c2 = 7.0
bc2c1 = 1.0
ac2c3 = 6.0
bc3c2 = 2.0
ac3o1 = 5.0
bo1c3 = 3.0

def make_rate_files(run, value):

    ##########k3_multiplier = 2.0

    # =========================
    # STEP 1: READ AP
    # =========================
    AP_file = value
    AP = np.loadtxt(AP_file)
    t = AP[:, 0]
    V = AP[:, 1]

    # =========================
    # STEP 2: COMPUTE BASE RATES (awk replacement)
    # =========================
    alpha = 1000 * 0.06 * np.exp((V + 24.0) / 14.5)
    beta  = 1000 * 1.7 / (np.exp((V + 34.0) / 16.9) + 1.0)
    k3    = (2.0 / 2.0) * (2.4e-12) * (-1.0) * (V - 60.0) * 1e-3 / (2 * 1.60217646e-19)

    np.savetxt("alpha_template_SK{}.txt", np.c_[t, alpha], fmt="%.8f %.6f")
    np.savetxt("beta_template.txt",  np.c_[t, beta],  fmt="%.8f %.6f")
    np.savetxt("k3_template.txt",    np.c_[t, k3],    fmt="%.8f %.6e")

    # =========================
    # STEP 3: SCALE TEMPLATES
    # =========================
    np.savetxt("ac1c2_template.txt", np.c_[t, alpha * ac1c2], fmt="%.8f %.6f")
    np.savetxt("bc2c1_template.txt", np.c_[t, beta  * bc2c1], fmt="%.8f %.6f")
    np.savetxt("ac2c3_template.txt", np.c_[t, alpha * ac2c3], fmt="%.8f %.6f")
    np.savetxt("bc3c2_template.txt", np.c_[t, beta  * bc3c2], fmt="%.8f %.6f")
    np.savetxt("ac3o1_template.txt", np.c_[t, alpha * ac3o1], fmt="%.8f %.6f")
    np.savetxt("bo1c3_template.txt", np.c_[t, beta  * bo1c3], fmt="%.8f %.6f")

    np.savetxt(
        "k3_control_short_template.txt",
        np.c_[t, k3],
        fmt="%.8f %.6e"
    )

    # =========================
    # STEP 4: PULSE EXPANSION FUNCTIONS
    # =========================
    def Make_New_Parameter_File_1(template_name, interval):
        data = np.loadtxt(template_name)
        t0 = data[:, 0]
        y0 = data[:, 1]

        first_value = y0[0]
        last_value  = y0[-1]

        output_name = template_name.replace("_template.txt", f"_SK{run}.txt")
        f_out = open(output_name, "w")

        for i in range(len(t0)):
            f_out.write(f"{t0[i]:.8f}  {y0[i]}\n")

        mid_interval_steps = int((interval - 0.003) / parameter_change_time_step)

        for p in range(1, num_of_pulses):
            for i in range(1, mid_interval_steps):
                tnew = 0.003 + (p - 1) * interval + i * parameter_change_time_step
                ynew = last_value - (last_value - first_value) / mid_interval_steps * i
                f_out.write(f"{tnew:.8f}  {ynew}\n")

            for i in range(len(t0)):
                f_out.write(f"{t0[i] + interval + (p - 1) * interval:.8f}  {y0[i]}\n")

        f_out.close()


    def Make_New_Parameter_File_2(template_name, interval):
        data = np.loadtxt(template_name)
        y = data[:, 1]

        total_t = interval * (num_of_pulses - 1) + 0.003
        base_t = np.arange(0, total_t + parameter_change_time_step, parameter_change_time_step)

        for p in range(1, num_of_pulses + 1):
            output_name = template_name.replace("_template.txt", f"_{p}_SK{run}.txt")
            f_out = open(output_name, "w")

            start_t = interval * (p - 1)
            end_t = start_t + 0.003
            idx = 0

            for tnow in base_t:
                if start_t <= tnow <= end_t and idx < len(y):
                    f_out.write(f"{tnow:.8f}    {y[idx]}\n")
                    idx += 1
                else:
                    f_out.write(f"{tnow:.8f}    0\n")

            f_out.close()

    # =========================
    # STEP 5: GENERATE FINAL FILES
    # =========================
    for name in [
        "ac1c2_template.txt",
        "bc2c1_template.txt",
        "ac2c3_template.txt",
        "bc3c2_template.txt",
        "ac3o1_template.txt",
        "bo1c3_template.txt",
    ]:
        Make_New_Parameter_File_1(name, interval)

    Make_New_Parameter_File_2("k3_control_short_template.txt", interval)

    print(f"DONE: Generated rate files for {num_of_pulses} pulses at {interval} s interval.")



def load_voltage_files(pattern="voltages_*.txt"):
    # Sort to ensure files go from voltage_0 to voltage_24
    file_list = sorted(glob.glob(pattern))
    all_data = []
    for f in file_list:
        with open(f) as fin:
            lines = [line.strip().split() for line in fin if line.strip()]
            times_volts = [(float(t), float(v)) for t, v in lines]
            all_data.append(times_volts)
    return all_data  # list of 25 lists of (t, v)

def load_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as f:
        lines = [line.strip().split() for line in f if line.strip()]
        return [(float(t), float(v)) for t, v in lines]  # list of (t, v) tuples

neuron_runs = 25
for i in range(neuron_runs):
    v = i/(neuron_runs - 1) * 0.04
    run = i * 2
    #voltage_data = load_file(f"voltages/voltages_{np.round(v, 4)}.txt")
    value = f"voltages/voltages_{np.round(v, 4)}.txt"
    make_rate_files(run, value)
    
print("DONE: All AP-based rate files generated.")

