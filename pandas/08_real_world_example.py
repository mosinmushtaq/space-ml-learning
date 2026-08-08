import pandas as pd

data = [
    ['2026-07-01', 'Sentinel-2', 15, 0.82, 24.5],
    ['2026-07-02', 'Landsat-8', 95, 0.22, 18.5],
    ['2026-07-03', 'Sentinel-2', 12, 0.85, 23.8],
    ['2026-07-04', 'GOES-16', 50, 0.65, 25.0],
    ['2026-07-05', 'Landsat-8', 30, 0.75, 22.0]
]

df = pd.DataFrame(data, columns=['Date', 'Satellite', 'CloudCoverage', 'NDVI', 'Temperature'])
print("Full dataset:")
print(df)

print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())

print("\nClear observations (CloudCoverage < 50):")
clear = df[df['CloudCoverage'] < 50]
print(clear)

print("\nAverage stats per satellite:")
avg_by_satellite = df.groupby('Satellite')[['CloudCoverage', 'NDVI']].mean()
print(avg_by_satellite)

print("\nHigh NDVI observations:")
high_ndvi = df[df['NDVI'] > 0.7]
print(high_ndvi)