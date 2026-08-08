# Pandas Core Concepts Reference

## 1. DataFrame and Series
*   **DataFrame**: A two-dimensional, size-mutable tabular dataset with labeled axes (rows and columns). Created from lists or dictionaries.
*   **Series**: A one-dimensional labeled array. Extracting a single column from a DataFrame returns a Series (`df['ColumnName']`). Extracting multiple columns returns a DataFrame (`df[['Col1', 'Col2']]`).

## 2. DataFrame Properties
*   `.shape`: Returns a tuple representing the dimensionality of the DataFrame (rows, columns).
*   `.columns`: Returns the column labels of the DataFrame.
*   `.dtypes`: Returns the data types of each column.

## 3. Accessing Data
*   **Entire Column**: `df['col_name']`
*   **Multiple Columns**: `df[['col1', 'col2']]`
*   **Specific Cell (Scalar)**: `df.loc[row_index, 'column_name']`
*   **Entire Row**: `df.loc[row_index]`

## 4. Boolean Filtering
Filter datasets by placing conditional statements inside the brackets.
*   **Single Condition**: `df[df['Column'] > Value]`
*   **Combined Conditions (AND)**: `df[(df['Col1'] == A) & (df['Col2'] < B)]`
*   **Combined Conditions (OR)**: `df[(df['Col1'] == A) | (df['Col2'] > B)]`

## 5. Aggregation Functions
Calculate summary statistics across numerical columns.
*   `.sum()`: Sum of values.
*   `.mean()`: Average of values.
*   `.max()`: Maximum value.
*   `.min()`: Minimum value.

## 6. Groupby Operations
The `.groupby()` method allows you to group data by categorical columns and apply aggregation functions to those specific groups.
*   **Single Column**: `df.groupby('CategoryColumn')['TargetColumn'].mean()`
*   **Multiple Aggregation Columns**: `df.groupby('CategoryColumn')[['Target1', 'Target2']].max()`
