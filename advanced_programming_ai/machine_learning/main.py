import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from linear_regression_model import LinearRegressionModelOLS

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
