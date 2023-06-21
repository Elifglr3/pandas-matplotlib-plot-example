import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Inductor (mH)": [0.1, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10],
    "Voltage (mV)": [13.3, 65, 132.5, 194, 267, 322, 388, 459, 523, 572, 652, 712, 782, 855, 920, 971, 1032, 1056, 1132, 1215, 1273]
})

plt.plot(df["Inductor (mH)"], df["Voltage (mV)"], label="Voltage vs. Inductor")

plt.xlabel("Inductor (mH)")
plt.ylabel("Voltage (mV)")

plt.title("Voltage vs. Inductor")

plt.show()
plt.savefig("voltage_vs_inductor.png")
