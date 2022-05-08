#include <stdio.h>

void main()
{
    int data = 5, result = 0;

    result = --result && (data = 0); /*--result면 4 && 0으로 result는 0, data=0 부분도 실행되서 0이 된다*/

    printf("data = %d, result = %d\n", data, result);
}