# 중위 순회
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], 
        [], [], [], [], [], [], [], []]

def search(pos):
    # 자식 노드가 두개 있는 경우
    if len(tree[pos]) == 2:
        # print("case1 search", tree[pos][0])
        search(tree[pos][0]) # 왼쪽 노드로 간다아...
        print(pos, end = " ") # 왼쪽 노드와 오른쪽 노드의 부모노드 출력
        # print("case1 search", tree[pos][1])
        search(tree[pos][1]) # 오른쪽 노드로 간다아...
    # 자식 노드가 하나인 경우
    elif len(tree[pos]) == 1:
        # print("case2 search", tree[pos][0])
        search(tree[pos][0]) # 왼쪽 노드만 조진다아....
        print(pos, end = " ") # 조진 뒤 부모노드 출력
    # 자식 노드가 없는 경우
    else:
        # print("case3")
        print(pos, end = " ") # 현 위치 출력

search(0)