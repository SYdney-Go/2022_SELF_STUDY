#include <stdio.h>

void main()
{
    int step, i;

    for(step=1; step<=9; step++) {
        printf("%d단 입니다\n", step);
        for(i=1; i<=9; i++) {
            printf("%d * %d = %d \n", step, i, step*i);
        }
        printf("\n");
    }
}