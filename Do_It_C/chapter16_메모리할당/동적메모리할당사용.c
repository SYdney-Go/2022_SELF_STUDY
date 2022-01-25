#include <stdio.h>
#include <malloc.h>

void main()
{
    char *p_name; /*p_name이라는 포인터 변수 생성*/
    /*포인터 변수에 32바이트 동적 메모리 할당*/
    p_name = (char *)malloc(32);

    /*만약 그렇게 할당받은 메모리가 정상적인 경우*/
    if(p_name != NULL)
    {
        /*사용자로부터 이름 입력 받기*/
        printf("Your name : ");
        /*입력받은 이름을 p_name 포인터 변수가 가리키는 동적 메모리 안에 할당*/
        fgets(p_name, 32, stdin);

        /*동적 메모리 안의 이름을 불러와서 출력*/
        printf("Hi ~%s \n", p_name);
        /*포인터 변수 안의 동적 메모리 해제*/
        free(p_name);
    }
    /*만약 메모리 할당이 정상적이지 않은 경우 에러 메세지 출력*/
    else
    {
        printf("Memory allocation error!");
    }
}