# Numpy Data Journey
##  📊 Library Overview 
NumPy (Numerical Python) is a foundational library for numerical computing in Python. It provides powerful N-dimensional arrays that are significantly faster than Python lists because the data is stored in one continuous place in memory. For optimal performance, its core routines are written in C and C++.
## 🚀 Quick Start
### Installation
```python
pip install numpy
```
### Import
```python
import numpy as np
```
## 💻 Basic Usage Examples
### Creating Arrays
Here are some of the most common methods for creating arrays in NumPy. 
#### Creating Arrays from Existing Data
The most straightforward way to create an array is by converting a Python list.
#### Creating Pre-initialized Arrays
NumPy provides convenient functions to generate arrays with specific initial values.
* numpy.zeros((2,3)) : Creates a 2x3 array filled with zeros
* numpy.ones((2,3)) : Creates a 2x3 array filled with ones
* numpy.full((2,3),7) : Creates a 2x3 array where all elements are 7
* numpy.linspace(0, 1, 5) : Creates a 1D array of 5 evenly spaced numbers between 0 and 1

The numpy.linspace() function is particularly valuable in data science and machine learning workflows. It's commonly used to generate test data, parameter ranges, and evaluation points for various algorithms.

Regardless of the constructor used to create an array, you can enforce a single data type for all elements using the dtype parameter.

### Array Dimensions and Size
NumPy provides several functions to inspect the structure and size of arrays:
* numpy.shape : Returns a tuple representing the dimensions of the array (number of rows, columns,..)
* numpy.ndim  : Returns the number of dimensions of the array
* numpy.size  : Returns the total number of elements in the array
### Manipulate Arrays


