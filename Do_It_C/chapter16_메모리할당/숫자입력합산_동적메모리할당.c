#include <stdio.h>
#include <malloc.h>

void main()
{
    int *p_num_list, count = 0, sum = 0, limit = 0, i;

    printf("사용할 최대 개수를 입력하세요 : ");
    /*사용자의 입력을 limit의 주소에 할당*/
    scanf("%d", &limit);
    /*할당받은 limit를 int로 변환해서 그만큼의 동적 메모리를 num_list에 할당*/
    p_num_list = (int *)malloc(sizeof(int)*limit);

    /*limit의 수가 count보다 작을때까지 -> 사용자가 입력한 횟수만큼*/
    while(count<limit)
    {
        printf("숫자를 입력하세요 (9999를 누르면 종료) : ");
        scanf("%d", p_num_list + count); /*&p_num_list[count]에 입력값 저장*/
        if(*(p_num_list + count) == 9999) break;
        count++;
    }

    /*구해진 p_num_list의 총합 구하기*/
    for(i=0; i<count; i++)
    {
        if(i>0) printf(" + ");
        printf(" %d ", *(p_num_list + i));
        sum = sum + *(p_num_list + i); /*&p_num_list[i]의 값을 더하기*/
    }
    printf(" = %d\n", sum);
    /*p_num_list에 사용했던 동적 메모리 지우기*/
    free(p_num_list);
}