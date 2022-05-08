#include <stdio.h>
#include <malloc.h>

void main()
{
    /*연령별 인원 수를 저장할 배열*/
    unsigned char limit_table[3];
    /*연령별 윗몸 일으키기 횟수를 저장할 포인터 배열?*/
    unsigned char *p[3];

    int age, member, temp, sum;

    /*age = 0,1,2*/
    for(age=0; age<3; age++)
    {
        printf("\n%d0대 연령의 윗몸 일으키기 횟수\n", age+2); /*age=2,3,4*/
        printf("이 연령대는 몇 명입니까?");
        scanf("%d", &temp);

        /*각 연령대 별 사람 수를 limit_table의 값으로 저장*/
        /*limit_table[age] = {입력된 사람수1, 입력된 사람수2, 입력된 사람수3}*/
        limit_table[age] = (unsigned char)temp;

        /*p[0] = limit_table[0]크기, 즉 입력 사람 수 만큼의 동적 메모리를 할당받는다*/
        p[age] =(unsigned char *)malloc(limit_table[age]);
        /*member = 입력 사람수*/
        for(member=0; member<limit_table[age]; member++)
        {
            printf("%dth : ", member+1);
            /*윗몸 일으키기 횟수를 입력 받는다!*/
            scanf("%d", &temp);
            /*p[age] = limit_table[age]을 가리키는 포인터이므로, 
            +member면 주소상 limit_table[age][member]에 값을 저장한다고 생각해도 될듯...*/
            *(p[age] + member) = (unsigned char)temp;
        }
    }


    printf("\n\n연령별 평균 윗몸 일으키기 횟수\n");
    /*age=0,1,2*/
    for(age=0; age<3; age++)
    {
        sum = 0;
        printf("%d0대 : ", age+2); /*age=2,3,4*/
        /*member=limit_table[0,1,2]에 저장된 수만큼*/
        for(member=0; member<limit_table[age]; member++)
        {
            /*limit_table[age][member]에 저장된 값을 가리키는 포인터*/
            sum = sum + *(p[age] + member);
        }
        printf("%5.2f\n", (double)sum / limit_table[age]);
        /*각 age의 입력 사람 수만큼 할당된 동적 메모리를 해제한다.*/
        free(p[age]);
    }
}