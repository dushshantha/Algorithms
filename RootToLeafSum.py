'''
A number can be constructed by a path from the root to a leaf. Given a binary tree, sum all the numbers that can be constructed from the root to all leaves.
'''

class Node():
    def __init__(self, val, left = None, right = None):
        self.value = val 
        self.left = left
        self.right = right

    
def rootToLeafSum_dfs(root):
    val_list = rootToLeaf(root, 0)
    return sum(val_list)

def rootToLeaf(node, p_val):
    if not node:
        return []
    if node.left == node.right == None:
        return [p_val * 10 + node.value]
    else:
        return rootToLeaf(node.left, p_val * 10 + node.value) + rootToLeaf(node.right, p_val * 10 + node.value)


def rootToLeafSum_bfs(root):
    q = [root]
    prnt = [0]
    total = 0
    while q:
        curr = q.pop(0)
        p_val = prnt.pop(0)
        if curr.left == curr.right == None:
            total += p_val * 10   + curr.value
        else:
            p_val = p_val * 10 + curr.value
            if curr.left:
                prnt.append(p_val)
                q.append(curr.left)
            if curr.right:
                prnt.append(p_val)
                q.append(curr.right)

    return total




n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)
print(rootToLeafSum_dfs(n1))
print(rootToLeafSum_bfs(n1))

print('----')
n1 = Node(1, None, None)
print(rootToLeafSum_dfs(n1))
print(rootToLeafSum_bfs(n1))
