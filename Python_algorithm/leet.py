from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    # 리스트 컨테이터 타입 생성 : list[type] = []
    # Optional : None을 허용하는 컨테이너 타입
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1, list2: None을 허용하는 ListNode
        # 결과적으로는 list1과 list2 모두 self.val=0, next=None을 가지는 ListNode 인스턴스가 되었다.
        # cur과 dummy로 ListNode 객체 생성
        cur = dummy = ListNode()
        
        while list1 and list2: # ? : ListNode가 False라는건, val과 next 모두가 None이란건가
            if list1.val < list2.val: # list의 값을 비교
                # 더 작은 값을 가진 ListNode를 cur.next에 저장한다.
                cur.next = list1
                # 그리고 list1은 list1.next로 갱신한다. 근데 list1.next는 아직 None 아닌가??
                # cur ListNode는 list1 ListNode로 갱신한다.
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
        
        # 아직 몇 개 남은 애들 cur.next에 붙이기
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next