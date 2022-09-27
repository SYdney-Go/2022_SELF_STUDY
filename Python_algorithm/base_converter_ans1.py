# 10진수를 2진수로 변환하기

number = int(input("Number : "))
result = ''

while number > 0:
    result  = str(number % 2) + result
    number = number // 2

print(result)