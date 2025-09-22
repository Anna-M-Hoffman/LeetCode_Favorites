# TRAPPING RAIN WATER
# You are given an array of non-negative integers height which represent an elevation map.
# Each value height[i] represents the height of a bar with width 1.
# Return the total amount of water that can be trapped after raining.

class Solution: 
    def trap(self, height: List[int]) -> int: 
      # Two pointers  
      left, right = 0, len(height)-1
      # Track the tallest bars from each side
        max_left, max_right = 0, 0
        depth = 0

        while left < right: # Move both pointers inward until they meet
            if height[left] < height[right]: # Left side is smaller than right - determines water level as max height of left
                if height[left] > max_left: # Current left is higher than max left
                    max_left = height[left] # Update maximum (tallest bar seen so far)
                else:
                    depth += max_left - height[left] # Water added between max left and current left height
                left += 1 # Move left pointer inward
            else: # Right side is smaller than left -  determines water level as max height of right
                if height[right] > max_right: # Current right is higher than max right
                    max_right = height[right] # Update maximum (tallest bar seen so far)
                else:
                    depth += max_right - height[right] # Water added between max right and current right height
                right -= 1 # Move right pointer inward
        return depth
      
# Time complexity: O(n)
# Space complexity: O(1)
