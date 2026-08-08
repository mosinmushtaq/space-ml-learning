import pandas as pd

data = [
    ['2026-07-01', 'Sentinel-2', 45],
    ['2026-07-02', 'Landsat-8', 12],
    ['2026-07-03', 'Sentinel-2', 80],
    ['2026-07-04', 'GOES-16', 5],
    ['2026-07-05', 'Landsat-8', 95],
    ['2026-07-06', 'Sentinel-2', 30]
]

df = pd.DataFrame(data, columns=['Date', 'Satellite', 'CloudCoverage'])

satellite_count = df.groupby('Satellite').size()
print(satellite_count)

avg_cloud = df.groupby('Satellite')['CloudCoverage'].mean()
print(avg_cloud)