#include <stdio.h>
#define MAX_COUNT 5

void main()
{
    int num[MAX_COUNT], count = 0, sum = 0, i;

    /*5보다 작은 count가 열심히 돌아가면서 입력을 받는다. -> 최대 다섯번 덧셈 가능*/
    while(count<MAX_COUNT)
    {
        printf("숫자를 입력하세요 (9999를 누르면 종료) : ");
        scanf("%d", num + count); /*&num[count]와 같은 의미로 입력값을 각 배열에 넣겠다!*/
        if(num[count] == 9999) break;
        count++; /*count의 1증가 -> 한칸 옆 배열로 이동*/
    }

    /*다 채워진 num배열 내부의 값을 다 더해보자*/
    /*위에서 구해진 총 수 입력의 횟수만큼*/
    for(i=0; i<count; i++)
    {
        /* i[1]부터는 + 기호 출력*/
        if(i>0) printf(" + ");
        /*각 i[i] 값의 출력*/
        printf(" %d ", num[i]);
        /*그렇게 구해진 값들을 더해가기*/
        sum = sum + num[i];
    }
    /*총 합의 결과 출력 */
    printf(" = %d\n", sum);
}