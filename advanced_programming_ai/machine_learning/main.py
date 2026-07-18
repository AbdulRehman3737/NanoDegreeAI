import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from knn_classifier import KNN_Classifier
from linear_regression_model import LinearRegressionModelOLS
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv('C:\\Work\\Nano\\advanced_programming_ai\\datasets\\placement.csv', encoding='latin1')

print(df.head())

plt.scatter(df['cgpa'], df['package'])
plt.xlabel("CGPA")
plt.ylabel('Package')
plt.show()

x = df.iloc[:, 0:1]
y = df.iloc[:, -1]

print("X: ", x, '\n')
print("Y: ", y, '\n')

# Split data: 80% training (model learns from this), 20% testing (evaluates generalization)
# random_state=2 ensures reproducible splits
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

lr = LinearRegression()
# Find the line (m, b) that minimizes sum of squared residuals on training data
lr.fit(X_train, y_train)

# Predict package for a single student using the learned equation: package = m*cgpa + b
print("Predict: ", lr.predict(X_test.iloc[0].values.reshape(1, 1)))

plt.scatter(df['cgpa'], df['package'])
plt.plot(X_train, lr.predict(X_train), color='red')
plt.xlabel("CGPA")
plt.ylabel('Package')
plt.show()

# Extract learned slope (m) and intercept (b) from the trained model
m = lr.coef_
b = lr.intercept_

# Manual calculation using the linear equation — should match lr.predict()
print(m * 8.58 + b)

x = df.iloc[:, 0:1].values
y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
manual_lr = LinearRegressionModelOLS()
# Train our own OLS model from scratch — same math as sklearn under the hood
manual_lr.fit(X_train, y_train)
# Predict with our manual model — result should match sklearn's
print("Manual Prediction: ", manual_lr.predict(X_test[0]))


# Now with the custom model for linear regression using gradient descent
from linear_regression_biased_model import LinearRegressionModelOLS as BiasedLinearRegressionModel

salary_data = pd.read_csv('C:\\Work\\Nano\\advanced_programming_ai\\datasets\\salary_data.csv', encoding='latin1')
x = salary_data.iloc[:, :-1].values
y = salary_data.iloc[:, 1].values
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
biased_lr = BiasedLinearRegressionModel(learning_rate=0.02, number_of_iterations=1000)
biased_lr.fit(X_train, y_train)
print('Bias and Weight are: ', biased_lr.b, biased_lr.w[0])
print("Biased Model Prediction: ", biased_lr.predict(X_test))

# We can find errors like MSE and Rsquared to evaluate the performance of our model
y_pred = biased_lr.predict(X_test)
# Value means the average squared difference between predicted and actual values — lower is better
mse = np.mean((y_test - y_pred) ** 2)
print("Mean Squared Error: ", mse)
# Value indicates how well the model explains the variance in the data — closer to 1 is better
rsquared = 1 - (np.sum((y_test - y_pred) ** 2) / np.sum((y_test - np.mean(y_test)) ** 2))
print("R-squared: ", rsquared)




# LOGISTIC REGRESSION is used for classification problems where the output is categorical (e.g., yes/no, 0/1). 
# It predicts the probability of a binary outcome based on input features. The model uses the logistic function to map predicted values to probabilities between 0 and 1.
from logistic_regression_model import LogisticRegressionModel

diabetes_data = pd.read_csv('C:\\Work\\Nano\\advanced_programming_ai\\datasets\\diabetes.csv', encoding='latin1')
features = diabetes_data.drop(columns=['Outcome'])
target = diabetes_data['Outcome']
scalar = StandardScaler()
scalar.fit(features)
standardized_data = scalar.transform(features)
X_train, X_test, y_train, y_test = train_test_split(standardized_data, target, test_size=0.2, random_state=2)
classifier = LogisticRegressionModel(learning_rate=0.01, number_of_iterations=1000)
classifier.fit(X_train, y_train)

x_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(y_train, x_train_prediction)
print("Accuracy on training data: ", training_data_accuracy)

x_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(y_test, x_test_prediction)
print("Accuracy on test data: ", test_data_accuracy)


input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)
# Change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)
# Reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
# Standardize the input data using the same scaler used for training
std_data = scalar.transform(input_data_reshaped)
prediction = classifier.predict(std_data)
if prediction[0] == 0:
    print("The person is not diabetic")
else:
    print("The person is diabetic")
    
    
# KNN Usage
classifier = KNN_Classifier(distance_metric='euclidean')
diabetes_data = pd.read_csv('C:\\Work\\Nano\\advanced_programming_ai\\datasets\\diabetes.csv', encoding='latin1')
X = diabetes_data.drop(columns=['Outcome'])
Y = diabetes_data['Outcome']
X = X.to_numpy()
Y = Y.to_numpy()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
k = 5
predictions = []
for test_data in X_test:
    predicted_class = classifier.predict(X_train, Y_train, test_data, k)
    predictions.append(predicted_class)
accuracy = accuracy_score(Y_test, predictions)
print("KNN Classifier Accuracy: ", accuracy)
