'''
100. Same Tree
Solved
Easy
Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both nodes are None, the trees are the same
        if not p and not q:
            return True 

        # If one is None and the other is not, the trees are not the same
        if not p or not q:
            return False

        # If the values of the current nodes are different, the trees are not the same
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Helper function to create a binary tree from a list of values
def buildTree(values):
    if not values:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in values]
    
    for index in range(len(nodes)):
        node = nodes[index]
        if node:
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            if left_index < len(nodes):
                node.left = nodes[left_index]
            if right_index < len(nodes):
                node.right = nodes[right_index]
    
    return nodes[0]

# Test input p = [1, 2, 3], q = [1, 2, 3]
p_values = [1, 2, 3]
q_values = [1, 2, 3]

p_tree = buildTree(p_values)
q_tree = buildTree(q_values)

# Create a Solution instance
solution = Solution()

# Test the isSameTree function
result = solution.isSameTree(p_tree, q_tree)

# Output the result
print(result)  # Expected output: True
