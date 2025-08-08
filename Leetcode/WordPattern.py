class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        strings = s.split()
        if len(pattern) != len(strings): return False

        pattern_hash = {}
        string_hash = {}

        for i in range(len(pattern)):

            if pattern[i] not in pattern_hash:
                pattern_hash[pattern[i]] = i
            if strings[i] not in string_hash:
                string_hash[strings[i]] = i

            if pattern_hash[pattern[i]] != string_hash[strings[i]]:
                return False
            
        return True

if __name__=="__main__":
    s = Solution()
    print(s.wordPattern("aaaa", "dog cat cat dog"))