#include <stdio.h>

void main()
{
    /*data의 크기는 4바이트 int*/
    int data = 0x12345678, i;
    /*포인터의 크기는 1바이트 char, data주소에서 1바이트씩 받아오기...*/
    char *p = (char *)&data;

    /*주소값의 변경없이 data 변수를 1씩 출력*/
    for(i = 0; i<4; i++)
    {
        /**(p+0) *(p+1) *(p+2) *(p+3) */
        printf("%X ", *(p+i));
    }
}