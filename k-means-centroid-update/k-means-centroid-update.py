import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    points = np.array(points)
    assignments = np.array(assignments)
    centroids = []
    for i in range(k):
        x = points[assignments == i]
        c = np.mean(x, axis = 0)
        centroids.append(c.tolist())
    return centroids
points = [[0,0],[2,2],[10,10],[12,12]]
assignments = [0,0,1,1]
k = 2
print(k_means_centroid_update(points, assignments, k))