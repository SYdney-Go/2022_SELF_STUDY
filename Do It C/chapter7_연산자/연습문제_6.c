#include <stdio.h>

void main()
{
    int data = 5, result = 0;

    result = data!=5 && (data = 0); /*0&&0이므로 result 는 0, 그리고 data의 값은 안변했다... 왜지?ㅜㅜ*/
    /*대박, 애초에 && 앞이 F니까 뒤를 안돌린거구나 */
    printf("data = %d, result = %d\n", data, result);
}