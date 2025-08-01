class Solution:
    def singleNumber(self, nums: list) -> int:
        
        once = 0
        twice = 0

        for number in nums:
            once = (once^number) & ~twice
            twice = (twice^number) & ~once
            print(f"Looking at {number}\nOnce: {once}\nTwice: {twice}")
        return once
    
if __name__=="__main__":
    s = Solution()
    print(s.singleNumber([2,2,3,2]))
