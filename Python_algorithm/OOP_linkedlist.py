class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def __str__(self):
        return f"Node({self.value})"
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        
    def __str__(self):
        if not self.head:
            return "The list is empty"
        
        list_str = ""
        cur = self.head
        while cur: 
            list_str += f"{cur.value} -> "
            cur = cur.next
        list_str += "End of List"
        return list_str
    
    def build(self, data):
        if self.head:
            return RunTimeError("The list already has values. Trye adding to the list, instead")
    
        self.head = cur = Node(0)
        while data:
            cur.next = Node(data.pop(0))
            cur = cur.next
            if cur.next == None:
                tail = cur
        self.head = self.head.next
        return
    
    def search(self, value):
        idx = 0
        self.head = cur = Node(0)
        while data:
            cur.next = Node(data.pop(0))
            cur = cur.next
            if cur.value == value:
                return idx
            idx += 1
        return -1
            
            
    
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    linkedlist = LinkedList()
    linkedlist.build(data)
    print(linkedlist)