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

# np.zeros() function can be used to create an array filled with zeros. It takes the shape of the array as an argument.
zeros_array = np.zeros((3, 4))
print("Array filled with zeros:\n", zeros_array)
# Other functions to create arrays filled with specific values include np.ones() for ones, np.full() for a specified value, and np.eye() for an identity matrix.
ones_array = np.ones((3, 4))
print("Array filled with ones:\n", ones_array)
full_array = np.full((3, 4), 7)
print("Array filled with a specified value (7):\n", full_array)
identity_matrix = np.eye(4)
print("Identity matrix:\n", identity_matrix)

# .add() function can be used to perform element-wise addition of two arrays. It takes two arrays as arguments and returns a new array with the sum of the elements.
# these are all vectorized operations that can be performed on arrays without the need for explicit loops, which allows for more efficient computation.
array_a = np.array([[1, 2], [3, 4]])
array_b = np.array([[5, 6], [7, 8]])
added_array = np.add(array_a, array_b)
print("Element-wise addition of array_a and array_b:\n", added_array)
# Other element-wise operations include np.subtract() for subtraction, np.multiply() for multiplication, and np.divide() for division.

# BLAS (Basic Linear Algebra Subprograms) is a specification for a set of low-level routines that perform common linear algebra operations such as vector and matrix multiplication,
# dot products, and solving linear systems. It is designed to be highly efficient and optimized for performance on various hardware architectures. 
# BLAS is often used as a building block for higher-level linear algebra libraries and applications, providing a standardized interface for performing these operations efficiently.
# BLAS uses CPU vectorization and multi-threading to optimize performance, and it can take advantage of SIMD instructions to further improve the speed of computations.

# SIMD (Single Instruction, Multiple Data) is a parallel computing architecture that allows a single instruction to be applied to multiple data points simultaneously. 
# It is commonly used in modern CPUs and GPUs to improve performance by processing multiple data elements in parallel. SIMD can be particularly beneficial for tasks that involve large arrays or matrices, 
# such as those commonly encountered in scientific computing and machine learning, as it can significantly reduce the time required for computations by leveraging data-level parallelism.

# Diff and subtract can be used to compute the difference between two arrays. The diff() function computes the n-th discrete difference along the specified axis, while the subtract() function performs element-wise subtraction of two arrays.
array_c = np.array([1, 2, 3, 4, 5])
array_d = np.array([5, 4, 3, 2, 1])
# diff would be [2-1, 3-2, 4-3, 5-4] = [1, 1, 1, 1]
difference_array = np.diff(array_c)
print("Difference between consecutive elements in array_c:", difference_array)
subtracted_array = np.subtract(array_c, array_d)
print("Element-wise subtraction of array_c and array_d:", subtracted_array)

# LCM and GCD can be computed using np.lcm() and np.gcd() functions, respectively. The lcm() function computes the least common multiple of two arrays element-wise, while the gcd() function computes the greatest common divisor of two arrays element-wise.
array_e = np.array([12, 15, 18])
array_f = np.array([8, 10, 6])
lcm_array = np.lcm(array_e, array_f)
print("Least common multiple of array_e and array_f:", lcm_array)
gcd_array = np.gcd(array_e, array_f)
print("Greatest common divisor of array_e and array_f:", gcd_array)

# Can create a set using np.unique() function, which returns the unique elements of an array. It can also return the indices of the unique elements and the counts of each unique element.
array_g = np.array([1, 2, 2, 3, 4, 4, 4, 5])
unique_elements = np.unique(array_g)
print("Unique elements in array_g:", unique_elements)
unique_elements_with_counts = np.unique(array_g, return_counts=True)
print("Unique elements and their counts in array_g:", unique_elements_with_counts)

# We can create random numbers and n-dimensional arrays using np.random module, which provides various functions for generating random numbers and arrays. 
# For example, np.random.rand() can be used to generate an array of random numbers between 0 and 1, while np.random.randint() can be used to generate an array of random integers within a specified range.'
random_array = np.random.rand(3, 4)
print("Random array of shape (3, 4):\n", random_array)
random_integers = np.random.randint(0, 10, size=(3, 4))
print("Random integers between 0 and 10 of shape (3, 4):\n", random_integers)

