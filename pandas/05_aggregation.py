import pandas as pd

data = [
    ['2026-07-01', 'Sentinel-2', 45, 22.1],
    ['2026-07-02', 'Landsat-8', 12, 24.5],
    ['2026-07-03', 'Sentinel-2', 80, 19.8],
    ['2026-07-04', 'GOES-16', 5, 25.2]
]

df = pd.DataFrame(data, columns=['Date', 'Satellite', 'CloudCoverage', 'Temperature'])
print(df['CloudCoverage'].sum())
print(df['CloudCoverage'].mean())
print(df['Temperature'].max())
print(df['Temperature'].min())