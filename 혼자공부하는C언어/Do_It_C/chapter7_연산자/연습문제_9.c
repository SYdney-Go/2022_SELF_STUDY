#include <stdio.h>

void main()
{
    int data = 5, result = 0;

    result = result-- || (data = 0); 
    /*이미 한쪽이 0이므로 뒤에도 돌아가서 data = 0, result = 0*/
    /*result = 0 -> -1 -> 전체 결과로 다시 지정*/
    printf("data = %d, result = %d\n", data, result);
}