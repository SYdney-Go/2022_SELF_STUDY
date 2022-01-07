#include <stdio.h>

int ReturnNum()
{
    int num = 5;
    return num;
}

void main()
{   
    int num;
    num = ReturnNum();
    printf("Number = %d\n", num);
}