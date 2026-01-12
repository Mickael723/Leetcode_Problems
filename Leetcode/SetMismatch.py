class Solution:
    def findErrorNums(self, nums: list) -> list:
        
        ans = [-1, -1]

        num_map = [0] * (len(nums) + 1)

        for num in nums:
            num_map[num] += 1
        
        for i in range(1, len(num_map)):
            if num_map[i] == 0:
                ans[1] = i
            if num_map[i] == 2:
                ans[0] = i
        
        return ans

if __name__=="__main__":
    s = Solution()
    print(s.findErrorNums([1,2,2,4]))
    print(s.findErrorNums([1,1]))
    print(s.findErrorNums([3,2,2]))