class Solution:
    def finalPrices(self, prices: list) -> list:
        
        discounted_prices = [-1] * len(prices)
        stack = []
        
        
        for i in range(len(prices) -1, -1, -1):
            
            while stack and stack[-1] > prices[i]:
                stack.pop()
            
            if stack:
                discounted_prices[i] = abs(prices[i] - stack[-1])
            else:
                discounted_prices[i] = prices[i]
            
            stack.append(prices[i])

        return discounted_prices


if __name__=="__main__":
    s = Solution()
    print(s.finalPrices([8,4,6,2,3]))
    print(s.finalPrices([1,2,3,4,5]))
    print(s.finalPrices([10,1,1,6]))