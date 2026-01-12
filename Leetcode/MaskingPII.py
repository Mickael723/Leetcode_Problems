import re
class Solution:
    def maskPII(self, s: str) -> str:

        #phone num
        if not s[0].isalpha():
            s = s.translate(str.maketrans({'+':' ', '-':' ', '(':' ', ')':' '}))
            s = s.split()
            s = "".join(s)
            if len(s) == 10:
                return "***-***-" + s[-4:]
            elif len(s) == 11:
                return "+*-***-***-" + s[-4:]
            elif len(s) == 12:
                return "+**-***-***-" + s[-4:]
            elif len(s) == 13:
                return "+***-***-***-" + s[-4:]
            
            return ""
        #email
        else:
            name, domain = s.split("@")
            name, domain = name.lower(), domain.lower()
            name = name[0] + "*****" + name[-1]
            return name + "@" + domain
    
if __name__== "__main__":
    s = Solution()
    print(s.maskPII("LeetCode@LeetCode.com"))
    print(s.maskPII("AB@qq.com"))
    print(s.maskPII("1(234)567-890"))