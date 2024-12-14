class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre_order_traversal(tree):
    if not tree:
        return
    if tree.val:
        print(tree.val, end= " ")
    if tree.left:
        pre_order_traversal(tree.left)
    if tree.right: 
        pre_order_traversal(tree.right)

def in_order_traversal(tree):
    if not tree:
        return
    if tree.left:
        in_order_traversal(tree.left)
    if tree.val:
        print(tree.val, end= " ")
    if tree.right: 
        in_order_traversal(tree.right)

def post_order_traversal(tree):
    if not tree:
        return
    if tree.left:
        post_order_traversal(tree.left)
    if tree.right: 
        post_order_traversal(tree.right)
    if tree.val:
        print(tree.val, end= " ")

if __name__ == '__main__':
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(7)
    tree.right.left = TreeNode(12)
    tree.right.right = TreeNode(20)

    print("Pre-order Traversal")
    print(pre_order_traversal(tree))
    print()

    print("In-order Traversal")
    print(in_order_traversal(tree))
    print()

    print("Post-order Traversal")
    print(post_order_traversal(tree))
    print()