import numpy as np
import pandas as pd

# Logistic regression finds the best-fit line Y = m*X + b by minimizing the sum of squared errors
class LogisticRegressionModel:
    """docstring for Logistic_Regression_Model."""
    def __init__(self, learning_rate, number_of_iterations):
        # Initialize the model with learning rate and number of iterations for gradient descent
        self.learning_rate = learning_rate
        self.number_of_iterations = number_of_iterations
        
    def fit(self, X, Y):
        self.m, self.n = X.shape
        
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y
        
        for _ in range(self.number_of_iterations):
            self.update_weights()
        
    def update_weights(self):
        # Update weights and bias using gradient descent
        y_hat = 1 / (1 + np.exp( - (self.X.dot(self.w) + self.b)))
        # Calculate gradients for weights and bias
        dw = (1/self.m) * np.dot(self.X.T, (y_hat - self.Y))
        db = (1/self.m) * np.sum(y_hat - self.Y)
        # Update weights and bias using the gradients and learning rate
        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db
        

    def predict(self, X):
        # Make predictions using the learned weights and bias
        y_pred = 1 / (1 + np.exp( - (X.dot(self.w) + self.b)))
        y_pred = np.where(y_pred > 0.5, 1, 0)
        return y_pred