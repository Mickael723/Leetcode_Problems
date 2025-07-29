class Solution:
    def isPalindrome(self, x: int) -> bool:

        #MO: First, negative number cannot be a palindrome
        if x < 0:
            return False
        #MO: Single digit numbers are palindromes
        if x < 10:
            return True
        
        #MO Reverse the number
        temp = x
        reverse = 0
        while temp > 0:
            last_digit = temp % 10
            reverse = reverse * 10 + last_digit
            temp = temp // 10
        
        return reverse == x

if __name__=="__main__":
    s = Solution()
    print(s.isPalindrome(12321))