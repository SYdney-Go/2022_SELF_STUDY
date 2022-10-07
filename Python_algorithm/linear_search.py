# 찾는 값의 위치 반환
data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
found = False

for i in range(len(data)):
    if data[i] == 40:
        found = True
        print(i)
        break
    
if not found:
    print("Not found")