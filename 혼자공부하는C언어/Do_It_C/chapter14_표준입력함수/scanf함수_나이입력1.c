#include <stdio.h>

void main()
{
    int num = 0;
    while(1) /*무한히 물어보겠다!*/
    {
        printf("input age : ");
        scanf("%d", &num); /*나이 입력을 받는다.*/

        if(num>0 && num <= 130) /*나이가 정상 범위이면 탈출*/
        {
            break;
        }
        else /*나이가 정상 범위가 아니면 나갈 수 없다...*/
        {
            printf("Incorrect Age!! \n");
        }
    }
    printf("your age : %d\n", num);
}