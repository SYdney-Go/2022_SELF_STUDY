# 후위 순회
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], 
        [], [], [], [], [], [], [], []]

def search(pos):
    for i in tree[pos]:
        # 완전 끝으로 갔다가
        search(i)
    # 안에서부터 풀어가면서 출력
    print(pos, end = " ")

search(0)