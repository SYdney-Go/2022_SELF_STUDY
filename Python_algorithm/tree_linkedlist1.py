class BinaryTree:
    def __init__(self, root=None, right=None, left=None):
        self.root = root
        self.root_next = None
        self.right = None
        self.left = None
    
    def __str__(self):
        return self.root
    
    def build_tree(self, l:list):
        value = [i for i in l]
        self.root = (value.pop(0))
        
        for v in value:
            if v > self.root:
                self.right = v
                self.root = self.right
            else:
                self.left = v
                self.root = self.left
                
b_cur = B = BinaryTree()
B.build_tree([1, 2, 3, 4, 5])
while b_cur.right and b_cur.left:
    print(b_cur.__str__())