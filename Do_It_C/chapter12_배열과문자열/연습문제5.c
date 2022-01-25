#include <stdio.h>

void main()
{
    int data[7] = {6, 3, 9, 7, 2, 4, 1};
    int temp, i, j;

    printf("정렬 전 : ");
    for(i=0; i<7; i++) printf("%d, ", data[i]);

    /*비교할 두 인덱스의 범위를 반복으로 지정*/
    for(i=0; i<6; i++) /*i = 0,1,2,3,4,5*/
    {
        for(j=i+1; j<7; j++) /*j = 1,2 3,4,5,6*/
        /*i=0, j=1,2,3,4,5,6*/
        {
            if(data[i] > data[j])
            {
                temp = data[i];
                data[i] = data[j];
                data[j] = temp;
            }
        }
    }
    printf("\n정렬 후 : ");
    for(i=0; i<7; i++) printf("%d, ", data[i]);
}