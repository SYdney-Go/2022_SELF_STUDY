# 2진수를 10진수로 바꾸기

number = input("NUMBER : ")
base_num = int(input("BASE : "))
result = 0

for i in range(len(number)):
    result += int(number[i]) * (2 ** (len(number) - i - 1))

print(result)