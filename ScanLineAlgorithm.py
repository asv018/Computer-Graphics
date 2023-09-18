import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

def scanline_fill(polygon):
    min_x = min(p[0] for p in polygon)
    max_x = max(p[0] for p in polygon)
    min_y = min(p[1] for p in polygon)
    max_y = max(p[1] for p in polygon)

    
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    image = [[(255, 255, 255)] * width for _ in range(height)]


    fill_color = (255, 0, 0)
    
    for y in range(min_y, max_y + 1):
        intersections = []
        for i, p1 in enumerate(polygon):
            p2 = polygon[(i + 1) % len(polygon)]
            if p1[1] <= y < p2[1] or p2[1] <= y < p1[1]:
                x_inter = int(p1[0] + (p2[0] - p1[0]) * (y - p1[1]) / (p2[1] - p1[1]))
                intersections.append(x_inter)

        intersections.sort()

        for i in range(0, len(intersections), 2):
            x_start = intersections[i]
            x_end = intersections[i + 1]
            for x in range(x_start, x_end + 1):
                image[y - min_y][x - min_x] = fill_color

    return image


polygon = [(50, 50), (200, 100), (150, 200), (100, 150)]
filled_image = scanline_fill(polygon)

plt.imshow(filled_image)
plt.axis('off')
plt.show()
