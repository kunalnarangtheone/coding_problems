import numpy as np
from collections import defaultdict

def euc_dist(a, b):
    return np.linalg.norm(a - b)

points = np.array([[1, 0], [2, 1], [5, 3], [4, 0], [6, 7], [3, 2], [9, 0], [4, 5], [5, 6], [8, 2]])
k = 4

# Intial centroids are sampled randomly without replacement
centroid_indices = np.random.choice(len(points), k, False)
centroids = [points[index] for index in centroid_indices]

distances = np.zeros((len(points), k))
# clusters = defaultdict(list)

for _ in range(5):
    clusters = defaultdict(list)
    for i in range(len(points)):
        for j in range(len(centroids)):
            distances[i][j] = euc_dist(points[i], centroids[j])
        clusters[np.argmin(distances[i])].append(points[i])

    for cluster, items in clusters.items():
        x_sum = 0
        y_sum = 0
        for x, y in items:
            x_sum+=x
            y_sum+=y

        x_avg, y_avg = float(x_sum / len(items)), float(y_sum / len(items))
        centroids[cluster] = np.array([x_avg, y_avg])

    # print(distances)
    # print(centroids)
    print(clusters)
    distances = np.zeros((len(points), k))
