# 1부터 100까지 출력하는 프로그램을 작성하시오.
# 3의 배수일 때는 Fizz를, 5의 배수일때는 Buzz, 3과 5의 공배수일때는 FizzBuzz를 출력합니다.

# 1에서 100까지 출력
for i in range(1, 101):
    # 3과 5의 공배수 먼저 잡아내기
    if (i % 3 == 0) and (i % 5 == 0):
        i = "FizzBuzz"
    # 3의 배수인 경우
    elif i % 3 == 0:
        i = "Fizz"
    # 5의 배수인 경우
    elif i % 5 == 0:
        i = "Buzz"
    print(i, end=' ')  