#include <stdio.h>

void main()
{
    char data[5] = {1, 2, 3, 4, 5};
    int result = 0, i;
    char *p = data; /*배열의 시작 위치를 포인터로 저장*/

    for(i=0; i<5; i++)
    {
        result = result + *p; /*포인터로 저장해둔 시작 위치에서 한 char씩 이동하기 -> 값 하나씩 지정하기*/
        p++;
    }
    printf("data 배열의 각 요소의 합은 %d입니다\n", result);
}