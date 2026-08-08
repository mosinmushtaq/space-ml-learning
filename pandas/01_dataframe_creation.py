import pandas as pd

data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 92, 78]
}

df = pd.DataFrame(data_dict)
print(df)
print(df.columns)
print(df.dtypes)
print(df.shape)

data_list = [
    ['2026-07-01', 'Sentinel-2', 45, 22.1],
    ['2026-07-02', 'Landsat-8', 12, 24.5],
    ['2026-07-03', 'Sentinel-2', 80, 19.8]
]

observations = pd.DataFrame(data_list, columns=['Date', 'Satellite', 'CloudCoverage', 'Temperature'])
print(observations)
print(observations.shape)
print(observations.columns)