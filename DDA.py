import matplotlib.pyplot as plt

def dda_algorithm(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the number of steps needed for iteration
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate the increment in x and y for each step
    x_increment = dx / steps
    y_increment = dy / steps

    # Lists to store the coordinates of the line
    x_points = [x1]
    y_points = [y1]

    # Perform the iteration and calculate the coordinates for the line
    x = x1
    y = y1
    for _ in range(steps):
        x += x_increment
        y += y_increment
        x_points.append(round(x))
        y_points.append(round(y))

    return x_points, y_points

def main():
    # Input two points (x1, y1) and (x2, y2) to draw the line between them
    x1, y1 = map(int, input("Enter the coordinates of the first point (x1 y1): ").split())
    x2, y2 = map(int, input("Enter the coordinates of the second point (x2 y2): ").split())

    x_points, y_points = dda_algorithm(x1, y1, x2, y2)

    # Plot the line using matplotlib
    plt.plot(x_points, y_points, marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('DDA Algorithm Line Drawing')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
