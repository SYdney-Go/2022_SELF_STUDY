#include <stdio.h>

void main()
{
    int num = 0, count = 0;
    char num_string[4] = '123';
    
    /*문자열이 끝날때까지 반복*/
    while(num_string[count] != 0)
    {
        /*자리수-1*10만큼을 제곱 + 계속해서 아래 자리수 더해가기*/
        num = num * 10 + (num_string[count] - '0');
        count++;
    }
    printf(" %s -> %d\n", num_string, num);
}