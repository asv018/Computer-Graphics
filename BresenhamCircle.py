import matplotlib.pyplot as plt

def draw_circle(center_x, center_y, radius):
    x = 0
    y = radius
    p = 3 - 2 * radius
    
    points = []
    
    while x <= y:
        points.append((x + center_x, y + center_y))
        points.append((-x + center_x, y + center_y))
        points.append((x + center_x, -y + center_y))
        points.append((-x + center_x, -y + center_y))
        points.append((y + center_x, x + center_y))
        points.append((-y + center_x, x + center_y))
        points.append((y + center_x, -x + center_y))
        points.append((-y + center_x, -x + center_y))
        
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1
        x += 1
    
    return points

# Example usage
center_x, center_y = 5, 5
radius = 4

circle_points = draw_circle(center_x, center_y, radius)

# Extract x and y coordinates from the circle points
x_coords, y_coords = zip(*circle_points)

# Create a scatter plot
plt.scatter(x_coords, y_coords, color='blue', marker='o', label='Bresenham Circle')

# Connect the points with lines to form the circle
for i in range(len(circle_points) - 1):
    plt.plot([circle_points[i][0], circle_points[i + 1][0]], [circle_points[i][1], circle_points[i + 1][1]], color='blue')

# Connect the last point with the first point to complete the circle
plt.plot([circle_points[-1][0], circle_points[0][0]], [circle_points[-1][1], circle_points[0][1]], color='blue')

# Set plot labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bresenham Circle Drawing Algorithm')

# Show a grid
plt.grid(True)

# Show the plot
plt.show()
