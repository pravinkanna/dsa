from collections import deque

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def printTree(root):
    if root is None:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)

def insert_recursively(root, val):
    if root is None:
        return BSTNode(val)
    if root.val == val:
        return root
    if root.val < val:
        root.right = insert_recursively(root.right, val)
    else:
        root.left = insert_recursively(root.left, val)
    return root

def insert_iterative(root, val):
    if root is None:
        return BSTNode(val)
    cur = root
    while True:
        if val < cur.val:
            if not cur.left:
                cur.left = BSTNode(val)    
                break
            cur = cur.left
        else:
            if not cur.right:
                cur.right = BSTNode(val)
                break
            cur = cur.right
    return root


def search(root, val, steps=0):
    if root is None:
        print("Not Found", val, "in", steps, "steps")
        return
    if(val == root.val):
        print("Found", val, "in", steps, "steps")
        return
    steps += 1
    if val < root.val:
        search(root.left, val, steps)
    else:
        search(root.right, val, steps)

def search_iterative(root, val):
    cur = root
    steps = 0
    while True:
        if val == cur.val:
            print("Found", val, "in", steps, "steps")
            break
        steps += 1
        if val < cur.val:
            if not cur.left:
                print("Not Found", val, "in", steps, "steps")
                break
            cur = cur.left
        else:
            if not cur.right:
                print("Not Found", val, "in", steps, "steps")
                break
            cur = cur.right

if __name__ == '__main__':
    root = BSTNode(20)
    root = insert_recursively(root, 10)
    root = insert_recursively(root, 15)
    root = insert_recursively(root, 12)
    root = insert_recursively(root, 7)
    root = insert_recursively(root, 5)
    root = insert_recursively(root, 100)
    printTree(root)
    print()

    root2 = BSTNode(20)
    root2 = insert_iterative(root2, 10)
    root2 = insert_iterative(root2, 15)
    root2 = insert_iterative(root2, 12)
    root2 = insert_iterative(root2, 7)
    root2 = insert_iterative(root2, 5)
    root2 = insert_iterative(root2, 100)
    printTree(root2)
    print()

    search(root, 7)
    search_iterative(root2, 7)