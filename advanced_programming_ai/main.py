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
# Reshape takes in its argument which are (no of arrays of previous dimension, elements in each dimension) and returns a view with the specified shape
reshaped_array = original_array.reshape(3, 1)
print("Reshaped array:\n", reshaped_array, "Shape:", reshaped_array.shape)
# 3-d array can be reshaped to 2-d array by specifying the new shape
reshaped_three_d_array = three_d_array.reshape(2, 6)
print("Reshaped 3-d array:\n", reshaped_three_d_array, "Shape:", reshaped_three_d_array.shape)
# Unknown dimension can be specified using -1, which will be inferred from the length of the array and the remaining dimensions
reshaped_four_d_array = four_d_array.reshape(2, 2, -1)
print("Reshaped 4-d array:\n", reshaped_four_d_array, "Shape:", reshaped_four_d_array.shape)

# flattening can be done with reshape or with flatten() method
flattened_array = original_array.reshape(-1)
print("Flattened array:", flattened_array, "Shape:", flattened_array.shape)
flattened_array_2 = original_array.flatten()
print("Flattened array using flatten():", flattened_array_2, "Shape:", flattened_array_2.shape)

# nditer is a multi-dimensional iterator object to iterate over arrays of any shape. It provides an efficient way to access and manipulate elements of an array.
# Helps to avoid nested loops when iterating over multi-dimensional arrays, which can be inefficient and hard to read. It allows us to
# iterate over each element of the array in a single loop, regardless of the number of dimensions.
print("Iterating over n_dimension_array:")
for element in np.nditer(n_dimension_array):
    print(element)

# op_dtype is a prop that can be used to specify the data type of the output array when performing operations on arrays.
# It is used in functions like np.add, np.multiply, etc. to ensure that the result of the operation is of a specific data type.
# flag = buffered is used to create a temporary buffer to hold the data during iteration, which can improve performance when iterating over large arrays.
print("Iterating with op_dtype and buffered flag:")
for element in np.nditer(n_dimension_array, op_dtypes=['S'], flags=['buffered']):
    print(element)

# ndenumerate returns indexes and values of an array as a tuple. It is used to iterate over multi-dimensional arrays and get both the index and value of each element.
print("Enumerating n_dimension_array:")
for index, value in np.ndenumerate(n_dimension_array):
    print("Enumerate:", index, value)

# concatenate arrays using np.concatenate() function. It takes a sequence of arrays and concatenates them along a specified axis.
# axis is a prop that specifies the axis along which the arrays will be concatenated. The default is 0, which means the arrays will be concatenated along the first axis (rows).
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
concatenated_array = np.concatenate((array1, array2), axis=0)
print("Concatenated array along axis 0:\n", concatenated_array)
concatenated_array_axis1 = np.concatenate((array1, array2), axis=1)
print("Concatenated array along axis 1:\n", concatenated_array_axis1)

# We also have dstack, hstack, vstack for stacking arrays along different axes without needing to specify the axis parameter.
# dstack stacks arrays along the third axis (depth), hstack stacks arrays horizontally (along columns), and vstack stacks arrays vertically (along rows).
dstacked_array = np.dstack((array1, array2))
print("Dstacked array:\n", dstacked_array)
hstacked_array = np.hstack((array1, array2))
print("Hstacked array:\n", hstacked_array)
vstacked_array = np.vstack((array1, array2))
print("Vstacked array:\n", vstacked_array)
# there is a normal stack() function that can be used to stack arrays along a specified axis, similar to concatenate but with more options for stacking.
stacked_array = np.stack((array1, array2), axis=0)
print("Stacked array along axis 0:\n", stacked_array)
# split() function can be used to split an array into multiple sub-arrays along a specified axis. It takes the array to be split,
# the number of splits, and the axis along which to split as arguments.
split_array = np.split(concatenated_array, 2, axis=0)
print("Split array along axis 0:\n", split_array)
# hsplit() and vsplit() can be used to split arrays horizontally and vertically, respectively, without needing to specify the axis parameter.
hsplit_array = np.hsplit(concatenated_array, 2)
print("Hsplit array:\n", hsplit_array)
vsplit_array = np.vsplit(concatenated_array, 2)
print("Vsplit array:\n", vsplit_array)
# sorting an array can be done using the sort() method, which sorts the array in-place, or the sorted() function, which returns a new sorted array.
# We can also specify the axis along which to sort the array. By default, it sorts along the last axis.
sorted_array = np.sort(concatenated_array, axis=0)
print("Sorted array along axis 0:\n", sorted_array)
sorted_array_axis1 = np.sort(concatenated_array, axis=1)
print("Sorted array along axis 1:\n", sorted_array_axis1)

# searchSorted function can be used to find the indices where elements should be inserted to maintain order in a sorted array.
# It takes a sorted array and the values to be inserted as arguments.
sorted_array_1d = np.array([1, 3, 5, 7, 9])
values_to_insert = [4, 10]
insertion_indices = np.searchsorted(sorted_array_1d, values_to_insert)
print("Insertion indices for values in sorted_array_1d:", insertion_indices)

# Filtering an array can be done using boolean indexing, where we create a boolean mask based on a condition and use it to filter the array.
# For example, to filter out elements greater than 5 from an array, we can create a boolean mask and use it to index the array.
array_to_filter = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
boolean_mask = array_to_filter > 5
filtered_array = array_to_filter[boolean_mask]
print("Filtered array (elements greater than 5):", filtered_array)
# A very simple example of filtering could be to filter out even numbers from an array. We can create a boolean mask for even numbers and use it to filter the array.
even_mask = array_to_filter % 2 == 0
filtered_even_array = array_to_filter[even_mask]
print("Filtered array (even numbers):", filtered_even_array)
print("True or False: ", array_to_filter[[True, False, True, False, True, False, True, False, True]])