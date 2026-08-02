import pandas as pd

# TASK 1: Exploratory Data Analysis (EDA)
# Load the Titanic dataset from the CSV file into a DataFrame
titanic_df = pd.read_csv(r'..\datasets\titanic1.csv')

# Display the dimensions (rows, columns) of the DataFrame
print('Shape:', titanic_df.shape)
# Show the first 5 and last 5 rows to get a feel for the data
print('\nTop 5 rows:\n', titanic_df.head())
print('\nBottom 5 rows:\n', titanic_df.tail())

# Count how many passengers survived (1) vs did not survive (0)
print('\nSurvived count:\n', titanic_df['Survived'].value_counts())

# Check how many missing values exist in each column
print('\nMissing values per column:\n', titanic_df.isnull().sum())

# Summary statistics (mean, std, min, quartiles, max) for numeric columns
print('\nStatistical measures:\n', titanic_df.describe())

# Pairwise correlation between all numeric columns
print('\nCorrelations:\n', titanic_df.corr(numeric_only=True))

# TASK 2: Feature selection and data preparation
# Drop columns that are not useful for prediction (ids, names, tickets)
unnecessary_cols = ['PassengerId', 'Name', 'Ticket', 'Cabin']
titanic_df.drop(columns=unnecessary_cols, inplace=True)

# Fill missing Age values with the column mean
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
# Fill missing Embarked values with the most frequent value (mode)
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0])

# Separate features (X) from the target/output column (y = Survived)
X = titanic_df.drop(columns=['Survived'])
y = titanic_df['Survived']

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Convert categorical columns (Sex, Embarked) into numeric one-hot columns
X = pd.get_dummies(X)

# Standardize features to have mean 0 and standard deviation 1
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Split data into training (80%) and testing (20%) sets with a fixed seed
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print('\nFeatures (X) shape:', X.shape)
print('Target (y) shape:', y.shape)
print('\nX_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)

# TASK 3: Model selection via hyperparameter tuning
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Dictionary of 4 classification models (with the important hyperparameters set explicitly)
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(random_state=42, min_samples_leaf=1, max_features='sqrt'),
    'SVC': SVC(C=1.0, kernel='rbf', gamma='scale'),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

# Hyperparameter values to try for each model during GridSearchCV
param_grids = {
    'Logistic Regression': {'C': [0.1, 1, 10]},
    'Random Forest': {'n_estimators': [50, 100], 'max_depth': [None, 5, 10], 'min_samples_leaf': [1, 2, 4], 'max_features': ['sqrt', 'log2']},
    'SVC': {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf'], 'gamma': ['scale', 'auto']},
    'KNN': {'n_neighbors': [3, 5, 7, 9], 'weights': ['uniform', 'distance']}
}


def tune_models(model_dict, grid_dict):
    # Train each model with 5-fold cross-validation and tune its hyperparameters
    best_results = []
    for name, model in model_dict.items():
        grid_search = GridSearchCV(model, grid_dict[name], cv=5, scoring='accuracy')
        grid_search.fit(X_train, y_train)
        # Keep track of the best score and best hyperparameters for each model
        best_results.append((name, grid_search.best_score_, grid_search.best_params_))
        print(f'\n{name} Best Score: {grid_search.best_score_}')
        print(f'{name} Best Params: {grid_search.best_params_}')
    # Pick the model with the highest cross-validation accuracy
    best_name, best_score, best_params = max(best_results, key=lambda x: x[1])
    return best_name, best_score, best_params


best_model_name, best_model_score, best_model_params = tune_models(models, param_grids)
print(f'\nBest Model: {best_model_name}')
print(f'Best Score: {best_model_score}')
print(f'Best Params: {best_model_params}')
