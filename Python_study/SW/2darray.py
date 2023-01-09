n, m = map(int, input().split())

mylist = [0 for _ in range(n)]

for i in range(n):
    mylist[i] = list(map(int, input().split()))
    
print(mylist)