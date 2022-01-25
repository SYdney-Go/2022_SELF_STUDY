#include <stdio.h>

void main()
{
    int data = 5, result = 0;

    result = result-- && (data=0); 
    /* 후위형은 연산후 결과 변경, 0&& 이다보니 뒤는 또 안돌아가서 data = 5*/
    /*result = 0 -> -1 -> 전체 결과로 다시 지정*/
    printf("data = %d, result = %d", data, result);
} 