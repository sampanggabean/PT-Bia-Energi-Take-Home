def calculateMaxDepth(n):
    if n is None:
        return 0
    if n.left is None and n.right is None:
        return 1
    return 1 + max(calculateMaxDepth(n.left), calculateMaxDepth(n.right))

class Node:
    def __init__(self):
        self.left = None
        self.right = None

n = Node()
n.left = Node()
n.right = Node()
n.left.left = Node()
n.right.right = Node()
n.right.right.right = Node()

print(calculateMaxDepth(n))