#include <stdio.h>

void main()
{
    int data =5, temp = 0;
    /*주소 변경 : data의 주소를 p에 전달하고 이를 const로 고정*/
    int *const p = &data;
    /*p주소에 3이라는 값 전달*/
    *p = 3;
    /*temp의 주소를 p로 전달하려고 해도 p는 이미 const로 고정되어 변경 안됨 -> 에러*/
    p = &temp;
}