import matplotlib.pyplot as plt

# Define the region codes for the 4 regions
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Define the window boundaries
x_min, y_min, x_max, y_max = 50, 50, 200, 200

# Define a function to compute the region code for a given point


def compute_region_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

# Define the Cohen-Sutherland clipping algorithm


def cohen_sutherland_clip(x1, y1, x2, y2):
    while True:
        # Compute region codes for both endpoints
        code1 = compute_region_code(x1, y1)
        code2 = compute_region_code(x2, y2)

        # If both endpoints are inside the window, accept the line
        if code1 == INSIDE and code2 == INSIDE:
            return x1, y1, x2, y2

        # If the line is completely outside the window, reject it
        if code1 & code2 != 0:
            return None

        # Otherwise, clip the line against the window boundaries
        x, y = 0, 0  # Initialize intersection point

        # Find the endpoint outside the window
        if code1 != INSIDE:
            code_out = code1
        else:
            code_out = code2

        # Find intersection point
        if code_out & TOP:
            x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
            y = y_max
        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            y = y_min
        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            x = x_max
        elif code_out & LEFT:
            y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            x = x_min

        # Replace the outside point with the intersection point
        if code_out == code1:
            x1, y1 = x, y
        else:
            x2, y2 = x, y


# Define the line to be clipped
x1, y1, x2, y2 = 30, 160, 250, 20

# Clip the line against the window
result = cohen_sutherland_clip(x1, y1, x2, y2)

# Plot the window and clipped line
plt.plot([x_min, x_max, x_max, x_min, x_min], [
         y_min, y_min, y_max, y_max, y_min], 'b-')
if result:
    x1_clipped, y1_clipped, x2_clipped, y2_clipped = result
    plt.plot([x1, x2], [y1, y2], 'g-', label='Original Line')
    plt.plot([x1_clipped, x2_clipped], [y1_clipped,
             y2_clipped], 'r-', label='Clipped Line')
    plt.legend()
else:
    plt.text(100, 100, 'Line is completely outside the window',
             fontsize=12, color='red')
plt.xlim(0, 300)
plt.ylim(0, 250)
plt.gca().invert_yaxis()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cohen-Sutherland Line Clipping')
plt.show()
