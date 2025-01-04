class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        curr_longest_length = 0
        left_ptr = 0
        right_ptr = 0

        while right_ptr < len(s):
            if s[right_ptr] not in seen_chars:
                seen_chars.add(s[right_ptr])
                curr_longest_length = max(curr_longest_length, len(seen_chars))
                right_ptr += 1
            else:
                seen_chars.remove(s[left_ptr])
                left_ptr += 1

        return curr_longest_length



if __name__== "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
    print(sol.lengthOfLongestSubstring(""))          # Output: 0
    print(sol.lengthOfLongestSubstring(" "))         # Output: 1
    print(sol.lengthOfLongestSubstring("a b c"))     # Output: 3
    print(sol.lengthOfLongestSubstring("dvdf"))      # Output: 3
