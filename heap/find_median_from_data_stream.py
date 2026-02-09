# FIND MEDIAN FROM DATA STREAM
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far.

class MedianFinder:
    # Uses two heaps, where the smaller values on the left side use a maxHeap
    # and the larger values on the right side use a minHeap
    # Heaps should not be 2+ greater than the other
    def __init__(self):
        self.small = [] # max heap (stores negatives)
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        # Always begin by adding num to small heap
        heapq.heappush(self.small, -num)
        
        # Move largest element of small to large heap
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # After step 2, large might have one extra element.
        # If it does, we move it to the small heap.
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:
        # If there is an extra number from an uneven split, it will always
        # be on the small side
        if len(self.small) > len(self.large):
            return -self.small[0]
        # Both are the same size = return mean of both heaps
        return (-self.small[0] + self.large[0]) / 2
