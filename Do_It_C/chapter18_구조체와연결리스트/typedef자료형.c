#include <stdio.h>

/*unsigned short int형을 US로 정의한다*/
typedef unsigned short int US;

void main()
{
    unsigned short int data = 5;
    US temp; /*unsigned short int temp와 같다.*/

    temp = data;
    printf("temp = %d\n", temp);
}