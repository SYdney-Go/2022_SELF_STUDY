# 2진수를 10진수로 바꾸기

number = input("NUMBER : ")
base_num = int(input("BASE : "))
changed_num = 0

for i in range(len(number)):
    site = number[-(i +1)]
    changed_num += (base_num ** i) * int(site)

print(changed_num)
