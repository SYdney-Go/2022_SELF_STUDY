# 에라토스테네스의 체 : 각각의 배수를 제거
from math  import sqrt
import time

NUM = 1000

start = time.time()
num_list = [i for i in range(2, NUM+1)]

for i in range(2, NUM+1):
    for j in range(2, NUM):
        try:
            num_list.remove(i*j)
        except:
            continue

end = time.time()

print(f"{end - start:.5f} sec") # 2.49904 sec