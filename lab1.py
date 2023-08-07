import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], color='blue', linewidth=2)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Drawing')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x1, y1 = 1, 2  # Starting point
    x2, y2 = 8, 7  # Ending point

    draw_line(x1, y1, x2, y2)
    