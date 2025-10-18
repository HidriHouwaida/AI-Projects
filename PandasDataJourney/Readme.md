# Pandas Data Journey 
##  📊 Library Overview
Pandas is a fundamental Python library providing high-performance, easy-to-use data structures and data analysis tools, essential for data science and machine learning workflows.
## 🚀 Quick Start
### Installation
```python
pip install pandas
```
### Import
```python
import pandas as pd
```

## 💻 Basic Usage Examples
### Creating DataFrames
```python
df = pd.DataFrame() # Empty DataFrame
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Basic Matrix
df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    columns=["A", "B", "C"],
    index=["X", "Y", "Z"], copy=False
) # With Custom Columns and Index and Preventing Data Copy
```
Key Parameters
* data: Input data (list, dictionary, array, etc.)

* columns: Column labels

* index: Row labels

* copy: Whether to copy input data (default: False)

### Essential Operations
```python
df.head()       # First 5 rows
df.tail()       # Last 5 rows  
df.info()       # Dataset information
df.describe()   # Statistical summary
df.shape        # Dimensions (rows, columns)
```
## Loading Data from Files
```python
coffee = pd.read_csv('coffee.csv') # CSV Files
result = pd.read_parquet('results.parquet') # Parquet Files
olympics = pd.read_excel('olympics.xlsx')
```
### Parquet 
Parquet is the most performant format for data scientists because its columnar storage architecture enables handling huge datasets efficiently. By storing data in columns rather than rows, it provides superior compression and allows reading only specific columns needed for analysis. This selective reading capability, combined with predicate pushdown filtering, dramatically reduces memory usage and processing time. These features make Parquet essential for working with large-scale data in machine learning and analytics workflows.
## Accessing Data 
* head(n) - Returns the first n rows (default: 5) for preliminary data assessment
* tail(n) - Returns the last n rows (default: 5) for end-of-dataset inspection
* sample(n, random_state) - Generates random sample of n rows with reproducible results via random_state
* loc[row_labels, column_labels] - Label-based selection using explicit row and column identifiers
* iloc[row_positions, column_positions] - Integer-position based selection using numerical indices
* sort_values(by, ascending) - Orders DataFrame by specified columns with controllable sort direction
* at[row_label, column_label] - Optimized label-based scalar access for fast single-element operations
* iat[row_position, column_position] - Optimized integer-based scalar access for maximum performance on positional indexing
## Advanced Data Filtering and Querying Methods
### Conditional Filtering
* Single Condition Filtering
```python
bios.loc[bios['height_cm'] > 220]
```
* Multi-Condition Boolean Filtering
```python
bios.loc[
    (bios['height_cm'] > 215) & 
    (bios["born_country"] == "USA"), 
    ["name", "height_cm"]
]
```
### String Operation Filtering
* Pattern Matching
```python
bios[bios['name'].str.contains("Keith")]
```
### SQL-Style Query Interface
* Declarative Query Syntax
```python
bios.query('born_country == "USA"')
```


