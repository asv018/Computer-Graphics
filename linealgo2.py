import matplotlib.pyplot as plt

def draw_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    points = []
    while True:
        points.append((x0, y0))
        
        if x0 == x1 and y0 == y1:
            break
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    
    return points

# Example usage
x0, y0 = 1, 1
x1, y1 = 8, 5

line_points = draw_line(x0, y0, x1, y1)

# Extract x and y coordinates for plotting
x_coords, y_coords = zip(*line_points)

plt.plot(x_coords, y_coords, marker='o')
plt.title("Bresenham's Line Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
