import numpy as np
import pandas as pd
from scipy.stats import ks_2samp

# -------------------------
# PSI Calculation
# -------------------------
def calculate_psi(expected, actual, bins=10):
    expected = np.array(expected)
    actual = np.array(actual)

    breakpoints = np.linspace(0, 100, bins + 1)
    expected_perc = np.percentile(expected, breakpoints)
    actual_perc = np.percentile(actual, breakpoints)

    psi = 0
    for i in range(len(expected_perc) - 1):
        expected_pct = np.mean((expected >= expected_perc[i]) &
                                (expected < expected_perc[i + 1]))
        actual_pct = np.mean((actual >= actual_perc[i]) &
                              (actual < actual_perc[i + 1]))

        if expected_pct == 0 or actual_pct == 0:
            continue

        psi += (actual_pct - expected_pct) * np.log(actual_pct / expected_pct)

    return psi

# Load baseline
baseline = pd.read_csv("data/baseline.csv")

# Live datasets
live_files = {
    "day_1": pd.read_csv("data/live_day_1.csv"),
    "day_2": pd.read_csv("data/live_day_2.csv"),
    "day_3": pd.read_csv("data/live_day_3.csv"),
    "day_4": pd.read_csv("data/live_day_4.csv"),
}

features = baseline.columns
results = []

for day, live_data in live_files.items():
    for feature in features:
        psi_score = calculate_psi(
            baseline[feature],
            live_data[feature]
        )

        ks_stat, ks_pvalue = ks_2samp(
            baseline[feature],
            live_data[feature]
        )

        results.append({
            "day": day,
            "feature": feature,
            "psi": round(psi_score, 3),
            "ks_pvalue": round(ks_pvalue, 5)
        })

drift_results = pd.DataFrame(results)
drift_results.to_csv("outputs/drift_results.csv", index=False)

print("Drift detection completed")
print(drift_results)
