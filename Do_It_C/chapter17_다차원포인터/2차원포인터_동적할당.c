#include <stdio.h>
#include <malloc.h>

void main()
{
    /*2차원 포인터 pp 설정*/
    short **pp;
    /*pp에 2차원 동적 메모리 주소를 할당*/
    pp = (short **)malloc(sizeof(short *));
    /*pp가 가리키는 곳에 1차원 동적 메모리 주소를 할당*/
    *pp = (short *)malloc(sizeof(short));

    /*pp가 가리키는 주소로 10을 보내기*/
    /*pp의 2차원 동적 메모리 주소가 가리키는 1차원 동적 메모리 주소로 가서 10대입*/
    **pp = 10;
    printf("**pp : %d\n", **pp);
    /*1차원 동적 메모리 주소를 먼저 해제*/
    free(*pp);
    /*그 뒤에 2차원 동적 메모리 주소를 해제*/
    free(pp);
} 