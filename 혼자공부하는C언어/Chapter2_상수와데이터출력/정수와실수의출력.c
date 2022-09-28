#include <stdio.h>

int main(void)
{
    printf("%d\n", 10);
    printf("%lf\n", 3.4); //소숫점6자리까지 출력
    printf("%f\n", 3.4);  //그냥 f가 lf인가보다.
    printf("%.1lf\n", 3.45); //소숫점첫째자리까지 출력 (반올림)
    printf("%.10lf\n", 3.4); //소숫점10자리까지 출력                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    printf("%d과 %d의 합은 %d입니다.\n", 10, 20, 10+20);
    printf("%.1lf - %.1lf = %.1lf\n", 3.4, 1.2, 3.4-1.2);

    return 0;
}