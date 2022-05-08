#include <stdio.h>

int main(void)
{
    printf("Be happy!\n");
    printf("12345678901234567890\n");
    printf("My\tfriend!\n");
    printf("Goot\bd\tchance\n"); //\b는 한칸 왼쪽으로 삭제
    printf("Cow\rW\a\n"); //\r은 맨 앞으로 이동한다. \a는 벨소리를 낸다.

    return 0;
}