import pandas as pd

data = [
    ['2026-07-01', 'Sentinel-2', 45, 0.75, 22.1],
    ['2026-07-02', 'Landsat-8', 12, 0.82, 24.5],
    ['2026-07-03', 'Sentinel-2', 80, 0.45, 19.8],
    ['2026-07-04', 'GOES-16', 5, 0.91, 25.2],
    ['2026-07-05', 'Landsat-8', 95, 0.22, 18.5],
    ['2026-07-06', 'Sentinel-2', 30, 0.68, 23.1]
]

df = pd.DataFrame(data, columns=['Date', 'Satellite', 'CloudCoverage', 'NDVI', 'Temperature'])

clear_and_healthy = df[(df['CloudCoverage'] < 50) & (df['NDVI'] > 0.6)]
print(clear_and_healthy)

cloudy_or_cold = df[(df['CloudCoverage'] > 70) | (df['Temperature'] < 20)]
print(cloudy_or_cold)