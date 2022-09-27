#include <stdio.h>

void main()
{
    int pos_num = 100, num = 0, i, temp_num;
    char num_string[4] = "123";

    for(i=0; i<3; i++) /*i=0~2까지*/
    {
        temp_num = num_string[i] -'0'; /*문자열에서 숫자열로 하나씩 변환*/
        num = num + temp_num * pos_num; /*0+백의자리*100, +십의자리*10, +일의자리*1*/
        pos_num = pos_num / 10; /*pos_num = 100, 10, 1*/
    }
    printf(" %s -> %d\n", num_string, num);
}