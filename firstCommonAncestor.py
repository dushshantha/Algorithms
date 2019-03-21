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

def isInTree(root, n):
    if not root:
        return False
    if  n == root:
        return True

    return (isInTree(root.left, n) or isInTree(root.right, n))

    

def commonAncestor(root, n1, n2):
    if not ( isInTree(root, n1) and isInTree(root, n2)):
        return None

    if n1 == root or n2 == root:
        return root

    n1_in_left = isInTree(root.left, n1)
    n2_in_left = isInTree(root.left, n2)

    if n1_in_left != n2_in_left:
        return root

    if n1_in_left and n2_in_left:
        return commonAncestor(root.left, n1, n2)
    else:
        return commonAncestor(root.right, n1, n2)


