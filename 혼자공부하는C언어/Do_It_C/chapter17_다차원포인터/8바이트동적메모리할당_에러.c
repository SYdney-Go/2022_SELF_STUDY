#include <stdio.h>
#include <malloc.h>

void GetMyData(int *q)
{
    q = (int *)malloc(8);
}

void main()
{
    /*포인터 변수 p 지정*/
    int *p;
    /*함수를 호출해서 p에 동적 메모리 할당...*/
    /*을 시도하나 앞서 p의 주소를 정해주지 않았기 때문에*/
    GetMyData(p);
    /*그 개판인 주소 p에 5 대입 할 수 없다*/
    *p = 5;
    free(p);
}