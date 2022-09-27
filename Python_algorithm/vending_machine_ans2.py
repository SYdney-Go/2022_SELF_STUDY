# 투입된 금액을 확인하고, 거스름돈을 돌려주는 문제
# 이때 거스름돈의 단위를 최대로 한다.

# 답안 예시 2. 리스트와 반복문으로 프로그램 간단하게 만들기
insert_price = input("INSERT : ")
product_price = input("PRODUCT : ")
change =  int(insert_price) - int(product_price)

coin = [10000, 5000, 1000, 500, 100, 50, 10, 1]

for i in coin:
    r = change // i
    change = change % i
    print(i, " : ", r)