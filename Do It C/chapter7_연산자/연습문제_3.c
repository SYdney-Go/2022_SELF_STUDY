#include <stdio.h>

void main()
{
    int data = 5, result = 0;
    result = data < 4 + 3; /*덧셈 먼저 -> 대소비교 나중에*/
    printf("result = %d, data = %d \n", result, data);
}