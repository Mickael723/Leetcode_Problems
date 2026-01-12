import heapq
class Solution:
    def lastStoneWeight(self, stones: list) -> int:

        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            largest = -heapq.heappop(heap)
            next_largest = -heapq.heappop(heap)

            difference = abs(largest - next_largest)

            if difference != 0:
                heapq.heappush(heap, -difference)
        
        return -heap[0]

if __name__=="__main__":
    s = Solution()
    print(s.lastStoneWeight([2,7,4,1,8,1]))
    print(s.lastStoneWeight([1]))