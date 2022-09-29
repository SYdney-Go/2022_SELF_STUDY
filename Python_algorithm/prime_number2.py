from math import sqrt

num = int(input("NUMBER : "))


def is_prime(n):
    prime = True
    num_sq = int(sqrt(n))
    for i in range(2, num_sq+1):
        if n % i == 0:
            prime = False
    return prime

for i in range(2, num+1):
    if is_prime(i) :
        print(i, end= " ")