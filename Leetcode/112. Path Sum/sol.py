from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return (self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val))
        

def test():
    # Manually build the tree: [5,4,8,11,null,13,4,7,2,null,null,null,1]
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    # Target sum
    targetSum = 22

    # Solution instance
    solution = Solution()
    
    # Call hasPathSum and print the result
    result = solution.hasPathSum(root, targetSum)
    print(f"Result for targetSum {targetSum}: {result}")  # Expected: True

# Run the test
test()