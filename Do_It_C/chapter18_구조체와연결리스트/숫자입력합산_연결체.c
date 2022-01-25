#include <stdio.h>
#include <malloc.h>

typedef struct node
{
    int number;
    struct node *p_next;
} NODE;


void AddNumber(NODE **pp_head, NODE **pp_tail, int data)
{
    if(NULL != *pp_head)
    {
        /*마지막 노드의 주소값에 p_next의 동적 메모리를 넣고 */
        (*pp_tail)->p_next = (NODE *)malloc(sizeof(NODE));
        /*pp_tail에 next의 주소를 지정??????*/
        **pp_tail = (*pp_tail)->p_next;
    }
    /*맨 첫번째 pp_head 지정*/
    else
    {
        /*pp_head = NODE의 수만큼 동적 메모리 값 넣은 값*/
        *pp_head = (NODE *)malloc(sizeof(NODE));
        *pp_tail = *pp_head; /*pp_head와 tail이 같다.*/
    }
    /*그 뒤에 tail의 number에는 입력 data를 넣는다.*/
    (*pp_tail)->number = data;
    /*그 뒤의 tail의 next는 아직 값이 없으니 NULL을 넣는다.*/
    (*pp_tail)->p_next = NULL;
}


void main()
{
    /*노드 시작과 끝을 기억*/
    NODE *p_head = NULL, *p_tail = NULL, *p;
    int sum = 0, temp; 

    while(1)
    {
        printf("숫자를 입력하세요 (9999를 누르면 종료) : ");
        scanf("%d", &temp);
        if(9999 == temp) break;
        AddNumber(&p_head, &p_tail, temp);
    }

    p = p_head;
    while(NULL != p)
    {
        if(p != p_head) printf(" + ");
        printf(" %d ", p->number);
        sum = sum + p->number;
        p = p->p_next;
    }
    printf(" = %d\n", sum);

    while(NULL != p_head)
    {
        p = p_head;
        p_head = p_head->p_next;
        free(p);
    }
    p_tail = p_head;
}