import numpy as np
import pandas as pd

# Linear regression finds the best-fit line Y = m*X + b by minimizing the sum of squared errors
class LinearRegressionModelOLS:
    """docstring for Linear_Regression_Model_OLS."""
    def __init__(self, learning_rate, number_of_iterations):
        # Initialize the model with learning rate and number of iterations for gradient descent
        self.learning_rate = learning_rate
        self.number_of_iterations = number_of_iterations
        
    def fit(self, X, Y):
        # Fit the model to the training data X and Y
        self.m, self.b = X.shape
        # Initialize weights and bias to zero
        self.w = np.zeros(self.b)
        self.b = 0
        # Store the training data for use in weight updates
        self.X = X
        self.Y = Y
        # Perform gradient descent to update weights and bias
        for _ in range(self.number_of_iterations):
            self.update_weights()

        
    def update_weights(self):
        # Update weights and bias using gradient descent
        y_prediction = self.predict(self.X)
        # Calculate gradients for weights and bias
        dw = - (2 * (self.X.T).dot(self.Y - y_prediction)) / self.m
        db = - 2 * np.sum(self.Y - y_prediction) / self.m
        # Update weights and bias using the gradients and learning rate
        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db
        
    # Make predictions using the learned weights and bias
    def predict(self, X):
        return X.dot(self.w) + self.b