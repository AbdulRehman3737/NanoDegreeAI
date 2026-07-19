import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Visualize two opposing vectors to illustrate the concept of separating hyperplanes
# The red and blue arrows represent two different classes in a 2D feature space
sns.set_theme()

plt.quiver(0, 0, 4, 5, scale_units='xy', angles='xy', color='r', scale=5)
plt.quiver(0, 0, -4, -7, scale_units='xy', angles='xy', color='b', scale=5)
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()

class svm_classifier():
    """Support Vector Machine classifier using stochastic gradient descent.
    
    Finds the optimal hyperplane that maximizes the margin between two classes.
    The objective is: minimize (1/2)||w||^2 + C * sum(max(0, 1 - y_i(w·x_i - b)))
    
    Args:
        learning_rate: Step size for weight updates during gradient descent.
        number_of_iterations: Number of passes over the training data.
        lambda_parameter: Regularization strength (inverse of C); higher values
            increase regularization and shrink the model's weights.
    """
    
    def __init__(self, learning_rate, number_of_iterations, lambda_parameter):
        self.learning_rate = learning_rate
        self.number_of_iterations = number_of_iterations
        self.lambda_parameter = lambda_parameter
    
    def fit(self, X, Y):
        """Train the SVM classifier on the given data.
        
        Initializes weights to zero and iteratively updates them using
        the sub-gradient of the hinge loss + L2 regularization objective.
        
        Args:
            X: Training feature matrix of shape (n_samples, n_features).
            Y: Binary labels array of shape (n_samples,) with values 0 or 1.
        """
        self.m, self.n = X.shape  # m = number of samples, n = number of features
        self.w = np.zeros(self.n) # Weight vector (one weight per feature)
        self.b = 0                # Bias term (offset of the hyperplane)
        self.X = X
        self.Y = Y
        
        # Run gradient descent for the specified number of epochs
        for _ in range(self.number_of_iterations):
            self.update_weights()
    
    def update_weights(self):
        """Perform one pass of stochastic gradient descent over all training samples.
        
        Maps original labels {0, 1} to {-1, +1} for the SVM hinge loss formulation.
        For each sample, computes the sub-gradient of the objective:
          - If correctly classified with margin >= 1: only regularization gradient
          - Otherwise: regularization gradient + hinge loss gradient from that sample
        """
        # Convert labels: 0 -> -1, 1 -> +1 (SVM convention)
        y_label = np.where(self.Y <= 0, -1, 1)
        
        for index, x_i in enumerate(self.X):
            # Check the margin condition: y_i(w·x_i - b) >= 1
            # If true, the sample is correctly classified with sufficient margin
            condition = y_label[index] * (np.dot(x_i, self.w) - self.b) >= 1
            
            if condition == True:
                # Margin satisfied: only apply L2 regularization gradient
                # This shrinks w slightly toward zero (weight decay)
                dw = 2 * self.lambda_parameter * self.w
                db = 0
                
            else: 
                # Margin violated: add hinge loss gradient to pull w toward correct classification
                dw = 2 * self.lambda_parameter * self.w - np.dot(x_i, y_label[index])
                db = y_label[index]
                
            # Gradient descent update: move weights in the opposite direction of the gradient
            self.w = self.w - self.learning_rate * dw
            self.b = self.b - self.learning_rate * db
    
    def predict(self, X):
        """Predict class labels for new data using the learned hyperplane.
        
        Computes the signed distance of each sample from the decision boundary:
          - Positive distance -> class 1
          - Negative distance -> class 0
        
        Args:
            X: Feature matrix of shape (n_samples, n_features).
        
        Returns:
            Predicted binary labels (0 or 1) for each sample.
        """
        # Project samples onto the normal of the hyperplane and subtract bias
        output = np.dot(X, self.w) - self.b
        # Sign of the output indicates which side of the hyperplane the point falls on
        predicted_labels = np.sign(output)
        # Map back to original labels: -1 -> 0, +1 -> 1
        y_hat = np.where(predicted_labels <= -1, 0, 1)
        return y_hat