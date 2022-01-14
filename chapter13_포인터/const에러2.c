#include <stdio.h>

void main()
{
    int data = 5;
    /*data의 주소를 p로 전달, 그리고 이렇게 받은 int p 전체에 const를 취해 값 전체를 고정*/
    const int *p = &data;
    /*값이 고정되어있는 상황에서 p를 변경할 수 없음*/
    *p = 3;
}