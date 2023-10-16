#  Program to perform 2D Transformations such as translation, rotation, scaling, reflection and sharing on a 2D shape.
import numpy as np
import matplotlib.pyplot as plt

# Define the original 2D shape as a list of vertices
original_shape = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0.5, 1.5]])

# Define transformation functions


def translate(shape, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    return np.dot(translation_matrix, np.vstack((shape.T, np.ones(len(shape))))).T[:, :2]


def rotate(shape, angle_degrees):
    angle_rad = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                                [np.sin(angle_rad), np.cos(angle_rad), 0],
                                [0, 0, 1]])
    return np.dot(rotation_matrix, np.vstack((shape.T, np.ones(len(shape))))).T[:, :2]


def scale(shape, sx, sy):
    scaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
    return np.dot(scaling_matrix, np.vstack((shape.T, np.ones(len(shape))))).T[:, :2]


def reflect(shape, axis):
    if axis == 'x':
        reflection_matrix = np.array([[1, 0, 0],
                                      [0, -1, 0],
                                      [0, 0, 1]])
    elif axis == 'y':
        reflection_matrix = np.array([[-1, 0, 0],
                                      [0, 1, 0],
                                      [0, 0, 1]])
    else:
        raise ValueError("Invalid axis. Use 'x' or 'y'.")
    return np.dot(reflection_matrix, np.vstack((shape.T, np.ones(len(shape))))).T[:, :2]


def shear(shape, kx, ky):
    shear_matrix = np.array([[1, kx, 0],
                             [ky, 1, 0],
                             [0, 0, 1]])
    return np.dot(shear_matrix, np.vstack((shape.T, np.ones(len(shape))))).T[:, :2]


# Apply transformations
translated_shape = translate(original_shape, 1, 1)
rotated_shape = rotate(original_shape, 45)
scaled_shape = scale(original_shape, 2, 0.5)
reflected_x_shape = reflect(original_shape, 'x')
sheared_shape = shear(original_shape, 0.5, 0.2)

# Plot the original and transformed shapes
plt.figure(figsize=(10, 8))
plt.plot(original_shape[:, 0], original_shape[:, 1],
         label='Original', color='blue')
plt.plot(translated_shape[:, 0], translated_shape[:,
         1], label='Translated', color='green')
plt.plot(rotated_shape[:, 0], rotated_shape[:, 1],
         label='Rotated', color='red')
plt.plot(scaled_shape[:, 0], scaled_shape[:, 1],
         label='Scaled', color='purple')
plt.plot(reflected_x_shape[:, 0], reflected_x_shape[:,
         1], label='Reflected (X-axis)', color='orange')
plt.plot(sheared_shape[:, 0], sheared_shape[:, 1],
         label='Sheared', color='pink')

plt.legend()
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True)
plt.title('2D Transformations')
plt.show()
