# 함수사이에 인수 주고받기

# 매개변수에 값이 대입되는 것 -> 참조하는 위치가 바뀐다.
# n과 x의 참조위치가 같게 시작해서 n만 갱신되는 것
def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input("x의 값을 입력하세요 : "))
print(f'1부터 {x}까지 정수의 합은 {sum_1ton(x)}입니다.')