#include <stdio.h>

/*data 배열의 요소 내 가장 큰 값을 찾는 코드*/
void main()
{
    short data[9] = {4, 6, 9, 8, 7, 2, 5, 1, 3};
    int i, max;
    max = 0;

    for(i=0; i<9; i++)
    {
        if(max<data[i]) max = data[i];
    }
    printf("Max : %d", max);
}