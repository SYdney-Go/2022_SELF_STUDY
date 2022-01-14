#include <stdio.h>

void main()
{
    /*한번에 하나의 문자만 입력 받고 싶은데, 문제는 하나 입력 후 엔터를 누르면 그 엔터를 입력 문자로 인식*/
    int input_data;
    input_data = getchar();
    printf("first input : %c\n", input_data);
    input_data = getchar();
    printf("second input : %c\n", input_data);
}