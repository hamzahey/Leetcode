'''
203. Remove Linked List Elements
Solved
Easy
Topics
Companies
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head , val: int) :
        # Base case: empty list
        if not head:
            return None
        
        # Recursively remove elements from the rest of the list
        head.next = self.removeElements(head.next, val)
        
        # If current node's value matches, skip it
        if head.val == val:
            return head.next
        else:
            return head

    def printList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

# Create linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

print("Original Linked List:")
solution = Solution()
solution.printList(head)

# Remove elements with value 6
head = solution.removeElements(head, 6)

print("Linked List after removing 6:")
solution.printList(head)