# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode):
        my_list = []
        
        if not root:
            return my_list
                
        # Add root value
        my_list.append(root.val)
        
        # Recursively get left subtree values and extend to my_list
        my_list.extend(self.preorderTraversal(root.left))
        
        # Recursively get right subtree values and extend to my_list
        my_list.extend(self.preorderTraversal(root.right))
        
        return my_list

# Example to test the code
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

    # Create an instance of Solution
    solution = Solution()
    
    # Perform preorder traversal
    result = solution.preorderTraversal(root)
    
    # Print the result
    print("Preorder Traversal:", result)