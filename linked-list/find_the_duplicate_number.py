# FIND THE DUPLICATE NUMBER
# You are given an array of integers nums containing n + 1 integers.
# Each integer in nums is in the range [1, n] inclusive.
# Every integer appears exactly once, except for one integer which appears two or more times. 
# Return the integer that appears more than once.
# Solve the problem without modifying the array nums and using O(1) extra space.

#  Floyd's Cycle Detection 
# A slow2 pointer catching up to the slow pointer at the start of the cycle works because...
# p is distance from start of linked list to start of cycle
# x is distance from where fast and slow pointers meet and start of cycle
# c is length of cycle 
# 2(slow) = fast
# 2(p + c - x) = p + 2c - x
# 2p + 2c - 2x = p + 2c - x
# p - x = 0
# p = x

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0 # First position is guaranteed not in loop because range is [1, n]
        
        while True: # Continue looping
            slow = nums[slow] # Advance slow once
            fast = nums[nums[fast]] # Advance fast twice
            if slow == fast:
                break # This is the point where slow within the cycle is now the same distance
                # from the start of the cycle as the nums[0] is from the start of the cycle
            
        slow2 = 0 # Another slow pointer from nums[0] to iterate to slow
        while True:
            slow = nums[slow] # Iterate slow once
            slow2 = nums[slow2] # Iterate slow2 once
            if slow == slow2:
                return slow # Also valid to return slow2
                
