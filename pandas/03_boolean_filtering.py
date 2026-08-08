import pandas as pd

data = [
    ['2026-07-01', 'Sentinel-2', 45, 22.1],
    ['2026-07-02', 'Landsat-8', 12, 24.5],
    ['2026-07-03', 'Sentinel-2', 80, 19.8],
    ['2026-07-04', 'GOES-16', 5, 25.2],
    ['2026-07-05', 'Landsat-8', 95, 18.5]
]

df = pd.DataFrame(data, columns=['Date', 'Satellite', 'CloudCoverage', 'Temperature'])

clear_observations = df[df['CloudCoverage'] < 30]
print(clear_observations)

high_temp = df[df['Temperature'] > 23]
print(high_temp)