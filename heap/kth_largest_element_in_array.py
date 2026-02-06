# KTH LARGEST ELEMENT IN AN ARRAY
# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)
            while len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0] # The heap after going through all nums 
        # will be size k because of clause inside for loop
        # Uses O(k) space
        # Runs in O(n log k)
