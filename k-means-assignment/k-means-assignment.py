import numpy as np
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    points = np.array(points)
    centroids = np.array(centroids)
    
    points = points[:, np.newaxis, :]
    distance = np.sum((points - centroids)**2, axis = 2)
    assigment  = np.argmin(distance, axis = 1)

    return assigment.tolist()
    
points = [[1,1],[1,2],[10,10],[10,11]]
centroids = [[0,0],[11,11]]
print(k_means_assignment(points, centroids))