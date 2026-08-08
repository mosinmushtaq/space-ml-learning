import pandas as pd

data = [
    ['2026-07-01', 'Sentinel-2', 45, 0.75, 22.1],
    ['2026-07-02', 'Landsat-8', 12, 0.82, 24.5],
    ['2026-07-03', 'Sentinel-2', 80, 0.45, 19.8],
    ['2026-07-04', 'GOES-16', 5, 0.91, 25.2],
    ['2026-07-05', 'Landsat-8', 95, 0.22, 18.5],
    ['2026-07-06', 'Sentinel-2', 30, 0.68, 23.1],
    ['2026-07-07', 'Landsat-8', 15, 0.85, 26.0],
    ['2026-07-08', 'GOES-16', 10, 0.88, 24.1]
]

satellite_data = pd.DataFrame(data, columns=['Date', 'Satellite', 'CloudCoverage', 'NDVI', 'Temperature'])

multi_stats = satellite_data.groupby('Satellite')[['NDVI', 'Temperature']].mean()
print(multi_stats)

cloud_stats = satellite_data.groupby('Satellite')[['CloudCoverage', 'NDVI']].max()
print(cloud_stats)