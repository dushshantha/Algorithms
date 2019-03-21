class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    

def buildTree(l, start, end):
    if start == end:
        return Node(l[start])
    
    center = (start + end) // 2
    tree = Node(l[center])

    if start < center:
        tree.left = buildTree(l, start, center - 1)
    
    if center < end:
        tree.right = buildTree(l, center + 1, end)
    
    return tree

def printTree(root):
    if not root:
        return
    
    printTree(root.left)
    print(root.data)
    printTree(root.right)

if __name__ == "__main__":
    l = [1,2,3,4,5,6]
    tree = buildTree(l, 0, len(l) - 1)
    print(l)
    printTree(tree)

    l = [2,5,6,8,12,35,56,78]
    tree = buildTree(l, 0, len(l) - 1)
    print(l)
    printTree(tree)
