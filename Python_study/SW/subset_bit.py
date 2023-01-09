arr = [3, 6, 7, 1, 5, 4]

n = len(arr) # 원소의 개수

for i in range(1<<n): # 1 << n은 부분집합의 개수 -> 원소의 개수만큼 1을 왼쪽으로 이동해서 비트 연산한 결과
    for j in range(n): # 원소의 수만큼 비트를 비교
        if i&(1<<j): # i의 j 번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=",")
    print()