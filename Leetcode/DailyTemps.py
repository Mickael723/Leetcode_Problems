class Solution:
    def dailyTemperatures(self, temperatures: list) -> list:
        
        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) -1, -1, -1):

            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = abs((stack[-1][0]) - i)
            else:
                ans[i] = 0
        
            stack.append((i,temperatures[i]))
        
        return ans

if __name__=="__main__":
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(s.dailyTemperatures([30,40,50,60]))
    print(s.dailyTemperatures([30,60,90]))