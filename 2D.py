import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.transforms import Affine2D

def plot_polygon(ax, points, color, label):
    polygon = patches.Polygon(points, closed=True, fill=None, edgecolor=color, label=label)
    ax.add_patch(polygon)

def apply_transformation(points, transformation_matrix):
    homogenous_points = np.column_stack((points, np.ones(len(points))))
    transformed_points = np.dot(homogenous_points, transformation_matrix.T)[:, :2]
    return transformed_points

def main():
    # Original polygon points
    original_points = np.array([[1, 1], [2, 3], [4, 2], [3, 0]])

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    
    # Plot original polygon
    plot_polygon(ax, original_points, 'blue', 'Original')

    # Translation
    translation_matrix = np.array([[1, 0, 2], [0, 1, 2], [0, 0, 1]])
    translated_points = apply_transformation(original_points, translation_matrix)
    plot_polygon(ax, translated_points, 'green', 'Translation')

    # Rotation
    angle = np.radians(45)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])
    rotated_points = apply_transformation(original_points, rotation_matrix)
    plot_polygon(ax, rotated_points, 'red', 'Rotation')

    # Scaling
    scaling_matrix = np.array([[2, 0, 0], [0, 1.5, 0], [0, 0, 1]])
    scaled_points = apply_transformation(original_points, scaling_matrix)
    plot_polygon(ax, scaled_points, 'purple', 'Scaling')

    # Reflection
    reflection_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    reflected_points = apply_transformation(original_points, reflection_matrix)
    plot_polygon(ax, reflected_points, 'orange', 'Reflection')

    # Shearing
    shear_matrix = np.array([[1, 0.5, 0], [0.5, 1, 0], [0, 0, 1]])
    sheared_points = apply_transformation(original_points, shear_matrix)
    plot_polygon(ax, sheared_points, 'pink', 'Shearing')

    ax.legend()
    ax.set_xlim(-5, 10)
    ax.set_ylim(-5, 10)
    ax.set_title('2D Transformations')
    plt.show()

if __name__ == "__main__":
    main()
