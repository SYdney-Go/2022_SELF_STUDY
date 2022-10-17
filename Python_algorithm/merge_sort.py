data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 3]

# 병합 정렬
def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    
    # 재귀적 분할 -> 데이터를 계속 나눠가기
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    # 나눠진 데이터를 다시 병합하기
    return merge(left, right)

# 병합
def merge(left, right):
    result = []
    i, j = 0, 0
    
    # 병합 시 작은 값부터 붙여나가기
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
            
    # 나머지 데이터를 정리해서 추가
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result

print(merge_sort(data))