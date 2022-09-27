# 10진수를 2진수로 변환하기

number = int(input("Number : "))
base = int(input("Base : "))
two_base = []

def converter(number, n):
    result = ''
    while number > 0:
        result  = str(number % n) + result
        number = number // n  
    return result

print(converter(number, base))