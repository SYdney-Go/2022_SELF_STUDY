data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

change = True
for i in range(len(data)):
    # 요소 교환이 더 안일어나면 종료
    if not change:
        break
    change = False
    for j in range(len(data) - i -1):
        # 만약 요소 교환이 일어나면,
        if data[j] > data[j + 1]:
            data[j] , data[j + 1] = data[j + 1], data[j]
            change = True
            
print(data)