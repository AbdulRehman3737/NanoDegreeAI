import numpy as np
import statistics

class KNN_Classifier:
    
    def __init__(self, distance_metric):
        self.distance_metric = distance_metric
        
    def compute_distance(self, training_data_point, test_data_point):
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
        distance_list = []
        for training_data in X_train:
            distance = self.compute_distance(training_data, test_data)
            distance_list.append((training_data, distance))
        
        distance_list.sort(key=lambda x: x[1])
        neighbours_list = []
        
        for j in range(k):
            neighbours_list.append(distance_list[j][0])
            
        return neighbours_list
    
    def predict(self, X_train, Y_train, test_data, k):
        neighbours = self.nearest_neighbours(X_train, test_data, k)
        
        labels = []
        for i in range(len(X_train)):
            for j in range(len(neighbours)):
                if np.array_equal(X_train[i], neighbours[j]):
                    labels.append(Y_train[i])
            
        predicted_class = statistics.mode(labels)
        return predicted_class