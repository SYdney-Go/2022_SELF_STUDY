# 링크드 리스트를 만들고
# 1.  input으로 받은 값이 리스트에 있는지 검색하고 없으면 false return
# 2.  정렬된 리스트가 있다고 가정하고 주어진 인풋은 해당 리스트에 순서에 맞게 삽입하기
# 2-1.만약 동일한 값이 존재한다면, 새로운 값은 그 뒤에 삽입된다.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def search_list(head_node, target_value) -> None:
    node = head_node
    node = node.next
    
    while node.next:
        if node.value == target_value:
            return "찾았다!"
        else:
            node = node.next
    return -1
    
def insert_num(head_node, new_num) -> None:
        node = head_node
        node = node.next
        pre = float("-inf")
        node_insert = Node(new_num)

        while node.next:
            if pre < new_num < node.value:
                # 이 다음의 node 값을 저장
                node_next = node.next
                node.next = node_insert
                node_insert.next = node_next
            pre = node.value
            node = node.next
        return node

if __name__ == '__main__':
    start = None
    head_node = node = Node(start)

    input_list = [1, 2, 3, 4, 5]
    for l in input_list:
        node.next = Node(l)
        node = node.next
    
    target_num = 2
    result = search_list(head_node, target_num)  
    
    new_num = 2.5
    result = insert_num(head_node, new_num)
    
    node = head_node
    while node.next:
        node = node.next
        print(node.value)
