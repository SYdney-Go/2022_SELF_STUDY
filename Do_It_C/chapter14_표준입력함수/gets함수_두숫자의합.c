#include <stdio.h>

int ArrayToInteger(char string[ ])
{
    int count = 0, num = 0;
    
    /*글자가 더 없고 사용자가 enter키를 누르면 종료*/
    while(string[count] != 0 && string[count] != '\n')
    {
        /*입력된 문자열을 숫자형으로 바꾸기*/
        num = num * 10 + string[count] - '0';
        count++;
    }
    return num;
}

void main()
{
    int first_num, second_num;
    char first_string[16], second_string[16];

    printf("input first number : ");
    fgets(first_string, 16, stdin);
    printf("input second number : ");
    fgets(second_string, 16, stdin);

    /*숫자형으로 바꾼 뒤에 연산 진행*/
    first_num = ArrayToInteger(first_string);
    second_num = ArrayToInteger(second_string);
    printf("%d + %d = %d\n", first_num, second_num, first_num + second_num);
}