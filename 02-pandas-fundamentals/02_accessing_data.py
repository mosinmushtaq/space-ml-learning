import pandas as pd

data = {
    'Date': ['2026-07-01', '2026-07-02', '2026-07-03'],
    'Satellite': ['Sentinel-2', 'Landsat-8', 'Sentinel-2'],
    'Temperature': [22.1, 24.5, 19.8]
}

observations = pd.DataFrame(data)
print(observations)

print("\n--- Accessing single column (Series) ---")
print(observations['Temperature'])
print(type(observations['Temperature']))

print("\n--- Accessing multiple columns (DataFrame) ---")
print(observations[['Date', 'Temperature']])
print(type(observations[['Date', 'Temperature']]))

print("\n--- Accessing single cell (scalar) ---")
print(observations.loc[2, 'Temperature'])

print("\n--- Accessing entire row (Series) ---")
print(observations.loc[2])

print("\n--- Accessing rows by range ---")
print(observations.loc[0:1])