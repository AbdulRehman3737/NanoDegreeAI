import numpy as np

p1 = (1, 1)
p2 = (2, 2)

# Calculate the Euclidean distance between two points in 2D space
dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

# Now take the square root of the sum of squared differences to get the Euclidean distance
euclidian_distance = np.sqrt(dist)
print("Euclidian Distance: ", euclidian_distance)

# For two points in 3 dimensions
p1 = (1, 1, 1)
p2 = (2, 2, 2)
dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
euclidian_distance = np.sqrt(dist)
print("Euclidian Distance: ", euclidian_distance)

# For n dimensions
p1 = (1, 1, 1, 1)
p2 = (2, 2, 2, 2)

def get_euclidian_distance(p1, p2):
    dist = 0

    for i in range(len(p1)):
        dist = dist + (p1[i] - p2[i]) ** 2
        
    euclidian_distance = np.sqrt(dist)
    print("Euclidian Distance is: ", euclidian_distance)
    
get_euclidian_distance(p1, p2)


# Using manhatten distance
def get_manhatten_distance(p1, p2):
    dist = 0
    
    for i in range(len(p1)):
        dist = dist + abs(p1[i] - p2[i])
        
    manhatten_distance = dist
    print("Manhatten Distance is: ", manhatten_distance)

get_manhatten_distance(p1, p2)