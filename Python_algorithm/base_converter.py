# 10진수를 2진수로 변환하기

number = int(input("Number : "))
two_base = []

while number > 0 :
    r_number = number % 2
    number = number // 2
    two_base.append(str(r_number))

if number == 1:
    two_base.append("1")

two_base.reverse()
print("".join(two_base))
