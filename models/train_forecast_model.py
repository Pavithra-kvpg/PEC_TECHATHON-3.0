import pandas as pd, pickle
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv("data/synthetic_hospital_data.csv", parse_dates=["ts"])
series = df[df.ward_id == 1].set_index("ts").oxygen_lpm.resample("1H").mean()

train = series[:-48]
model = ExponentialSmoothing(train, seasonal="add", seasonal_periods=24)
fit = model.fit()

with open("models/oxygen_model.pkl", "wb") as f:
    pickle.dump(fit, f)

print("✅ Model trained and saved to models/oxygen_model.pkl")
