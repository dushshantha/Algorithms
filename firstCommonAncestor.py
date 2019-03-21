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

def insertTree(tree, n):
    if not tree:
        return
    if tree.data >= n.data:
        if tree.left:
            insertTree(tree.left, n)
        else:
            tree.left = n
    else:
        if tree.right:
            insertTree(tree.right, n)
        else:
            tree.right = n

def printTree(root):
    if not root:
        return

    printTree(root.left)
    print(root.data)
    printTree(root.right)


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

if __name__ == '__main__':
    l = [1,2,3,4,5,6]
    tree = buildTree(l, 0, len(l) - 1)
    n1 = Node(9)
    n2 = Node(5)

    insertTree(tree, n1)
    insertTree(tree, n2)
    print(l)
    printTree(tree)

    print('Common Ancestor: ' +  str(commonAncestor(tree, n1, n2).data))
