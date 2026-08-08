import pandas as pd

data = [
    ['2026-07-01', 'Sentinel-2', 20, 0.75],
    ['2026-07-02', 'Landsat-8', 90, 0.30],
    ['2026-07-03', 'Sentinel-2', 15, 0.82],
    ['2026-07-04', 'GOES-16', 5, 0.91],
    ['2026-07-05', 'Landsat-8', 10, 0.85],
    ['2026-07-06', 'Sentinel-2', 40, 0.68]
]

df = pd.DataFrame(data, columns=['Date', 'Satellite', 'CloudCoverage', 'NDVI'])

clear_data = df[df['CloudCoverage'] < 50]
print("Clear observations:")
print(clear_data)

healthy_clear = df[(df['CloudCoverage'] < 50) & (df['NDVI'] > 0.7)]
print("\nClear AND healthy vegetation:")
print(healthy_clear)

group_stats = df.groupby('Satellite')['NDVI'].mean()
print("\nAverage NDVI per satellite:")
print(group_stats)