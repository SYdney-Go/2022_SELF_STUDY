#include <stdio.h>

void main()
{
    /*data의 크기는 4바이트 int*/
    int data = 0x12347856, i;
    /*포인터의 크기는 1바이트 char, data주소에서 1바이트씩 받아오기...*/
    char *p = (char *)&data;

    for(i = 0; i<4; i++)
    {
        printf("%X ", *p);
        p++;
    }
}