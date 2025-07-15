from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hash_s = {}
        hash_t = {}

        for i in range(len(s)):

            if s[i] not in hash_s.keys():
                hash_s[s[i]] = i
            
            if t[i] not in hash_t.keys():
                hash_t[t[i]] = i
            
            if hash_s[s[i]] != hash_t[t[i]]:
                return False
        
        if len(hash_s.keys()) != len(hash_t.keys()):
            return False
        return True
            
if __name__=="__main__":
    print(Solution.isIsomorphic(Solution, s = "bbbaaaba", t = "aaabbbba"))