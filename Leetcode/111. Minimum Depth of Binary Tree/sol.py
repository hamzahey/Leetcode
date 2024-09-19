'''
111. Minimum Depth of Binary Tree
Solved
Easy
Topics
Companies
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    
    # Initialize the queue for BFS
    queue = deque([(root, 1)])  # (node, depth)
    
    while queue:
        node, depth = queue.popleft()
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            return depth
        
        # Add left and right children to the queue if they exist
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

# Example usage:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(minDepth(root))  # Output: 2
