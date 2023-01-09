N = int(6)
M = int(9)
A = [2, 7, 4, 1, 5, 3]
A.sort()

count = 0
i = 0
j = N-1

while i < j :
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)