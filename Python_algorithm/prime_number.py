# 주어진 수가 소수인지를 판별하는 함수
# 주어진 수의 제곱근 값을 범위로 나눠지는 값이 있는가 Y -> 소수 아님 
from math import sqrt

num = int(input("NUMBER : "))


def is_prime(num):
    prime = True
    num_sq = int(sqrt(num))
    for i in range(2, num_sq+1):
        if num % i == 0:
            prime = False
            print(num, "소수 아님")
    return prime