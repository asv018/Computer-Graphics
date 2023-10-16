import matplotlib.pyplot as plt


def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            r = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, r)
            else:
                u2 = min(u2, r)

    if u1 > u2:
        return None
    else:
        clipped_x1 = x1 + u1 * dx
        clipped_y1 = y1 + u1 * dy
        clipped_x2 = x1 + u2 * dx
        clipped_y2 = y1 + u2 * dy
        return (clipped_x1, clipped_y1, clipped_x2, clipped_y2)


x1, y1 = 2, 3
x2, y2 = 8, 6


xmin, ymin = 3, 4
xmax, ymax = 7, 7


result = liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

if result is not None:
    clipped_x1, clipped_y1, clipped_x2, clipped_y2 = result

    plt.plot([x1, x2], [y1, y2], 'b', label="Original Line")

    plt.plot([clipped_x1, clipped_x2], [clipped_y1,
             clipped_y2], 'r', label="Clipped Line")

    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin,
             ymax, ymax, ymin], 'k', label="Clipping Window")

    plt.legend()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
else:
    print("Line is completely outside the clipping window.")
