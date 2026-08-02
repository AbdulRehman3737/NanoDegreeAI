import pandas as pd

# TASK 1
titanic_df = pd.read_csv(r'..\datasets\titanic1.csv')

print('Shape:', titanic_df.shape)
print('\nTop 5 rows:\n', titanic_df.head())
print('\nBottom 5 rows:\n', titanic_df.tail())

print('\nSurvived count:\n', titanic_df['Survived'].value_counts())

print('\nMissing values per column:\n', titanic_df.isnull().sum())

print('\nStatistical measures:\n', titanic_df.describe())

print('\nCorrelations:\n', titanic_df.corr(numeric_only=True))

# TASK 2
unnecessary_cols = ['PassengerId', 'Name', 'Ticket', 'Cabin']
titanic_df.drop(columns=unnecessary_cols, inplace=True)

titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0])

X = titanic_df.drop(columns=['Survived'])
y = titanic_df['Survived']

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

X = pd.get_dummies(X)

scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print('\nFeatures (X) shape:', X.shape)
print('Target (y) shape:', y.shape)
print('\nX_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)

# TASK 3
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(random_state=42),
    'SVC': SVC(),
    'KNN': KNeighborsClassifier()
}

param_grids = {
    'Logistic Regression': {'C': [0.1, 1, 10]},
    'Random Forest': {'n_estimators': [50, 100], 'max_depth': [None, 5, 10]},
    'SVC': {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']},
    'KNN': {'n_neighbors': [3, 5, 7], 'weights': ['uniform', 'distance']}
}


def tune_models(model_dict, grid_dict):
    best_results = []
    for name, model in model_dict.items():
        grid_search = GridSearchCV(model, grid_dict[name], cv=5, scoring='accuracy')
        grid_search.fit(X_train, y_train)
        best_results.append((name, grid_search.best_score_, grid_search.best_params_))
        print(f'\n{name} Best Score: {grid_search.best_score_}')
        print(f'{name} Best Params: {grid_search.best_params_}')
    best_name, best_score, best_params = max(best_results, key=lambda x: x[1])
    return best_name, best_score, best_params


best_model_name, best_model_score, best_model_params = tune_models(models, param_grids)
print(f'\nBest Model: {best_model_name}')
print(f'Best Score: {best_model_score}')
print(f'Best Params: {best_model_params}')
