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

def isBST_withInOrderTraversal(root):
    global prev
    if not root:
        return True
    if not isBST_withInOrderTraversal(root.left):
        return False
    if root.data < prev:
        return False
    prev = root.data
    return isBST_withInOrderTraversal(root.right)

def isBST_MinMax(root, min , max):
    if not root:
        return True

    if not isBST_MinMax(root.left, min , root.data):
        return False

    if not min <= root.data < max:
        return False

    return isBST_MinMax(root.right, root.data , max)

if __name__ == '__main__':
    l = [1,4,3,4,5,6]
    prev = -1
    tree = buildTree(l, 0, len(l) - 1)

    print(l)
    printTree(tree)
    print(isBST_withInOrderTraversal(tree))
    print(isBST_MinMax(tree, -1, 100))

    l = [1,2,3,4,5,6]
    prev = -1
    tree = buildTree(l, 0, len(l) - 1)

    print(l)
    printTree(tree)
    print(isBST_withInOrderTraversal(tree))
    print(isBST_MinMax(tree, -1, 100))


    l = [1,2,3,4,5,6,7,8,3,6,8]
    prev = -1
    tree = buildTree(l, 0, len(l) - 1)

    print(l)
    printTree(tree)
    print(isBST_withInOrderTraversal(tree))
    print(isBST_MinMax(tree, -1, 100))
