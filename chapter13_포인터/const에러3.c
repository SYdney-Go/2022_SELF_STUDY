#include <stdio.h>

void main()
{
    int data = 5, temp = 0;
    /*주소와 값 모두에 const를 적용*/
    const int *const p = &data;
    /*값 변경 안됨*/
    *p = 3;
    /*주소 변경 안됨*/
    p = &temp;
}