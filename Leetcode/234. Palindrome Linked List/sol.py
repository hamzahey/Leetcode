'''234. Palindrome Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Initialize the pointer that will traverse the list
        front_pointer = head

        def recursively_check(current: ListNode) -> bool:
            nonlocal front_pointer
            # Base case: if we reach the end of the list
            if current is None:
                return True
            
            # Recur on the next node
            is_palindrome = recursively_check(current.next)
            
            # Check the value with the front pointer
            if not is_palindrome:
                return False
            
            is_equal = (current.val == front_pointer.val)
            
            # Move the front pointer forward
            front_pointer = front_pointer.next
            
            return is_equal

        return recursively_check(head)

# Example usage:
# Creating the linked list for input [1, 2, 2, 1]
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

# Creating an instance of Solution and checking if the linked list is a palindrome
sol = Solution()
print(sol.isPalindrome(head))  # Output: True

# Creating another linked list for input [1, 2]
head2 = ListNode(1, ListNode(2))
print(sol.isPalindrome(head2))  # Output: False
