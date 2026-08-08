import numpy as np

raw_pixels = np.array([
    [100, 120, 150],
    [90, 110, 140],
    [80, 95, 130]])

adjusted_pixels = raw_pixels + 25
print(adjusted_pixels)

normalized_pixels = raw_pixels / 255.0
print(normalized_pixels)

background_noise = np.array([5, 10, 15])
clean_signal = raw_pixels - background_noise
print(clean_signal)



2. Subtracting background_noise (Broadcasting)Yes, it subtracts the 1D array from all 3 rows.
This is the core concept of broadcasting. Because your 3x3 raw_pixels matrix has 3 columns, and your 1D background_noise array has 3 elements, NumPy automatically "stretches" the 1D array downwards. It subtracts 5 from column 0, 10 from column 1, and 15 from column 2, repeating this for every single row.  What if you subtract a 2x2 matrix from a 3x3 matrix?The code will crash and throw a ValueError. Broadcasting only works if the dimensions are mathematically compatible. For two arrays to be compatible, their dimensions must either be exactly equal, or one of the dimensions must be exactly 1. Since a 3x3 and a 2x2 do not match and neither has a dimension of 1, NumPy cannot align them to do the math.