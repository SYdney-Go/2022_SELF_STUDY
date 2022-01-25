#include <stdio.h>
#include <malloc.h>

void main()
{
    /*limit_table = 연령별 인원수를 저장*/
    unsigned char *p_limit_table;
    /*연령별 각 인원의 윗몸 일으키기 횟수를 저장*/
    unsigned char **p;
    int age, age_step, member, temp, sum;

    printf("20대부터 시작해서 연령층이 몇 개인가요? : ");
    scanf("%d", &age_step);
    /*p_limit_table = 입력받은 연령층 만큼의 메모리 주소를 가리키는 1차원 포인터 변수*/
    p_limit_table = (unsigned char *)malloc(age_step);
    /*p = 입력 받은 연령층에 사람수만큼 곱한 메모리 주소를 가리키는 2차원 포인터 변수*/
    p = (unsigned char **)malloc(sizeof(unsigned char *) * age_step);

    /*age = 입력받은 연령층 수*/
    for(age=0; age<age_step; age++)
    {
        printf("\n%d0대 연령의 윗몸 일으키기 횟수\n", age+2); /*5개면 2, 3, 4, 5, 6, 7*/
        printf("이 연령대는 몇 명입니까? : ");

        scanf("%d", &temp);
        /*각 연령층의 사람수를 p_limit_table[age]가 가리키는 주소에 대입*/
        /*p_limit_table[0]이 가리키는 주소 = 20대 연령층의 수에 입력수 대입*/
        *(p_limit_table + age) = (unsigned char)temp;

        /*이렇게 *(p_limit_table[age]) = 각 연령대 별 사람수가 된다.*/
        /*p[age] =  각 연령층의 사람 수 만큼의 동적 메모리를 가진다.*/
        *(p + age) = (unsigned char *)malloc(*(p_limit_table + age));
        
        /*p_limit_table+age 는 각 연령대별 사람수이므로 0 ~ 각 연령대별 사람수만큼 반복*/
        for(member=0; member<*(p_limit_table+age); member++)
        {
            printf("%dth : ", member+1);
            scanf("%d", &temp);
            /*p[age][member]라는 위치에 사용자 입력, 즉 윗몸일으키기 횟수를 저장*/
            *(*(p+age) + member) = (unsigned char)temp;
        }
    }
    
    printf("\n\n연령별 평균 윗몸 일으키기 횟수\n");\
    /*age=0부터 연령층 전제만큼*/
    for(age=0; age<age_step; age++)
    {
        sum = 0;
        printf("%d0대 : ", age+2);
        /*p_limit_table[age] 즉, 연령대별 사람수만큼 반복*/
        for(member=0; member<*(p_limit_table+age); member++)
        {   
            /*p[age][member]의 주소가 가리키는 값을 sum에 더해나가기*/
            sum = sum + *(*(p+age) + member);
        }
        printf("%5.2f\n", (double)sum / *(p_limit_table + age));
        free(*(p + age));
    }
    /*2차원 포인터가 가리키는 동적 메모리 해제*/
    free(p);
    /*1차원 포인터가 가리키는 동적 메모리 해제*/
    free(p_limit_table);
}