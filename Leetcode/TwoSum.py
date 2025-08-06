class Solution:
    def twoSum(self, nums: list, target: int) -> list:

        sum_set = set()

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in sum_set:
                return [nums.index(complement), i]
            
            sum_set.add(nums[i])
        
        return []

if __name__=="__main__":
    s = Solution()
    print(s.twoSum([3,2,4], 6))