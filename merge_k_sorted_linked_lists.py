# MERGE K SORTED LINKED LISTS
# You are given an array of k linked lists lists, 
# where each list is sorted in ascending order.

# Return the sorted linked list that is the result of 
# merging all of the individual linked lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None # No lists to process

        while len(lists) > 1: # There are 2+ lists to merge
            mergedLists = []
            for i in range(0, len(lists), 2): # Take two lists at a time
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None 
                # makes l2 None if i + 1 is out of bounds
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists # This updates the input to the while and for loops
            # Ex lists = [[1][4][3]] now beccomes lists = [[1,3][4]]
        return lists[0] # At this point lists contains one list all sorted


        
    def merge(self, l1, l2):
        dummy = ListNode() # head
        tail = dummy # tail is set to head originally

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 # Only insert node from l1 at the end
                l1 = l1.next # Move pointer to next node in l1
            else:
                tail.next = l2 # Insert node from l2 at end
                l2 = l2.next # Move pointer to next node in l2

            tail = tail.next # Move tail pointer to last node just added 
            # for the next iteration
        
        if l1: # Insert the non-empty list at the end of the list
            tail.next = l1 
        if l2:
            tail.next = l2

        return dummy.next # Return the head of the merged list
