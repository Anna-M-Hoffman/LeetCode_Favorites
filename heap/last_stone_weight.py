# LAST STONE WEIGHT

# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.

# Return the weight of the last remaining stone or return 0 if none remain.

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python does not have a max heap. 
        # We use a min heap but multiply every value by -1
        # and reconvert by multiplying again by -1
        
        stones = [-s for s in stones] 
        # Putting the stones in a list and multiplying by -1

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            stone1 *= -1
            stone2 *= -1
            if stone1 > stone2:
                stone1 = stone1 - stone2
                heapq.heappush(stones, stone1 * -1)
            elif stone2 > stone1:
                stone2 = stone2 - stone1
                heapq.heappush(stones, stone2 * -1)
        if not stones:
            return 0
        else:
            return stones[0] * -1
