#include <stdio.h>
#include <string.h>

void main()
{
    char data[10] = {'H', 'e', 'l', 'l', 'o', 0,};
    char result[20];

    strcpy(result, data);
    strcat(result, " world!");

    printf("%s + \" world!\" = %s", data, result);
}