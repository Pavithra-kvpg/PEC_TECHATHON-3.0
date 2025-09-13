import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start = datetime.now() - timedelta(days=30)
timestamps = pd.date_range(start=start, periods=30*24, freq="H")

data = []
for ward in range(1, 5):
    oxygen = np.random.normal(15, 3, len(timestamps))
    beds_total = 25
    beds_occupied = np.random.randint(10, 25, len(timestamps))
    staff_on_duty = np.random.randint(3, 6, len(timestamps))
    tank_percent = 100 - (oxygen.cumsum() * 0.01) % 100
    for i, ts in enumerate(timestamps):
        data.append([ts, ward, oxygen[i], tank_percent[i], beds_total, beds_occupied[i], staff_on_duty[i]])

df = pd.DataFrame(data, columns=[
    "ts", "ward_id", "oxygen_lpm", "tank_percent",
    "beds_total", "beds_occupied", "staff_on_duty"
])

df.to_csv("data/synthetic_hospital_data.csv", index=False)
print("✅ Synthetic data saved at data/synthetic_hospital_data.csv")
