class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        msg = f"Node ({self.value}) \n\tLeft : {self.left} \n\tRight: {self.right}"
        return msg

b = BinaryTreeNode(5, 1, 2)
print(b)