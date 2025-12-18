import numpy as np
import pandas as pd

np.random.seed(42)
N = 1000

# -------------------------
# BASELINE DATA (Day 0)
# -------------------------
baseline = pd.DataFrame({
    "transaction_amount": np.random.normal(loc=2000, scale=500, size=N),
    "customer_age": np.random.normal(loc=35, scale=10, size=N),
    "transactions_per_day": np.random.poisson(lam=3, size=N)
})

baseline.to_csv("data/baseline.csv", index=False)

# -------------------------
# LIVE DATA — DAY 1
# Slight natural variation (almost healthy)
# -------------------------
live_day_1 = pd.DataFrame({
    "transaction_amount": np.random.normal(loc=2050, scale=520, size=N),
    "customer_age": np.random.normal(loc=36, scale=10, size=N),
    "transactions_per_day": np.random.poisson(lam=3, size=N)
})

live_day_1.to_csv("data/live_day_1.csv", index=False)

# -------------------------
# LIVE DATA — DAY 2
# GRADUAL DRIFT (mean slowly shifts)
# -------------------------
live_day_2 = pd.DataFrame({
    "transaction_amount": np.random.normal(loc=2300, scale=550, size=N),
    "customer_age": np.random.normal(loc=38, scale=11, size=N),
    "transactions_per_day": np.random.poisson(lam=4, size=N)
})

live_day_2.to_csv("data/live_day_2.csv", index=False)

# -------------------------
# LIVE DATA — DAY 3
# SUDDEN SHIFT (abrupt behavior change)
# -------------------------
live_day_3 = pd.DataFrame({
    "transaction_amount": np.random.normal(loc=3200, scale=700, size=N),
    "customer_age": np.random.normal(loc=45, scale=13, size=N),
    "transactions_per_day": np.random.poisson(lam=6, size=N)
})

live_day_3.to_csv("data/live_day_3.csv", index=False)

# -------------------------
# LIVE DATA — DAY 4
# NOISE INJECTION (random instability)
# -------------------------
noise = np.random.normal(0, 800, N)

live_day_4 = pd.DataFrame({
    "transaction_amount": np.random.normal(loc=3200, scale=700, size=N) + noise,
    "customer_age": np.random.normal(loc=45, scale=13, size=N),
    "transactions_per_day": np.random.poisson(lam=6, size=N)
})

live_day_4.to_csv("data/live_day_4.csv", index=False)

print("Baseline and live data (with drift) generated successfully")
