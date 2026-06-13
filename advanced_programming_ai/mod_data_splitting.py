import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

dataset = sklearn.datasets.load_breast_cancer()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# Splitting the data into features and target variable
X = df
Y = dataset.target

print(X.head())
print(Y)

# Splitting the data into training and testing sets, reserve 20% of the data for testing, random state is set to 3 for reproducibility like a seed value
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)
print(X.shape, X_train.shape, X_test.shape, Y.shape, Y_train.shape, Y_test.shape)

# Standardizing the features using StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train_standardized = scaler.transform(X_train)
X_test_standardized = scaler.transform(X_test)

print(X_train_standardized)