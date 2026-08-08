import numpy as np

values = np.array([10, 25, 15, 40, 35, 5, 50])
high_values = values[values > 20]
print(high_values)

low_values = values[values < 30]
print(low_values)

raw_pixels = np.array([
    [100, 120, 150],
    [90, 110, 140],
    [80, 95, 130]])

threshold_mask = raw_pixels > 115
print(threshold_mask)

high_pixels = raw_pixels[raw_pixels > 100]
print(high_pixels)      