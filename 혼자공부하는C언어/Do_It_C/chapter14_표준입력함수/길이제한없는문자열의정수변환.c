#include <stdio.h>
#include <string.h>

void main()
{
    int pos_num = 1, num = 0, i, count;
    char num_string[4] = "123";
    /*문자열의 길이를 구하기*/
    count = strlen(num_string);

    /*i= 0~문지열의 길이-1만큼 = 문자열길이-1만큼 10을 곱하기*/
    for(i=0; i<count-1; i++) pos_num = pos_num * 10;

    /*문자열의 길이만큼 연산 반복하기*/
    for(i=0; i<count; i++)
    {
        /* + 각 자리수의 수 * 자리수 */
        num = num + (num_string[i]-'0') * pos_num;
        pos_num = pos_num/10;
    }
    printf(" %s -> %d\n", num_string, num);
}