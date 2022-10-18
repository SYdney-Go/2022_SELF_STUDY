class Node:
    def __init__(self, value=None, next=None, pre=None):
        self.value = value
        self.next = None
        self.pre = None
        
def head_to_tail(head_node):
    print("Head_to_tail")
    # while을 위한 초깃값 미리 설정
    # 이게 꼭 있어야 None의 고통에서 벗어날 수 있다...
    # head_node = head_node.next
    while head_node:
        print(head_node.value)
        head_node = head_node.next
   
def tail_to_head(tail_node):  
    print("Tail_to_head")
    while tail_node:
        print(tail_node.value)
        tail_node = tail_node.pre
    

if __name__ == "__main__":
    
    example_list = [1, 2, 3, 4, 5]
    head_node = cur = Node()
    
    while example_list:
        cur.next = Node(example_list.pop(0))
        tail = cur
        cur = cur.next
        cur.pre = tail
        print(cur.value)
    
    head_to_tail(head_node.next)
    tail_to_head(tail)