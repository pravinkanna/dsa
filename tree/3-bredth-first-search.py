from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(node):
    if not node:
        return
    queue = deque([node])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if(node.left):
            queue.append(node.left)
        if(node.right):
            queue.append(node.right)

def build_tree():
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(7)
    tree.right.left = TreeNode(12)
    tree.right.right = TreeNode(20)
    return tree

if __name__ == '__main__':
    tree = build_tree()

    print("BFS:", end=" ")
    bfs(tree)
