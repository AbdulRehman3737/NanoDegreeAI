# -----------------------------------PANDAS-------------------------------------------
import pandas as pd
import requests
from io import StringIO

# Dataframes are 2-dimensional labeled data structures with columns of potentially different types. They are similar to SQL tables or Excel spreadsheets and are one of the most commonly used data structures in pandas.
df = pd.read_csv('C:\\Nano\\advanced_programming_ai\\datasets\\aug_train.csv')
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
file_path = 'C:\\Nano\\advanced_programming_ai\\datasets\\movie_titles_metadata.tsv'
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
    

# df.head method can be used to view the first few rows of the dataframe, while tail can be used to view the last few rows, which can be useful for getting a quick overview of the data and checking that it has been loaded correctly.
df = pd.read_csv('C:\\Nano\\advanced_programming_ai\\datasets\\BostonHousing.csv')
print("First 5 rows of the dataframe:\n", df.head(), df.tail())

# type of df.shape is a tuple that represents the dimensions of the dataframe, where the first element is the number of rows and the second element is the number of columns.
print("Shape of the dataframe:", df.shape, "Type of shape:", type(df.shape))

# isnull method can be used to check for missing values in the dataframe, which can be important for data cleaning and preprocessing before analysis.
# The isnull() method returns a dataframe of the same shape as the original dataframe, where each element is a boolean value indicating whether the corresponding element in the original dataframe is null (True) or not (False).
# This allows us to easily identify and handle missing values in the dataset.
print("Missing values in the dataframe:\n", df.isnull().sum())

# value_counts method can be used to count the occurrences of unique values in a column, which can be useful for understanding the distribution of categorical data and identifying any potential issues (e.g., imbalanced classes) 
# that may need to be addressed before analysis.
# The value_counts() method returns a Series containing counts of unique values in the specified column, sorted in descending order. 
# This allows us to quickly see the frequency of each unique value in the column, which can be helpful for understanding the distribution of the data and making informed decisions about how to handle it during analysis.
print("Value counts for the 'PTRATIO' column:\n", df['ptratio'].value_counts())

# gourp_by and mean can be used to group the data by a specific column and calculate the mean of another column for each group, which can be useful for summarizing and analyzing the data based on different categories or groups.
# The groupby() method is used to group the data based on the values in a specified column, and the mean() method is then applied to calculate the average of another column for each group.
# This allows us to easily compare the average values across different groups and identify any patterns or trends in the data that may be relevant for analysis.
grouped_mean = df.groupby('ptratio').mean()
print("Mean of grouped by 'ptratio':\n", grouped_mean)

# .describe method can be used to get a statistical summary of the numerical columns in the dataframe, which can be useful for understanding the distribution and characteristics of the data.
# The describe() method returns a dataframe that includes various statistical measures such as count, mean, standard deviation, minimum, 25th percentile, median (50th percentile), 75th percentile, 
# and maximum for each numerical column in the original dataframe.
# This allows us to quickly assess the central tendency, variability, and range of the data, which can be helpful for identifying any potential issues (e.g., outliers, skewness) that may need to be addressed before analysis.
print("Statistical summary of the dataframe:\n", df.describe())

# drop method can be used to remove specific columns or rows from the dataframe, which can be useful for data cleaning and preprocessing before analysis.
# The drop() method takes the labels of the rows or columns to be dropped as an argument, along with the axis parameter to specify whether to drop rows (axis=0) or columns (axis=1).
# This allows us to easily remove any unnecessary or irrelevant data from the dataframe, which can help to simplify the analysis and improve performance by reducing the size of the dataset.
# For example, to drop the 'age' column from the dataframe, we can use the following code:
df_dropped = df.drop('age', axis=1)
print("Dataframe after dropping 'age' column:\n", df_dropped.head())

# iloc and loc can be used for indexing and selecting data from the dataframe. iloc is used for integer-based indexing, while loc is used for label-based indexing.
# The iloc[] indexer allows us to select rows and columns based on their integer position in the dataframe, while the loc[] indexer allows us to select rows and columns based on their labels (e.g., column names, row indices).
# This provides flexibility in how we access and manipulate the data in the dataframe, allowing us to easily select specific subsets of the data for analysis or visualization.
# For example, to select the first 5 rows and the 'age' column using iloc, we can use the following code:
selected_data_iloc = df.iloc[0:5, df.columns.get_loc('age')]
print("Selected data using iloc:\n", selected_data_iloc)
# To select the same data using loc, we can use the following code:
selected_data_loc = df.loc[0:4, 'age']
print("Selected data using loc:\n", selected_data_loc)

