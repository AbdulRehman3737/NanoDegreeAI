import numpy as np

# K-Nearest Neighbours — Distance Metric Examples
# KNN relies on distance calculations to find similar data points.
# Two common metrics are demonstrated below: Euclidean and Manhattan distance.

p1 = (1, 1)
p2 = (2, 2)

# Euclidean Distance (2D): straight-line distance between two points
# Formula: sqrt((x2-x1)^2 + (y2-y1)^2)
dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

# Now take the square root of the sum of squared differences to get the Euclidean distance
euclidian_distance = np.sqrt(dist)
print("Euclidian Distance: ", euclidian_distance)

# Euclidean Distance (3D): extends the formula to three dimensions
p1 = (1, 1, 1)
p2 = (2, 2, 2)
# Formula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
euclidian_distance = np.sqrt(dist)
print("Euclidian Distance: ", euclidian_distance)

# Euclidean Distance (n dimensions): generalises to any number of features
p1 = (1, 1, 1, 1)
p2 = (2, 2, 2, 2)

def get_euclidian_distance(p1, p2):
    # Sum the squared differences across all dimensions
    dist = 0

    for i in range(len(p1)):
        dist = dist + (p1[i] - p2[i]) ** 2

    # Take the square root to get the true geometric distance
    euclidian_distance = np.sqrt(dist)
    print("Euclidian Distance is: ", euclidian_distance)
    
get_euclidian_distance(p1, p2)


# Manhattan Distance: sum of absolute differences along each axis (city-block / grid distance)
# Formula: |x2-x1| + |y2-y1| + ... — no square root needed
def get_manhatten_distance(p1, p2):
    dist = 0

    for i in range(len(p1)):
        dist = dist + abs(p1[i] - p2[i])

    manhatten_distance = dist
    print("Manhatten Distance is: ", manhatten_distance)

get_manhatten_distance(p1, p2)