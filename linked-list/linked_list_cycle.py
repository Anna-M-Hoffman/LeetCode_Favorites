# LINKED LIST CYCLE
# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
# Solved using Floyd's Tortoise and Hare Algorithm (slow and fast pointers)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next: # Fast moves two spaces at a time, so a two checks for null are needed
          slow = slow.next
          fast = fast.next.next 
          if fast == slow: # If the fast pointer catches up to the slow pointer, it must be a cycle
            return True
        return False # The fast pointer reached a Null state
            
