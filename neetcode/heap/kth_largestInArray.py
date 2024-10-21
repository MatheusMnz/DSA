import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: # type: ignore
        heap = [-num for num in nums]
        heapq.heapify(heap)

        for i in range(k):
            if i == k - 1:
                return -heapq.heappop(heap)
            else:
                heapq.heappop(heap)

        return 

