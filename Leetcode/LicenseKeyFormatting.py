class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

       total_len = len(s)
       num_dashes = s.count("-")
       num_chars = total_len - num_dashes

       first_grp_len = (num_chars % k) or k
       ans = []
       cnt = first_grp_len

       for char in s:
           if char == "-":
               continue
           ans.append(char.upper())
           cnt -= 1

           if cnt == 0:
               cnt = k
               ans.append("-") 
                  
       return "".join(ans).rstrip("-")
    
if __name__== "__main__":
    s = Solution()
    print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
    print(s.licenseKeyFormatting("2-5g-3-J", 2))