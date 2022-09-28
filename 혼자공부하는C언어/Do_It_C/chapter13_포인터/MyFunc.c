#include <stdio.h>

/*전달되는 주소의 형식이 셋 중 하나로 어떤 것인지 모르는 상황일때*/
void MyFunc(char *p_char, short *p_short, int *p_int)
{
    if(p_char != NULL) *p_char = 1;
    else if(p_short != NULL) *p_short = 1;
    else *p_int = 1;
}

void main()
{
    short data = 5;
    /*사용할 값 외의 주소의 형식들은 NULL으로 보낸다.*/
    MyFunc(NULL, &data, NULL);
}