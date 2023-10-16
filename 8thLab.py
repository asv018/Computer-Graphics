import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a 3D point as a NumPy array [x, y, z]


def create_point(x, y, z):
    return np.array([x, y, z, 1])


def translate(point, tx, ty, tz):
    translation_matrix = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    return np.dot(translation_matrix, point)


def rotate_x(point, angle_x):
    rotation_matrix = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x), 0],
        [0, np.sin(angle_x), np.cos(angle_x), 0],
        [0, 0, 0, 1]
    ])
    return np.dot(rotation_matrix, point)

# Scaling function


def scale(point, sx, sy, sz):
    scaling_matrix = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    return np.dot(scaling_matrix, point)


def plot_points(*points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for point in points:
        x, y, z, _ = point
        ax.scatter(x, y, z, marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


if __name__ == "__main__":
    original_point = create_point(1, 2, 3)
    print("Original point:", original_point)
    translated_point = translate(original_point, 2, 3, 4)
    print("Translated point:", translated_point)

    rotated_point = rotate_x(original_point, np.pi / 4)
    print("Rotated point (X-axis):", rotated_point)

    scaled_point = scale(original_point, 2, 0.5, 3)
    print("Scaled point:", scaled_point)

    plot_points(original_point, translated_point, rotated_point, scaled_point)
