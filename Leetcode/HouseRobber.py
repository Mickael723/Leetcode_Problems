class Solution:
    def rob(self, nums: list) -> int:
        
        dp_array = [-1] * (len(nums))

        dp_array[0] = 0 #MO: Boundary

        for i in range(0, len(nums)):
            
            if i == 0:
                dp_array[i] = nums[i]
            elif i == 1:
                dp_array[i] = max(nums[0], nums[1])
            else:
                dp_array[i] = max(dp_array[i-1], nums[i] + dp_array[i - 2])
        
        return(dp_array[-1])
        

if __name__=="__main__":
    s = Solution()

    nums = [1,2,3,1]

    print(s.rob(nums))
