tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], 
        [], [], [], [], [], [], [], []]
data = [0]

while len(data) > 0:
    # pos는 data에서 0부터 하나씩 꺼내온다.
    # pos로 마지막까지 계속 값을 꺼내온다.
    pos = data.pop(0)
    print(pos, end = ' ')
    for i in tree[pos]:
        # 동시에 pos는 tree에서 하나씩 꺼내올 수 있도록 한다.
        # tree의 값을 순서대로 data에 append 한다.
        # 나중에 tree의 값을 다 꺼냈을 때도 문제가 안되게 공백 리스트를 붙인다.
        data.append(i)