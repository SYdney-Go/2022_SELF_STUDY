data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 3]

def quick_sort(data):
    if len(data) <= 1:
        return data
    
    # 피벗으로 리스트의 첫번째 요소 사용
    pivot = data[0]
    
    left, right, same = [], [], 0
    
    for i in data:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            same += 1
            
    left = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] * same + right

print(quick_sort(data))