# random.choice can be used to generate values with a set probability distribution. It takes an array of values and an array of probabilities as arguments and returns a random sample from the values based on the specified probabilities.
values = ['A', 'B', 'C', 'D']
probabilities = [0.5, 0.3, 0.2, 0.0] # Probabilities must sum to 1
random_sample = np.random.choice(values, size=10, p=probabilities)
print("Random sample based on specified probabilities:", random_sample)




# -----------------------------------PANDAS-------------------------------------------
import pandas as pd
import requests
from io import StringIO

# Dataframes are 2-dimensional labeled data structures with columns of potentially different types. They are similar to SQL tables or Excel spreadsheets and are one of the most commonly used data structures in pandas.
df = pd.read_csv('C:\\Work\\NanoDegreeAI\\advanced_programming_ai\\datasets\\aug_train.csv')
print("Dataframe loaded successfully. Shape:", df.shape, df)

# Can also read df from a url like this:
url = 'https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv'
df = pd.read_csv(url)
print("Dataframe loaded from URL successfully. Shape:", df.shape, df)

# To feign as a browser and avoid getting blocked by the server, we can use the headers parameter in the read_csv() function to specify a user-agent string. This can help to bypass restrictions that some servers may have in place for automated requests.
# We will use a GET request to fetch the data from the URL, and we can specify the headers to include a user-agent string that mimics a browser. This can help to avoid getting blocked by the server when trying to access the data.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
# Use stringIO and requests to read the data from the URL with headers
response = requests.get(url, headers=headers)
# StringIO allows us to treat the response text as a file-like object, which can be passed to the read_csv() function to load the data into a dataframe.
df = pd.read_csv(StringIO(response.text))
print("Dataframe loaded from URL with headers successfully. Shape:", df.shape, df)

