// #include <graphics.h>
#include <bits/stdc++.h>
#include <stdio.h>
#include <conio.h>

void drawEllipse(int xc, int yc, int a, int b)
{
    int x = 0, y = b;
    int a_squared = a * a;
    int b_squared = b * b;
    int delta_a_squared = 2 * a_squared;
    int delta_b_squared = 2 * b_squared;
    int p;

    while (y >= 0)
    {
        putpixel(x + xc, y + yc, WHITE);
        putpixel(-x + xc, y + yc, WHITE);
        putpixel(x + xc, -y + yc, WHITE);
        putpixel(-x + xc, -y + yc, WHITE);

        p = b_squared + (a_squared * (1 - 2 * y));
        if (p > 0)
        {
            y--;
            p -= delta_a_squared * y;
        }

        x++;
        p += b_squared * (2 * x + 1);
    }
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\Turboc3\\BGI");

    int xc, yc, a, b;
    printf("Enter the center coordinates (xc yc): ");
    scanf("%d %d", &xc, &yc);
    printf("Enter the semi-major axis (a): ");
    scanf("%d", &a);
    printf("Enter the semi-minor axis (b): ");
    scanf("%d", &b);

    drawEllipse(xc, yc, a, b);

    getch();
    closegraph();
    return 0;
}
