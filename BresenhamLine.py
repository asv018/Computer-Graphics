import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
    
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    error = dx / 2
    ystep = 1 if y1 < y2 else -1
    y = y1
    
    for x in range(x1, x2 + 1):
        points.append((y, x) if steep else (x, y))
        error -= dy
        if error < 0:
            y += ystep
            error += dx
    
    return points

# Example usage
x1, y1 = 1, 1
x2, y2 = 8, 5
line_points = bresenham_line(x1, y1, x2, y2)

# Extract x and y coordinates from the line points
x_coords, y_coords = zip(*line_points)

# Create a scatter plot
plt.scatter(x_coords, y_coords, color='red', marker='o', label='Bresenham Line')

# Set plot labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bresenham Line Algorithm')

# Show a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()
