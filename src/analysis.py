import pandas as pd

# -------------------------
# Load drift metrics
# -------------------------
drift_df = pd.read_csv("outputs/drift_results.csv")


# -------------------------
# Drift classification logic
# -------------------------
def classify_drift(psi, ks_pvalue):
    if psi > 0.25 and ks_pvalue < 0.05:
        return "High"
    elif psi > 0.1 and ks_pvalue < 0.05:
        return "Medium"
    else:
        return "Low"


def assign_alert(drift_level):
    if drift_level == "High":
        return "RED"
    elif drift_level == "Medium":
        return "YELLOW"
    else:
        return "GREEN"


# -------------------------
# Apply drift classification
# -------------------------
drift_df["drift_level"] = drift_df.apply(
    lambda row: classify_drift(row["psi"], row["ks_pvalue"]),
    axis=1
)

# -------------------------
# Create feature-wise summary
# -------------------------
feature_summary = drift_df[[
    "day",
    "feature",
    "psi",
    "ks_pvalue",
    "drift_level"
]]

feature_summary.to_csv(
    "outputs/feature_drift_summary.csv",
    index=False
)

print("Feature-wise drift scoring completed")
print(feature_summary)


# -------------------------
# Apply alert logic
# -------------------------
feature_summary["alert"] = feature_summary["drift_level"].apply(assign_alert)

alert_table = feature_summary[[
    "day",
    "feature",
    "psi",
    "ks_pvalue",
    "drift_level",
    "alert"
]]

alert_table.to_csv(
    "outputs/alert_table.csv",
    index=False
)

print("\nAlert system generated")
print(alert_table)
