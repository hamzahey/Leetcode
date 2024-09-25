class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)      # Traverse left subtree
        traverse(node.right)     # Traverse right subtree
        result.append(node.val)  # Visit the root (last in postorder)
    
    traverse(root)
    return result

# Example to test the postorder traversal
if __name__ == "__main__":
    # Construct the following binary tree:
    #     1
    #      \
    #       2
    #      /
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    # Perform postorder traversal
    result = postorderTraversal(root)
    
    # Print the result
    print("Postorder Traversal:", result)