# We can read a tsv file using the read_csv() function by specifying the delimiter as a tab character ('\t').
file_path = 'C:\\Work\\NanoDegreeAI\\advanced_programming_ai\\datasets\\movie_titles_metadata.tsv'
# Need to give names param to specify the column names since tsv files may not have a header row. The names parameter takes a list of column names that will be used to label the columns in the resulting dataframe.
df_tsv = pd.read_csv(file_path, delimiter='\t', names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres'])
print("Dataframe loaded from TSV file successfully. Shape:", df_tsv.shape, df_tsv)

# Index column can be specified using the index_col parameter in the read_csv() function. This allows us to set a specific column as the index of the dataframe, which can be useful for data manipulation and analysis.
# The index_col parameter takes the name of the column to be used as the index or the column number (starting from 0) as an argument. Setting index_col to a specific column will make that column the index of the dataframe, 
# which can be used for easier data access and manipulation.
df_indexed = pd.read_csv(file_path, delimiter='\t', names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres'], index_col='release_year')
print("Dataframe loaded with index column successfully. Shape:", df_indexed.shape, df_indexed)

# Header can be specified using the header parameter in the read_csv() function. This allows us to specify which row in the file should be used as the header (column names) of the dataframe.

# useCols parameter can be used to specify which columns to read from the file. This can be useful when we only need a subset of the columns for our analysis, as it can help to reduce memory usage and improve performance.
# The usecols parameter takes a list of column names or column numbers (starting from 0) as an argument. Only the specified columns will be read from the file and included in the resulting dataframe.
df_usecols = pd.read_csv(file_path, delimiter='\t', names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres'], usecols=['name', 'rating'])
print("Dataframe loaded with specified columns successfully. Shape:", df_usecols.shape, df_usecols)

# Skiprows and nrows parameters can be used to specify which rows to skip and how many rows to read from the file, respectively. This can be useful when we want to ignore certain rows (e.g., header rows, metadata) 
# or when we only want to read a specific number of rows for analysis.
# The skiprows parameter takes an integer or a list of integers as an argument, which specifies the number of rows to skip at the beginning of the file or the specific row numbers to skip. 
# The nrows parameter takes an integer as an argument, which specifies the number of rows to read from the file after skipping the specified rows.
df_skip_nrows = pd.read_csv(file_path, delimiter='\t', names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres'], skiprows=1, nrows=5)
print("Dataframe loaded with skipped rows and limited number of rows successfully. Shape:", df_skip_nrows.shape, df_skip_nrows)

# encoding param can be used to specify the encoding of the file being read. This is important when dealing with files that may contain special characters or non-ASCII text, as it ensures that the data is read correctly and prevents encoding-related errors.
# The encoding parameter takes a string as an argument, which specifies the encoding of the file (e.g., 'utf-8', 'latin-1', 'iso-8859-1').

# on_bad_lines parameter can be used to specify how to handle lines in the file that do not conform to the expected format (e.g., lines with missing values, extra columns). 
# This can help to prevent errors during the reading process and allow for more flexible handling of imperfect data.
# The on_bad_lines parameter takes a string as an argument, which specifies how to handle bad lines (e.g., 'error' to raise an error, 'warn' to issue a warning and skip the line, 'skip' to silently skip the line).

# .info method can be used to get a concise summary of the dataframe, including the number of non-null entries, data types of each column, and memory usage.
# This can be useful for understanding the structure of the data and identifying any potential issues (e.g., missing values, incorrect data types) that may need to be addressed before analysis.
print("Dataframe info:", df.info())

# dtype param can be used to specify the data types of the columns in the dataframe. This can be useful for ensuring that the data is read correctly and for optimizing memory usage,
# as pandas will use the specified data types when loading the data into memory.
# The dtype parameter takes a dictionary as an argument, where the keys are the column names and the values are the desired data types (e.g., {'column_name': 'data_type'}). 
# This allows us to specify the data type for each column in the dataframe, which can help to prevent issues related to incorrect data types and improve performance.
# if getting error that cannot convert according to rule safe, can use the parameter errors='coerce' to convert invalid parsing to NaN, which allows the reading process to continue without raising an error.
df_dtype = pd.read_csv(file_path, delimiter='\t', names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres'], dtype={'rating': float})
print("Dataframe loaded with specified data types successfully. Shape:", df_dtype.shape, df_dtype)

# parse_dates parameter can be used to specify which columns should be parsed as dates when reading the data. This can be useful for ensuring that date information is correctly interpreted and can be easily manipulated for analysis.
# The parse_dates parameter takes a list of column names or column numbers (starting from 0) as an argument, which specifies the columns to be parsed as dates. This allows pandas to automatically convert the specified columns into datetime objects, which can be used for various date-related operations and analyses.
df_parse_dates = pd.read_csv(file_path, delimiter='\t', names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres'], parse_dates=['release_year'])
# Expects actual dates here
print("Dataframe loaded with parsed dates successfully. Shape:", df_parse_dates.shape, df_parse_dates.info())

# converters parameter can be used to specify custom functions for converting the data in specific columns when reading the data. This can be useful for handling data that may require special processing or cleaning before it can be used for analysis.
# The converters parameter takes a dictionary as an argument, where the keys are the column names and the values are the custom functions to be applied to the data in those columns (e.g., {'column_name': function}). This allows us to apply specific transformations or cleaning operations to the data in the specified columns during the reading process, which can help to ensure that the data is in the desired format for analysis.
def convert_year(year):
    try:
        if year == '1999':
            return 20000001
        else:
            return int(year)
    except ValueError:
        return None  # or you could choose to return a default value or raise an error


df_converters = pd.read_csv(file_path, delimiter='\t', names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres'], converters={'release_year': convert_year})
print("Dataframe loaded with custom converters successfully. Shape:", df_converters, df_converters.info())

# Chunking can be done using the chunksize parameter in the read_csv() function, which allows us to read the data in smaller, manageable chunks instead of loading the entire dataset into memory at once. 
# This can be particularly useful when dealing with large datasets that may not fit into memory.
# The chunksize parameter takes an integer as an argument, which specifies the number of rows to read at a time. When the chunksize parameter is used, 
# the read_csv() function returns an iterator that yields chunks of the specified size as dataframes, allowing us to process the data in smaller portions and avoid memory issues.
chunk_size = 2
for chunk in pd.read_csv(file_path, delimiter='\t', names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres'], chunksize=chunk_size):
    print("Chunk:\n", chunk)