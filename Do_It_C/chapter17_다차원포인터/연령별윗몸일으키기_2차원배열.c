#include <stdio.h>

void main()
{
    unsigned char limit_table[3] = {4, 2, 3};
    unsigned char count[3][4];
    int age, member, temp, sum;

    /*age=0,1,2*/
    for(age=0; age<3; age++)
    {
        printf("\n%d0대 연령의 윗몸 일으키기 횟수\n", age+2); /*age=2,3,4*/
        /*member<limit_table[0]=4, [1]=2, [2]=3*/
        for(member=0; member<limit_table[age]; member++)
        {
            printf("%dth : ", member+1); /*limit_table[0]=0,1,2,3 ->member=1,2,3,4*/
            scanf("%d", &temp);
            /*count[0][0], count[0][1], count[0][2], count[0][3]
            count[1][0], count[1][1]
            count[2][0], count[2][1], count[2][2]
            count 배열 각각에 입력값을 저장한다.*/
            count[age][member] = (unsigned char)temp;
        }
    }
    
    printf("\n\n연령별 평균 윗몸 일으키기 횟수\n");
    /*age=0,1,2*/
    for(age=0; age<3; age++)
    {
        sum=0;
        printf("%d0대 : ", age+2); /*age+2 = 2,3,4*/
        /*limit_table[0] = 4, limit_table[1] = 2, limit_table[2] = 3*/
        for(member=0; member<limit_table[age]; member++)
        {
            /*sum에 count 배열의 각 값을 더해가기*/
            sum = sum + count[age][member];
        }
        /*limit_table[age]에 들어간 수로 각 age의 총 합을 나누기*/
        printf("%5.2f\n", (double)sum / limit_table[age]);
    }
}