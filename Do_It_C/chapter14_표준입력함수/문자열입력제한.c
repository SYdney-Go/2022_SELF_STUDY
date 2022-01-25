#include <stdio.h>

int GetMyString(char buffer[ ], int limit)
{
    int i;
    for(i=0; i<limit; i++) /*i = 0~9까지 반복*/
    {
        buffer[i] = getchar(); /*입력 받기*/
        if(buffer[i] == '\n') /*만약 배열에 enter가 입력되면*/
        {
            buffer[i] = 0; /*enter 키는 0으로 처리*/
            return 1; 
        }
    }
    /* 10이상의 배열 위치, 즉 글자가 길어진 경우*/
    buffer[i] = 0; /*enter 키는 0으로 처리*/
    while(getchar() != '\n') /*엔터를 입력하면 입력배쉬 초기화*/
    return 0;
}


void main()
{
    char temp[10]; /*1바이트 10칸짜리 배열 temp 생성*/
    int state;
    state = GetMyString(temp, 9); /* 결과값 0과1을 받환 */

    if(state == 1) printf("input : %s\n", temp);
    else printf("input : %s -> out of range\n", temp);
}