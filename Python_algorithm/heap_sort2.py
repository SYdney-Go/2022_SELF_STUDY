# 범용 힙의 구현
def heapify(data, i):
    left = 2 * i + 1
    right = 2 * i + 2
    size = len(data) - 1
    min = i
    # 왼쪽 아래가 작은 경우
    if left <= size and data[min] > data[left]:
        min = left
     # 오른쪽 아래가 작은 경우
    if right <= size and data[min] > data[right]:
        min = right
    # 먄약 최소값 기준이 바뀐 경우 교환
    if min != i:
        data[i], data[min] = data[min], data[i]
        # 해당 반복
        heapify(data, min)
 
        
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 힙 구성
for i in reversed(range(len(data) // 2)): # 4, 3, 2, 1, 0
    heapify(data, i)
print(data)

# 힙 정렬 실행
sorted_data = []
for _ in range(len(data)):
    # 마지막 노드와 루트 노드를 교체
    data[0], data[-1] = data[-1], data[0]
    # 맨 마자막 노드, 즉 루트 노드가 꺼내진다.
    sorted_data.append(data.pop())
    # 꺼내진 데이터를 heapify 함수로 보내서 재구성
    heapify(data, 0)
    
print(sorted_data)