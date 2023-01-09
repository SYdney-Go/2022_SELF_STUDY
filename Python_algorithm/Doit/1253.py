N = int(10)
Result = 0

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N-1
    
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
            
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(Result)