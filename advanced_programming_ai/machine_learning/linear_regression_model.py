# Linear regression finds the best-fit line Y = m*X + b by minimizing the sum of squared errors
class LinearRegressionModelOLS:
    """docstring for Linear_Regression_Model_OLS."""
    def __init__(self):
        # m = slope (how much Y changes per 1-unit increase in X)
        self.m = None
        # b = y-intercept (predicted Y when X = 0)
        self.b = None
        
    # Fit the model using Ordinary Least Squares: calculate optimal m and b from training data
    def fit(self, X_train, y_train):
        # Numerator of slope formula: sum of (X deviation)*(Y deviation) — measures covariance
        num = 0
        # Denominator of slope formula: sum of squared X deviations — measures variance of X
        den = 0
        
        # Loop over every data point to compute the summations
        for i in range(X_train.shape[0]):
            # Σ (Xᵢ - X̄)(Yᵢ - Ȳ): positive when both deviate in the same direction
            num = num + ((X_train[i] - X_train.mean()) * (y_train[i] - y_train.mean()))
            # Σ (Xᵢ - X̄)²: spreads in X give more stable slope estimates
            den = den + ((X_train[i] - X_train.mean()) * (X_train[i] - X_train.mean()))

        # m = covariance(X,Y) / variance(X) — the angle of the best-fit line
        self.m = num/den
        # b = Ȳ - m*X̄ — shifts the line to pass through the center (X̄, Ȳ) of the data
        self.b = y_train.mean() - (self.m * X_train.mean())
        print(self.m)
        print(self.b)
        
    # Predict Y for new X values using the learned line: Ŷ = m*X + b
    def predict(self, X_test):
        print(X_test)
        return self.m * X_test + self.b
