#include <stdio.h>

/*data 배열의 짝수번 요소에 저장된 값을 합산하는 코드*/
void main()
{
    short data[9] = {4, 6, 9, 8, 7, 2, 5, 1, 3};
    int i, total;

    total = 0;

    for (i=0; i<9; i++)
    {
        if(i%2==1)
        {
            total = total + data[i];
            printf("%d ", total);
        }
    }
    printf("\nTotal : %d\n", total);
}