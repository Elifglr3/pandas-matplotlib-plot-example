import pandas as pd
import matplotlib.pyplot as plt
import warnings
from matplotlib import MatplotlibDeprecationWarning
warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)

df = pd.DataFrame({
    "Capacitor (nF)": [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    "Voltage (mV)": [11.6, 57.5, 116.5, 169, 233.5, 285.6, 327, 417.3, 473, 507, 566, 650, 683, 765, 830, 898, 921, 963, 1001, 1060, 1140]
})

plt.plot(df["Capacitor (nF)"], df["Voltage (mV)"], label="Voltage vs. Capacitor")

plt.xlabel("Capacitor (nF)")
plt.ylabel("Voltage (mV)")

plt.title("Voltage vs. Capacitor")
plt.show()
plt.savefig("voltage_vs_capacitor.png")
