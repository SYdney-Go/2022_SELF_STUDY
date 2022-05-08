/*short 포인터 이용하여 data 변수를 0x12340412로 변경*/
#include <stdio.h>

void main()
{
    int data = 0x12345678;
    short *p = (short *)&data;
    *p = 0x0412;
    printf("%X\n", data);
}