# df.corr() method can be used to compute the pairwise correlation of the columns in the dataframe, which can be useful for understanding the relationships between
# different variables and identifying any potential correlations that may be relevant for analysis.
# The corr() method returns a dataframe containing the correlation coefficients between each pair of columns in the original dataframe. 
# The correlation coefficient ranges from -1 to 1, where values close to 1 indicate a strong positive correlation, values close to -1 indicate a strong negative correlation, and values close to 0 indicate no correlation.
# This allows us to quickly identify any strong correlations between variables, which can be helpful for feature selection, understanding the underlying structure of the data, and making informed decisions about how to handle the data during analysis.
correlation_matrix = df.corr()
print("Correlation matrix of the dataframe:\n", correlation_matrix)

# dropna method can be used to remove rows or columns with missing values from the dataframe, which can be useful for data cleaning and preprocessing before analysis.
# The dropna() method takes the axis parameter to specify whether to drop rows (axis=0) or columns (axis=1) that contain missing values.
df_dropna = df.dropna(axis=0)
print("Dataframe after dropping rows with missing values:\n", df_dropna.info())

# fillna method can be used to fill missing values in the dataframe with a specified value or method, which can be useful for data cleaning and preprocessing before analysis.
# The fillna() method takes a value or a method as an argument to fill the missing values in the dataframe. For example, we can fill missing values with a specific value (e.g., 0) or use a method such as 'ffill' (forward fill) or 
# 'bfill' (backward fill) to propagate non-null values forward or backward, respectively.
df_fillna = df.fillna(0)
# inplace parameter can be used to modify the original dataframe directly without creating a new one. If inplace=True, the original dataframe will be modified and the method will return None.
# If inplace=False (default), a new dataframe with the filled values will be returned, and the original dataframe will remain unchanged.
print("Dataframe after filling missing values with 0:\n", df_fillna.info())
# can be done for a specific column as well by specifying the column name in the fillna() method. For example, to fill missing values in the 'age' column with the mean age, we can use the following code:
mean_age = df['age'].mean()
df_fillna_age = df.fillna({'age': mean_age})
print("Dataframe after filling missing values in 'age' column with mean:\n", df_fillna_age.info())


# Label encoding can be done using the LabelEncoder class from the sklearn.preprocessing module, which can be useful for converting categorical variables into numerical format for analysis and modeling.
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

label_encoder = LabelEncoder()

cancer_data = pd.read_csv('C:\\Nano\\advanced_programming_ai\\datasets\\breast-cancer.csv')
# The fit_transform() method of the LabelEncoder class is used to fit the encoder to the data and transform the categorical labels into numerical format in a single step.
labels = label_encoder.fit_transform(cancer_data['diagnosis'])
print("Encoded labels for 'diagnosis' column:\n", labels)
# After encoding the 'diagnosis' column, we can add the encoded labels back to the original dataframe as a new column (e.g., 'diagnosis_encoded') for further analysis or modeling.
cancer_data['diagnosis_encoded'] = labels
print("Dataframe with encoded 'diagnosis' column:\n", cancer_data.head())

# diff between ordinal and nominal encoding is that ordinal encoding assigns a unique integer to each category based on a specific order or ranking, while nominal encoding assigns a unique integer to each category without any inherent order or ranking.
# Ordinal encoding is used when the categories have a meaningful order (e.g., low, medium, high), while nominal encoding is used when the categories do not have a meaningful order (e.g., colors, types of animals).
# In ordinal encoding, the assigned integers reflect the relative position of the categories, while in nominal encoding, the assigned integers are arbitrary and do not imply any order or ranking among the categories.
customer_pd = pd.read_csv('C:\\Nano\\advanced_programming_ai\\datasets\\customer.csv')
print("Original 'customer_type' column:\n", customer_pd.head())
labels = label_encoder.fit_transform(customer_pd['Purchased'])
customer_pd['Purchased_encoded'] = labels
customer_pd.drop('Purchased', axis=1, inplace=True)
print("Dataframe with encoded 'Purchased' column:\n", customer_pd.head())

