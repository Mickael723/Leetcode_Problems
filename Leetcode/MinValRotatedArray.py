class Solution:
    def findMin(self, nums: list) -> int:

        #Edge Case
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            curr = nums[mid]
            if left == right:
                return curr
            #Case 2 min is on one of the edges
            if mid == 0 and nums[mid + 1] > curr:
                return curr
            if mid == len(nums) - 1 and nums[mid - 1] < curr:
                return curr
            #Case 1 min is in the middle
            if curr < nums[mid + 1] and curr < nums[mid - 1]:
                return curr
            
            #Time to shorten the search space
            elif curr > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

if __name__=="__main__":
    s = Solution()
    print(s.findMin([4,5,6,7,0,1,2]))


