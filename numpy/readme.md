# NumPy Basics - Study Notes

## Key Concepts

1. **Array Creation:** Initializing data structures using `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, and `np.linspace()`.
2. **Array Properties:** Using `.shape` for dimensions, `.size` for total element count, and `.dtype` for data type.
3. **Indexing:** Accessing specific array elements. For 1D: `array[index]`. For 2D: `array[row, col]`.
4. **Slicing:** Extracting ranges of values using `start:stop:step` syntax, including negative indices to count from the end.
5. **Broadcasting:** Applying arithmetic operations (like adding or multiplying a scalar) across an entire array efficiently, or performing operations between arrays of compatible shapes.
6. **Boolean Indexing:** Filtering arrays using straightforward comparison operators (`>`, `<`, `==`).
7. **Aggregation:** Calculating core metrics across an entire array or specific axes using `.sum()`, `.mean()`, `.max()`, and `.min()`.
8. **Reshape Basics:** Changing an array's structural dimensions structurally (e.g., converting a 1D sequence into a 2D grid) using `.reshape(rows, cols)`.
9. **Matrix Operations:** Computing the dot product between vectors with `.dot()` or multiplying matrices natively using the `@` operator.

## Core Function Reference

| Function / Syntax | Purpose | Example |
| :--- | :--- | :--- |
| `np.array()` | Converts a standard Python list into a NumPy array. | `np.array([1, 2, 3])` |
| `np.zeros()`, `np.ones()` | Creates an array strictly filled with 0s or 1s. | `np.zeros((2, 3))` |
| `np.arange()` | Creates sequential numbers with a defined step size. | `np.arange(0, 10, 2)` |
| `np.linspace()` | Creates evenly spaced numbers across a specified interval. | `np.linspace(0, 10, 5)` |
| `array[row, col]` | Directly indexes a single element in a 2D array. | `matrix[1, 2]` |
| `array[start:stop]` | Slices a continuous sub-section of an array. | `arr[1:4]` |
| `array[array > x]` | Boolean filtering based on a conditional threshold. | `arr[arr > 10]` |
| `.reshape()` | Modifies the structural shape of the array explicitly. | `arr.reshape(3, 4)` |
| `.sum()`, `.mean()` | Computes numeric sums or averages. | `arr.mean()` |
| `.dot()`, `@` | Computes the dot product or performs matrix multiplication. | `A @ B` |
