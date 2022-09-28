#include <stdio.h>

void main()
{
    int data = 5, result = 0;

    result = data++ + 2; /*단항연산자 먼저 -> 일반 연산, 이때 단항 연산자의 경우 변수 값 자체 변화*/
    printf("data = %d, result = %d\n", data, result);
}