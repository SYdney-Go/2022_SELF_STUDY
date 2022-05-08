#include <stdio.h>
#include <stdio_ext.h>

void main()
{
    int age = 0;
    while(1)
    {
        printf("input age : ");
        if(scanf("%d", &age) == 0)
        {
             __fpurge(stdin);
            printf("[Enter] digit number!! \n");
        }
        else
        {
            if(age>0 && age<=130)
            {
                break;
            }
            else
            {
                printf("Incorrect Age!! \n");
            }
        }
    }
    printf("your age : %d \n", age);
}