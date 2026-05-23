# Advanced programming for AI - main.py

# Numpy - For computing and data manipulation
# Pandas - For data analysis and manipulation
# Scikit-learn - For machine learning algorithms and tools
# Matplotlib - For data visualization
# Seaborn - For statistical data visualization
# ------------------------------------------------------
# Deeplearning Libraries: in deeplearning semester
# TensorFlow - For deep learning and neural networks
# PyTorch - For deep learning and neural networks
# Keras - High-level neural networks API, running on top of TensorFlow
# ------------------------------------------------------
import numpy as np
from time import process_time

print(f"NumPy is installed. Version: {np.__version__}")

# Every element like 1, 2 is 0-dimensional array (scalar) or rank-0 tensor
# A 1-d array contains 0-d arrays (scalars) and is called a vector or rank-1 tensor
# A 2-d array contains 1-d arrays (vectors) and is called a matrix or rank-2 tensor
# A 3-d array contains 2-d arrays (matrices) and is called a tensor or rank-3 tensor
n_dimension_array = np.array([[1, 2], [3, 4]])
# Above is a 2-d array (matrix) containing 1-d arrays (vectors) which in turn contain 0-d arrays (scalars)
nd_array_tuple = np.array((1, 3, 4, 5))
print("N-dimensional array:\n", n_dimension_array, type (n_dimension_array))
print("Tuple array:\n", nd_array_tuple, type (nd_array_tuple))

# Shapes are represented in tuples, (rows, columns) for 2-d arrays
print("Shape of n_dimension_array:", n_dimension_array.shape)
print("Shape of nd_array_tuple:", nd_array_tuple.shape)
# For 3-d arrays, shape is represented as (depth, rows, columns)
three_d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print("Shape of 3_d_array:", three_d_array.shape)
# To get dimensions of an array, we can use the ndim attribute
print("Dimensions of n_dimension_array:", n_dimension_array.ndim)
print("Dimensions of three_d_array:", three_d_array.ndim)

# ndmin as a prop to specify minimum dimensions of the array
nd_array_min_dim = np.array([1, 2, 3], ndmin=5)
print("Array with minimum dimensions: ", nd_array_min_dim, "Shape:", nd_array_min_dim.shape)

# Compare list and nd array performance
start_time = process_time()
list_example = list(range(1000000))
list_example = [x+5 for x in list_example]  # Adding 5 to each element
end_time = process_time()
print(f"Time taken by list: {end_time - start_time}")

# ndarrays are faster beause they take the same space in memory instead of multiple instances like a list
# Vectorized operations in ndarrays are optimized and implemented in C, which is much faster than Python loops used in lists.
# Vectorized operations are operations that can be applied to entire arrays without the need for explicit loops, which allows for more efficient computation.
start_time = process_time()
nd_array_example = np.array(range(1000000))
nd_array_example += 5  # Adding 5 to each element
end_time = process_time()
print(f"Time taken by NumPy array: {end_time - start_time}")

# Index in nd arrays is similar to lists, but we can also use multi-dimensional indexing
# For 2-d arrays, we can use [row_index, column_index] to access elements
print("Element at (0, 1) in n_dimension_array:", n_dimension_array[0, 1])
# For 3-d arrays, we can use [depth_index, row_index, column_index] to access elements
print("Element at (1, 0, 1) in three_d_array:", three_d_array[1, 0, 1])
# For 4-d arrays, we can use [time_index, depth_index, row_index, column_index] to access elements
four_d_array = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print("Element at (0, 1, 0, 1) in four_d_array:", four_d_array[0, 1, 0, 1])

# Slicing in nd arrays is similar to lists, but we can also use multi-dimensional slicing
# For 2-d arrays, we can use [row_start:row_end, column_start:column_end] to slice elements
print("Sliced array from n_dimension_array:\n", n_dimension_array[0:2, 0:2])
# For 3-d arrays, we can use [depth_start:depth_end, row_start:row_end, column_start:column_end] to slice elements
print("Sliced array from three_d_array:\n", three_d_array[0:2, 0:2, 0:2])
# For 4-d arrays, we can use [time_start:time_end, depth_start:depth_end, row_start:row_end, column_start:column_end] to slice elements
print("Sliced array from four_d_array:\n", four_d_array[0:2, 0:2, 0:2, 0:2])

# dType of an array can be specified using the dtype parameter
int_array = np.array([15, 21, 36], dtype=int)
float_array = np.array([1, 2, 3], dtype=float)
print("Integer array:", int_array, "Data type:", int_array.dtype)
print("Float array:", float_array, "Data type:", float_array.dtype)

# asType() method can be used to change the data type of an array
converted_array = int_array.astype(float)
print("Converted array:", converted_array, "Data type:", converted_array.dtype)

# copy and view of an array
original_array = np.array([1, 2, 3])
# A view is a new array object that looks at the same data of the original array. Changes to the view will affect the original array and vice versa.
view_array = original_array.view()
view_array[0] = 10
print("Original array after modifying view:", original_array)
# A copy is a new array object that has its own data. Changes to the copy will not affect the original array and vice versa.
copy_array = original_array.copy()
copy_array[0] = 20
print("Original array after modifying copy:", original_array, "Copy array:", copy_array)

# Base attribute finds if an array is original or a view
# If it returns none, it not pointing to anything, its original
# If it returns an array, it a view pointing at something
print("Original: ", original_array.base, "Copy: ", copy_array.base, "View: ", view_array.base)

# Reshaping an array can be done using the reshape() method
# Reshaping does not change the data of the array, it only changes the shape. The total number of elements must remain the same.
# Reshape takes in its argument which are (arrays, elements in each dimension) and returns a new array with the specified shape
reshaped_array = original_array.reshape(3, 1)
print("Reshaped array:\n", reshaped_array, "Shape:", reshaped_array.shape)