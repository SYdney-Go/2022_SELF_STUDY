#include <stdio.h>

void main()
{
    int m, n;
    for(m=5; m<7; m++) {
        for(n=0; n<3; n++){
            if(m==5 && n==1) goto exit_pos;
            printf("m(%d) - n(%d) \n", m, n);
        }
    }
    exit_pos :
    printf("<end m:%d, n:%d> \n", m, n);
}