# ordinalEncoding on Review and education columns
ordinal_encoder = OrdinalEncoder(categories=[['Poor', 'Average', 'Good'], ['School', 'UG', 'PG']])
encoded = ordinal_encoder.fit_transform(
    customer_pd[['Review', 'Education']]
)
customer_pd[['Review_encoded', 'Education_encoded']] = encoded
customer_pd.drop(['Review', 'Education'], axis=1, inplace=True)
print("Dataframe with encoded 'Review' and 'Education' columns:\n", customer_pd.head())

# One hot encoding can be done using the OneHotEncoder class from the sklearn.preprocessing module, which can be useful for converting categorical variables into a binary format for analysis and modeling.
# One-hot encoding creates new binary columns for each category in the original column, where each column represents the presence (1) or absence (0) of a specific category. This allows us to represent
# categorical variables in a format that can be easily used for machine learning algorithms, which typically require numerical input.
heart_pd = pd.read_csv('C:\\Nano\\advanced_programming_ai\\datasets\\heart.csv')
categorical_variables = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'ca', 'thal']
numeric_variables = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'slope']
heart_df_onehot = pd.get_dummies(heart_pd, columns=categorical_variables)
print("Dataframe after one-hot encoding:\n", heart_df_onehot.head())

# Balancing the dataset can be done using the resample function from the sklearn.utils module, which can be useful for addressing class imbalance in the dataset before analysis and modeling.
# The resample function allows us to either upsample the minority class (i.e., increase the number of samples in the minority class) or downsample the majority class (i.e., decrease the number of samples in the majority class) to create a balanced dataset.
from sklearn.utils import resample
credit_data = pd.read_csv('C:\\Nano\\advanced_programming_ai\\datasets\\credit_data.csv')
# Separate majority and minority classes
majority_class = credit_data[credit_data['Class'] == 0]
minority_class = credit_data[credit_data['Class'] == 1]
# Before balancing
print("Original dataset:\n", credit_data['Class'].value_counts())
# Downsample majority class
majority_downsampled = resample(majority_class, replace=False, n_samples=len(minority_class), random_state=42)
# Combine minority class with downsampled majority class
balanced_data = pd.concat([majority_downsampled, minority_class])
print("Balanced dataset:\n", balanced_data['Class'].value_counts())

# We can also do it with normal methods like .sample and concatenate. For example, to downsample the majority class using the sample() method, we can use the following code:
majority_downsampled_sample = majority_class.sample(n=len(minority_class), random_state=42)
balanced_data_sample = pd.concat([majority_downsampled_sample, minority_class])
print("Balanced dataset using sample method:\n", balanced_data_sample['Class'].value_counts())

# Standardization can be done using the StandardScaler class from the sklearn.preprocessing module, which can be useful for scaling numerical features to have a mean of 0 and a standard deviation of 1 before analysis and modeling.
# Standardization is important because it can help to improve the performance of machine learning algorithms by ensuring that the features are on a similar scale, which can prevent certain features from dominating the learning process and can help to improve convergence during training.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Can make datasets via scikit-learn's built-in datasets module, which provides various datasets for testing and experimentation. For example, we can load the breast cancer dataset using the following code:
from sklearn.datasets import load_breast_cancer
dataset = load_breast_cancer()
new_dataFrame = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
print("New dataframe created from breast cancer dataset:\n", new_dataFrame.head())
# We can then apply standardization to the numerical features in the new dataframe using the StandardScaler class. For example, to standardize the 'mean radius' feature, we can use the following code:
new_dataFrame['mean radius'] = scaler.fit_transform(new_dataFrame[['mean radius']])
print("Dataframe after standardizing 'mean radius' feature:\n", new_dataFrame.head())


# Training a model goes like:
# -> Data Cleaning (Duplication removing, handling missing values, handling outliers)
# -> Data Splitting (Train-test split)
# -> Encoding of categorical variables (One Hot Encoding, Label Encoding, Ordinal Encoding)
# -> Feature Scaling of Numerical Data (Standardization, Normalization)
# -> Feature Engineering and Selection (Creating new features, selecting important features based on correlation, feature importance, etc.)
# -> Model Training (Using algorithms like Logistic Regression, Decision Trees, etc.)
# -> Model Evaluation (Using metrics like accuracy, precision, recall, etc.)
# -> Hyperparameter Tuning (Using techniques like Grid Search, Random Search, etc.)
# -> Final Model Selection and Deployment.