import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv('C:\\Work\\Nano\\advanced_programming_ai\\datasets\\covid.csv')

# Check missing values and city distribution
print(df.isnull().sum())
print(df['city'].value_counts())

# Split into train/test sets (test_size=0.2 -> 20% for testing, random_state=42 -> reproducible split)
X_train, X_test, Y_train, Y_test = train_test_split(df.drop(columns=['has_covid']), df['has_covid'], test_size=0.2, random_state=42)

print(X_train)

# Impute missing fever values with mean (strategy='mean' is default)
si = SimpleImputer()
X_train_fever = si.fit_transform(X_train[['fever']])
X_test_fever = si.transform(X_test[['fever']])

print(X_train_fever)

# Ordinal encode cough: Mild->0, Strong->1 (categories specifies the ordered mapping)
oe = OrdinalEncoder(categories=[['Mild', 'Strong']])
X_train_cough = oe.fit_transform(X_train[['cough']])
X_test_cough = oe.transform(X_test[['cough']])

print(X_train_cough)

# One-hot encode city (sparse_output=False -> returns dense array, drop='first' -> drops first category to avoid multicollinearity)
ohe_city = OneHotEncoder(sparse_output=False, drop='first')
X_train_city = ohe_city.fit_transform(X_train[['city']])
X_test_city = ohe_city.transform(X_test[['city']])

print(X_train_city)

# One-hot encode gender
ohe_gender = OneHotEncoder(sparse_output=False, drop='first')
X_train_gender = ohe_gender.fit_transform(X_train[['gender']])
X_test_gender = ohe_gender.transform(X_test[['gender']])

print(X_train_gender)

# Store age column separately
X_train_age = X_train[['age']].values
X_test_age = X_test[['age']].values

# Concatenate all transformed columns into final train/test arrays
X_train_transformed = np.concatenate([X_train_fever, X_train_cough, X_train_city, X_train_gender, X_train_age], axis=1)
X_test_transformed = np.concatenate([X_test_fever, X_test_cough, X_test_city, X_test_gender, X_test_age], axis=1)

print(X_train_transformed)
print(X_test_transformed)

# Does all of the above in a single function
# Build ColumnTransformer: SimpleImputer on fever, OrdinalEncoder on cough, OneHotEncoder on gender & city, passthrough on age/rest
# Build ColumnTransformer: applies different transforms to different columns
# - SimpleImputer() -> imputes missing values with mean (strategy='mean' is default)
# - OrdinalEncoder(categories=[['Mild', 'Strong']]) -> maps Mild->0, Strong->1 (categories defines the ordered mapping)
# - OneHotEncoder(sparse_output=False, drop='first') -> creates dummy columns (sparse_output=False returns dense array, drop='first' drops first category to avoid multicollinearity)
# - remainder='passthrough' -> keeps all untransformed columns (age) as-is
transformer = ColumnTransformer(transformers=[
    ('tfn1', SimpleImputer(), ['fever']),
    ('tfn2', OrdinalEncoder(categories=[['Mild', 'Strong']]), ['cough']),
    ('tfn3', OneHotEncoder(sparse_output=False, drop='first'), ['gender', 'city']),
], remainder='passthrough')
transformer.set_output(transform='pandas')
X_train_transformed = transformer.fit_transform(X_train)
X_test_transformed = transformer.transform(X_test)

print(X_train_transformed.head())
print(X_test_transformed)