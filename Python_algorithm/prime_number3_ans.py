import math, time

NUM = 1000

def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(math.sqrt(n))
    
    data = [i + 1 for i in range(2, n, 2)] # 일단 짝수 날린 값
        
    while limit >= data[0]: #홀수들을 리스트에서 돌리면서
        prime.append(data[0])
        data = [j for j in data if j % data[0] != 0] # 앞의 값으로 나눠지는 뒤의 값들을 빼기
    
    return prime + data

start = time.time()
get_prime(NUM)
end = time.time()

print(f"{end - start:.5f} sec") #0.00023 sec