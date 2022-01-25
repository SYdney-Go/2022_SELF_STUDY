#include <stdio.h>

void main()
{
    int count = 0;

    while (count < 10) {
        printf("안녕하세요\n");
        count++;
    }
    printf("\"안녕하세요\"가 총 %d번 출력되었습니다.\n", count);
}