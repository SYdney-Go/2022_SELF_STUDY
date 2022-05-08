#include <stdio.h>

void main()
{
    int input_data = getchar(); /*문자 입력받기*/
    while(getchar() != '\n') /*표준입력버퍼의 모든 입력값의 제거*/
    printf("first input : %c\n", input_data); /*문자 출력하기*/
    
    input_data = getchar();
    while(getchar() != '\n')
    printf("second input : %c\n", input_data);
}