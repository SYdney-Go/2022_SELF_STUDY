#include <stdio.h>

void main()
{
    int value = 50000;
    double point;

    point = (value >= 10000) ? value * 0.1 : value * 0.05;
    printf("point = %.0f", point);
}