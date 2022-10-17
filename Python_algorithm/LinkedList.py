class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        
        # head에 값이 들어오면
        while node is not None:
            # 데이터 값을 리스트에 붙인다.
            nodes.append(node.data)
            # 그리고 다음 노드를 가리킨다. 
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        


    
if __name__ == '__main__':
    l = LinkedList()
    
    first_node = Node("a")
    l.head = first_node
    
    seconde_node = Node("b")
    third_node = Node("c")
    