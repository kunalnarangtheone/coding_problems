import numpy as np
from collections import defaultdict
from statistics import mode

def euc_dist(a, b):
    return np.linalg.norm(a - b)

points = [([1, 0], 0), ([2, 1], 1), ([5, 3], 1), ([4, 0], 1), ([6, 7], 0), ([3, 2], 0), ([9, 0], 1), ([4, 5], 1), ([5, 6], 1), ([8, 2], 0)]
prediction = []

k = 5


# for point, actual_tag in points:
#     distances = [0 for _ in range(points)]

for i in range(len(points)):
    distances = []
    for j in range(len(points)):
        if i != j:
            distances.append((euc_dist(np.array(points[i][0]), np.array(points[j][0])), points[j]))

    distances.sort()
    tags = [distance[1][1] for distance in distances[:k]]
    prediction.append(mode(tags))

print(f"Actual: {[point[1] for point in points]}")
print(f"Prediction: {prediction}")
