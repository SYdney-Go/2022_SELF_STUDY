data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data)):
    # 현재의 요소를 임시 공간에 저장
    temp = data[i]
    j = i - 1
    # 현재 요소 앞의 데이터와의 크기 비교
    while (j >= 0) and (data[j] > temp):
        # 값의 크기를 비교해서 앞으로 한칸씩 당겨서 적절한 위치로 옮기기
        data[j + 1] = data[j]
        j -= 1
    # 적절한 위치에 임시공간에 저장된 값을 이동
    data[j + 1] = temp
    
print(data)