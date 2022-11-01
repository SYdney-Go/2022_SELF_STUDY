# # SLL 복습

# from tkinter import N


# class SLL_Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = None
        
#     def __str__(self):
#         next_pointer = " -> "if self.next else " "
#         return f"{self.value}{next_pointer}"

# node1 = SLL_Node(1)
# node2 = SLL_Node(2)
# node1.next = node2

# # my 출력
# head = node1

# while head:
#     print(head.__str__(), end=" ")
#     head = head.next
    
# # 재귀 출력
# def recursive_traverse(head):
#     if head == None:
#         return "\nEnd of List"
#     return head.__str__() + recursive_traverse(head.next)

# head = node1
# print(recursive_traverse(head))

# # while loop 실행
# def while_traverse(head):
#     if head == None:
#         head = SLL_Node("End of List")
#     while head:
#         print(head, end=" ")
#         head = head.next

        
# head = node1
# while_traverse(head)

# # 삽입
# def insert_at(head, idx, value) -> bool:
#     counter = 0
    
#     if not head:
#         return False
#     while head:
#         if counter == idx -1:
#             dummy = head.next
#             head.next = SLL_Node(value, dummy)
#             return True
#         counter += 1
#         head = head.next
#     return False

# head = node1
# insert_at(head, 2, 3)
# while head:
#     print(head.__str__(), end=" ")
#     head = head.next

# DLL
class DLL_Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
        
# 1. 위의 함수로 0번째 인덱스에 새로운 값을 추가하면 False 반환, 고치기...? -> 잘 되는데용....
D_node1 = DLL_Node(1)
D_node2 = DLL_Node(2)
D_node3 = DLL_Node(3)
D_node1.next = D_node2
D_node2.next = D_node3
D_node2.pre = D_node1
D_node3.pre = D_node2

# 2. DLL 삽입 기능 구현하기
def D_insert_at(head, idx, value):
    head_node = head
    counter = 0
    if not head:
        return False
    if idx == 0:
        head.prev = DLL_Node(value, head)
        head = head.prev
    while head:
        pre = head
        if counter == idx-1:
            head.next = DLL_Node(value, head.next, pre)
            head.prev = head
        counter += 1
        print(head.value, end=" ")
        head = head.next
    return False
        
head = D_node1
while head:
    pre_node = head
    print(head.value, end=" ")
    head = head.next
    if head != None:
        head.prev = pre_node
print("\n===========================")

# ------------------
head = D_node1
D_insert_at(head, 3, 4)