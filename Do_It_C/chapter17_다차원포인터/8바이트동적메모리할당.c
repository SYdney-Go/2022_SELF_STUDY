#include <stdio.h>
#include <malloc.h>

void GetMyData(int **q)
{
    /*포인터변수의 q는 1차원 포인터 p변수의 주소를 가리킨다*/
    /*q에 동적으로 할당된 메모리를 대입
    이 값은 p 변수의 주소를 따라 포인터변수 p가 가리키는 값이 된다*/
    *q = (int *)malloc(8);
}


void main()
{
    /*포인터 변수 p 설정*/
    int *p;
    /*포인터변수를 가리키는 주소 전달*/
    GetMyData(&p);
    /*그 주소가 가리키는 동적 메모리로 이동하여 값 전달*/
    *p = 5;
    /*동적 메모리 해제*/
    free(p);
}