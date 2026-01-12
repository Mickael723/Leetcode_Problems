import heapq
class Solution:
    def kSmallestPairs(self, nums1: list, nums2: list, k: int) -> list:

        heap = []
        pairs = []
        visited = set()

        heapq.heappush(heap, (nums1[0]+nums2[0], (0,0)))
        visited.add((0,0))

        while len(pairs) < k and heap:

            _, indices = heapq.heappop(heap)
            i, j = indices
            pairs.append([nums1[i], nums2[j]])

            if i+1 < len(nums1):
                if (i+1, j) not in visited:
                    heapq.heappush(heap, (nums1[i+1]+nums2[j], (i+1,j)))
                    visited.add((i+1, j))
            if j+1 < len(nums2):
                if (i, j+1) not in visited:
                    heapq.heappush(heap, (nums1[i]+nums2[j+1], (i,j+1)))
                    visited.add((i,j+1))
        
        return pairs
        
if __name__=="__main__":
    s = Solution()
    print(s.kSmallestPairs([1,7,11], [2,4,6], 3))