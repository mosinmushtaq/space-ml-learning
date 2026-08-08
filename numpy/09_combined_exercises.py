import numpy as np

sensor_data = np.array([12.5, 45.2, 55.1, 62.3])
filtered = sensor_data[sensor_data > 40]
print(filtered.mean())

telemetry = np.arange(20).reshape(4, 5)
#telemetry = np.arange(20).reshape(4, 5) -- creates the array first and then reshapes it
print(telemetry.shape)
region = telemetry[1:3, 1:3]
print(region.sum(axis=1))

brightness = np.array([100, 150, 200, 180])
adjusted = brightness * 1.2
print(adjusted)