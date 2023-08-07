#include <iostream>
using namespace std;

// Function to draw a line using Bresenham's algorithm
void drawLine(int x1, int y1, int x2, int y2)
{
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int incX = (x1 < x2) ? 1 : -1;
    int incY = (y1 < y2) ? 1 : -1;

    int x = x1, y = y1;

    if (dx >= dy)
    {
        int d = 2 * dy - dx;
        while (x != x2)
        {
            // Draw the pixel at (x, y)
            cout << "(" << x << ", " << y << ")" << endl;
            x += incX;
            if (d >= 0)
            {
                y += incY;
                d -= 2 * dx;
            }
            d += 2 * dy;
        }
    }
    else
    {
        int d = 2 * dx - dy;
        while (y != y2)
        {
            // Draw the pixel at (x, y)
            cout << "(" << x << ", " << y << ")" << endl;
            y += incY;
            if (d >= 0)
            {
                x += incX;
                d -= 2 * dy;
            }
            d += 2 * dx;
        }
    }
}

int main()
{
    int x1, y1, x2, y2;
    cout << "Enter the coordinates of the starting point (x1, y1): ";
    cin >> x1 >> y1;
    cout << "Enter the coordinates of the ending point (x2, y2): ";
    cin >> x2 >> y2;

    cout << "Coordinates of the line pixels:" << endl;
    drawLine(x1, y1, x2, y2);
    return 0;
}
