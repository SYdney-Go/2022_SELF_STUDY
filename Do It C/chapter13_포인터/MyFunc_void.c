#include <stdio.h>

/*세가지 주소 타입 중 어떤걸 사용할지 flag로 설정*/
void MyFunc(void *p, char flag)
{
    if(flag == 0) *(char *)p = 1;
    else if(flag == 1) *(short *)p = 1;
    else *(int *)p = 1;
}

void main()
{
    short data = 5;
    MyFunc(&data, 1);
}