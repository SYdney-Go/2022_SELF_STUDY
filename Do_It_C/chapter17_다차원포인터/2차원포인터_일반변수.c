#include <stdio.h>

void main()
{
    short data = 3;
    /*1차원 포인터 변수 p는 data의 주소를 참조*/
    short *p = &data;
    /*2차원 포인터 변수 pp는 p의 주소를 참조*/
    short **pp = &p;

    printf("[Before  ] data : %d\n", data);

    /*1차원 포인터와 2차원 포인터를 사용해서 값을 수정할 수 있다.*/
    
    /*1차원 포인터 변수 p가 가리키는 주소에 값 4를 보내기*/
    *p = 4;
    printf("[Use *p  ] data : %d\n", data);

    /*2차원 포인터 변수가 가리키는 1차원 포인터가 가리키는 주소에 값 5를 보내기*/
    **pp = 5;
    printf("[Use **pp] data : %d\n", data);
}