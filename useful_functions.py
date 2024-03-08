import numpy as np

def angle_between_vectors(v1, v2):
    """Return the angle between two vectors in radians."""
    return np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

#print(angle_between_vectors(np.array([0, 1, 2]), np.array([2, 3, 4])))