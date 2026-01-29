import numpy as np
import os
import AP3 as ap

neuron_runs = 25

def get_peak_times(t_vec, v_vec, threshold=0.0):
    """
    Extracts the times when the voltage crosses the threshold.
    Returns a list of peak times in seconds.
    """
    max_index = np.argmax(v_vec)     
    peak_v = v_vec[max_index]
    peak_t = t_vec[max_index]
    return peak_t, peak_v

def run_ap(value=0):
    t_vec, v_vec = ap.run_neuron(value)
    if (t_vec is None) or (v_vec is None):
        print("Error: AP run did not return valid data.")
        return
    print(f"AP run completed with {len(t_vec)} time points.")
    t, v = get_peak_times(t_vec, v_vec)
    #print(f"Peak voltage: {v} mV at time: {t} seconds")
    return t, v

with open("control_AP_voltage_cut", "r") as f:
    t_vec = []
    v_vec = []
    
    for line in f:
        if line.startswith("#"):
            continue  # Skip header lines
        t, v = map(float, line.split())
        t_vec.append(t)  # Convert to ms
        v_vec.append(v)
    
    peak_time, peak_voltage = get_peak_times(np.array(t_vec), np.array(v_vec))
    print(f"Peak voltage: {peak_voltage} mV at time: {peak_time} seconds")
    

with open("voltages.txt", "w") as f:
    f.write("# Time (s) Voltage (mV)\n")
    for i in range(neuron_runs):
        print(f"Running AP simulation {i + 1}/{neuron_runs} with value {i/(neuron_runs - 1) * 0.04}...")
        peak_time, peak_voltage = run_ap(i/(neuron_runs - 1) * 0.04)
        if peak_time is not None and peak_voltage is not None:
            print(f"Run {i + 1}: Peak voltage {peak_voltage} mV at time {peak_time} seconds")
            f.write(f"{peak_time} {peak_voltage}\n")  # Write to file
        else:
            print(f"Run {i + 1}: No valid peak detected.")
        print("-" * 40)