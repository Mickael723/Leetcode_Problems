class Solution:
    def addBinary(self, a: str, b: str) -> str:

        carry = 0
        a_val = int(a, 2)
        b_val = int(b, 2)
        
        while b_val != 0:
            carry = a_val & b_val
            a_val = a_val ^ b_val
            b_val = carry << 1
        
        return bin(a_val)[2:]

if __name__=="__main__":
    s = Solution()
    print(s.addBinary("1010","1011"))