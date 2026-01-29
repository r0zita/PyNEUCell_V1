from neuron import h, gui
import neuron
neuron.h.load_file("nrngui.hoc")

import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
import subprocess

# Load standard run libraries (sets up v_init, tstop, etc.)
h.load_file("stdrun.hoc")

t_diff = .844


def run_neuron(value=0):
    # Create axon section
    axon = h.Section(name='axon')
    axon.nseg = 300  # Increased spatial resolution
    axon.diam = 2
    axon.L = 300

    # Biophysical properties
    axon.Ra = 70
    axon.cm = 1
    axon.insert('pas')
    axon.g_pas = 0.0044
    axon.e_pas = -60

    # Insert and configure ion channels
    axon.insert('GNa')
    axon.gnabar_GNa = 0.004
    axon.vthreshold_GNa = -50
    axon.ena = 50

    #BK potassium calcium binding channel
    axon.insert('aabBK')
    axon.ek = -77
    axon.gakbar_aabBK = value
    axon.gabkbar_aabBK = 0.04

    axon.insert('GK')
    axon.vthreshold_GK = -50
    axon.ek = -77
    #og value = .0035
    axon.gkbar_GK = 0.0025

    axon.insert('GCa')
    axon.vthreshold_GCa = -50
    axon.eca = 75
    #og value = .035
    axon.gcabar_GCa = 0.042

    # Stimulus
    stim = h.IClamp(axon(0.02))
    stim.delay = 0.5
    stim.dur = 1
    stim.amp = 0.4

    # Simulation settings
    h.v_init = -60
    h.dt = 0.002
    h.steps_per_ms = 500
    h.tstop = 3 + t_diff

    # Recording vectors
    v_vec = h.Vector().record(axon(0.5)._ref_v)
    t_vec = h.Vector().record(h._ref_t)

    # Run simulation
    h.finitialize(h.v_init)
    h.continuerun(h.tstop)

    # Save voltages to file
    with open(f"voltages/voltages_{np.round(value, 4)}.txt", "w") as f:
        for t, v in zip(t_vec, v_vec):
            #t /= 1000 # Convert to seconds
            if t >= t_diff:
                t -= t_diff
                #t = float(Decimal(str(t)) / Decimal('1000'))
                f.write(f"{t:.4f}\t{v:.4f}\n")

    filename = f"voltages/voltages_{np.round(value, 4)}.txt"
    #output_file = filename.replace(".txt", "_awk.txt")
    output_file = filename

    awk_command = f"awk '{{print $1/1000.0 \"\\t\" $2}}' {filename}"

    result = subprocess.run(awk_command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        with open(output_file, "w") as f_out:
            f_out.write(result.stdout)
        print(f"Processed {filename} -> {output_file}")
    else:
        print(f"AWK failed on {filename}: {result.stderr}")

    

    return t_vec, v_vec


def plot_voltage():
    # Load voltages from file
    t_vec = []
    v_vec = []
    with open("voltages.txt", "r") as f:
        for line in f:
            if line.startswith("#"):
                continue  # Skip header lines
            t, v = map(float, line.split())
            t_vec.append(t * 1000)  # Convert to ms
            v_vec.append(v)

    # Plotting
    plt.plot(t_vec, v_vec)
    plt.xlabel('Time (ms)')
    plt.ylabel('Voltage (mV)')
    plt.title('Membrane Potential at axon(0.5)')
    plt.savefig("ap_plot.png")  # Optional: save the plot
    plt.show()
    


