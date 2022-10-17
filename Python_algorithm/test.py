# 원형 링크드 리스트 정의
class Node():
    def __init__(self, val=None, next=None):
        self.val = None
        self.next = None

def solution(n, m, moles):
    moles = sorted(moles)
    head = cur = Node()
    cur.val = moles[0]
    print(list(head.val))

    for i in range(len(moles)):
        cur.next = cur
        cur.val = moles[i]
    cur.next = head
    print(list(head.val))

    answer = 0
    
    # cur = head
    # while cur.next == head:
    #   print(list(cur.val))
    # cur = head
    # for _ in range(20):
    #     cur.next
    #     print(list(cur.val))
    # return answer

    
s = solution(7, 2, [[7, 5, 6], [2, 1, 10], [6, 6, 6], [2, 2, 10], [3, 2, 10], [5, 5, 6], [8, 6, 6], [3, 1, 10]])