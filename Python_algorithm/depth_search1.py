# 전위 순회
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], 
        [], [], [], [], [], [], [], []]

def search(pos):
    # 일단 왼쪽 끝값부터 조지기 때문에 print로 먼저 출력
    print(pos, end = " ")
    # 마지막 값으로 가서 거기서부터 tree를 조질거기 때문에 먼저 재귀로 마지막까지 간다!
    # search(n)을 다음 pos로 전달
    for i in tree[pos]:
        search(i)

search(0)