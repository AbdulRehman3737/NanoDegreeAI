import numpy as np
import statistics

# KNN (K-Nearest Neighbours) Classifier
# A lazy learning algorithm that classifies new data points based on the majority label
# of the k closest training examples. No explicit training phase — all work happens at prediction.
# Supports both euclidean and manhattan distance metrics.


class KNN_Classifier:

    def __init__(self, distance_metric):
        # distance_metric: 'euclidean' (straight-line) or 'manhattan' (grid-based)
        self.distance_metric = distance_metric
        
    def compute_distance(self, training_data_point, test_data_point):
        # Euclidean distance: sqrt of sum of squared differences — straight-line distance in n-D space
        # Manhattan distance: sum of absolute differences — distance along axes only (city-block)
        if(self.distance_metric == 'euclidean'):
            dist = 0
            for i in range(len(training_data_point)):
                dist = dist + (training_data_point[i] - test_data_point[i]) ** 2
            euclidean_distance = np.sqrt(dist)
            return euclidean_distance
        elif (self.distance_metric == 'manhattan'):
            dist = 0
            for i in range(len(training_data_point)):
                dist = dist + abs(training_data_point[i] - test_data_point[i])
            manhattan_distance = dist
            return manhattan_distance
    
    def nearest_neighbours(self, X_train, test_data, k):
        # Compute distance from the test point to every training point
        distance_list = []
        for training_data in X_train:
            distance = self.compute_distance(training_data, test_data)
            distance_list.append((training_data, distance))
        
        # Sort by distance ascending so closest neighbours come first
        distance_list.sort(key=lambda x: x[1])
        # Pick the k closest training points
        neighbours_list = []
        
        for j in range(k):
            neighbours_list.append(distance_list[j][0])
            
        return neighbours_list
    
    def predict(self, X_train, Y_train, test_data, k):
        # Find the k nearest neighbours, look up their labels, then return the majority class
        neighbours = self.nearest_neighbours(X_train, test_data, k)
        
        labels = []
        # Map each neighbour back to its original label by matching the data point
        for i in range(len(X_train)):
            for j in range(len(neighbours)):
                if np.array_equal(X_train[i], neighbours[j]):
                    labels.append(Y_train[i])
            
        # Majority vote — the most frequent label among the k neighbours wins
        predicted_class = statistics.mode(labels)
        return predicted_class