class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        solutions = [-1] * (len(s) + 1)
        def LLS(i: int) -> int:
            if i == 0: return 0
            if solutions[i] != -1:
                return solutions[i]
            
            seen_chars = set()
            curr_longest_length = 0
            prev_longest_length = 1

            for j in range(i):
                if s[j] in seen_chars:
                    prev_longest_length = curr_longest_length
                    curr_longest_length = 0
                    seen_chars.clear()
                    
                curr_longest_length += 1
                seen_chars.add(s[j])
                    

            computed_longest_length = max(prev_longest_length, curr_longest_length)
            solutions[i] = max(computed_longest_length, LLS(i - 1))

        for i in range(0, len(s) + 1):
            LLS(i)
        return max(max(solutions), 0)


if __name__== "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
    print(sol.lengthOfLongestSubstring(" "))         # Output: 1
    print(sol.lengthOfLongestSubstring("a b c"))     # Output: 3
