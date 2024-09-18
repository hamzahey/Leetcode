from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = getHeight(node.left)
            if left_height == -1:
                return -1  # Left subtree is not balanced
            
            right_height = getHeight(node.right)
            if right_height == -1:
                return -1  # Right subtree is not balanced
            
            if abs(left_height - right_height) > 1:
                return -1  # Current node is not balanced
            
            return max(left_height, right_height) + 1
        
        return getHeight(root) != -1

# Helper function to create a binary tree
def create_tree() -> TreeNode:
    # Create nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    
    return root

# Create tree and check if it is balanced
tree_root = create_tree()
solution = Solution()
is_tree_balanced = solution.isBalanced(tree_root)
print(f"The tree is {'balanced' if is_tree_balanced else 'not balanced'}")
