#include <stdio.h>

void main()
{
    int input_data;
    input_data = getchar(); /*문자 입력*/
    getchar(); /*엔터 입력*/
    printf("first input : %c\n", input_data);

    input_data = getchar(); /*문자 입력*/
    getchar(); /*엔터 입력*/
    printf("second input : %c\n", input_data);
}