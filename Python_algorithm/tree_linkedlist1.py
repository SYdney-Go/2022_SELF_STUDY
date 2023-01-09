import random

class BinaryTree:
    def __init__(self, root=None, right=None, left=None):
        self.root = root
        self.right = right
        self.left = left
    
    def __str__(self):
        return self.root
    
def build_tree(BT, l:list):

    if not l:
        return
    
    value = l.pop(0)
    
    if BT.root < value:
        if BT.right:
            BT.root = BT.right
            BT.left = None
        BT.right = value
    else:
        if BT.left:
            BT.root = BT.left
            BT.right = None
        BT.left = value
    print("-----------------")
    print(BT.root)
    print(BT.left)
    print(BT.right)      
    return build_tree(BT, l)
        
    
if __name__ == "__main__":
    l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]          
    B = BinaryTree(root=l.pop(0))
    print("네, 제가 바로 귀여운 루트 ",B.__str__()) 
    while l:
        build_tree(B, l)
        
    l_rand = [random.randint(1, 100) for _ in range(100)]
    B_rand = BinaryTree(root=l_rand.pop(0))
    print(l_rand)
    print("네, 제가 바로 귀여운 루트 ",B_rand.__str__()) 
    while l_rand:
        build_tree(B_rand, l_rand)