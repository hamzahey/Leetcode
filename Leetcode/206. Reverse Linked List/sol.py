'''206. Reverse Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head  # base case: empty or single-node list

        new_head = self.reverseList(head.next)
        head.next.next = head  # reverse link
        head.next = None  # remove original link
        return new_head

    def printList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

# Create a sample linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original Linked List:")
solution = Solution()
solution.printList(head)

# Reverse the linked list
head = solution.reverseList(head)

print("Reversed Linked List:")
solution.printList(head)