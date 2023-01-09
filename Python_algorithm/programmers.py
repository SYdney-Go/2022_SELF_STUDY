class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
    
    def __repr__(self):
        if self.nodeCount == 0:
            return "LinkedList : empty"
        
        s = ""
        curr = self.head
        while curr:
            s += repr(curr.data)
            s += " -> "
            curr = curr.next
        return s

    def getAt(self, pos):
        # index 범위 밖에 있을 때
        if pos < 1 or pos > self.nodeCount:
            return None
        
        # 시작을 1부터
        i = 1
        curr = self.head # 현재 위치 정하기
        while i < pos:
            curr = curr.next
            i += 1
        return curr
    
    def insertAt(self, pos, newNode):
        # 가능한 index 범위 밖에 있을 때
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        
        # 맨 앞에 삽입하는 경우
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            # 맨 마지막에 삽입하는 경우 -> prev = tail
            if pos == self.nodeCount+1:
                prev = self.tail
            # 중간에 삽입하는 경우 -> prev = 넣으려는 위치 앞의 노드
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode
        
        # 먄약 맨 마지막에 삽입하는 경우, tail을 newNode로 수정
        if pos == self.nodeCount + 1:
            self.tail = newNode
        
        self.nodeCount += 1
        return True
    
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        if pos == 1:
            value = self.head.data
            self.head = self.head.next
        
        # 만약 길이가 1인데 그 위치의 값을 빼면 tail은?
        else:
            prev = self.getAt(pos - 1)
            if pos == self.nodeCount:
                value = self.tail.data
                self.tail = prev
                prev.next = None
                
            else:
                curr = prev.next
                value = curr.data
                prev.next = curr.next
        
        self.nodeCount -= 1
        return print(value)
    
    def getLength(self):
        return self.nodeCount
    
    def traverse(self):
        result = []
        curr = self.head
        while curr:
            result += [curr.data]
            curr = curr.next
        return result

    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail  = L.tail
        self.nodeCount += L.nodeCount
        return L
        
if __name__ == "__main__":
    A = Node(10)
    B = Node(30)
    C = Node(50)
    D = Node(100)
    
    L = LinkedList()
    L.insertAt(1, A)
    L.insertAt(2, B)
    L.insertAt(3, C)
    L.insertAt(4, D)
    
    print(L.traverse())
    L.popAt(2)
    L.popAt(3)
    L.popAt(1)
    print(L.traverse())