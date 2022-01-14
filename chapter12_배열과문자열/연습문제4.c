#include <stdio.h>

void main()
{
    char data[12] = {0, };
    data[5] = 1;
    data[11] = 2;
    int i, row, col;

    for(i=0; i<12; i++)
    {   
        col = i % 3 + 1;
        row = i / 4 + 1;

        if(data[i]==1) printf("%d행 %d열은 검은돌 입니다. \n", row, col);
        else if (data[i]==2) printf("%d행 %d열은 흰돌 입니다. \n", row, col);
        else printf("%d행 %d열은 돌이 없습니다.\n", row, col);

    }
}