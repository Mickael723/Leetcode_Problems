class Solution:
    def maxProfit(self, prices: list) -> int:
        
        first_buy = -prices[0]
        first_sell = 0
        second_buy = -prices[0]
        second_sell = 0

        for price in prices[1:]:

            if -price > first_buy:
                first_buy = -price
            
            if price + first_buy > first_sell:
                first_sell = price + first_buy
            
            if -price + first_sell > second_buy:
                second_buy = -price + first_sell
            
            if price + second_buy > second_sell:
                second_sell = price + second_buy

        return second_sell

if __name__=="__main__":
    s = Solution()
    print(s.maxProfit([3,3,5,0,0,3,1,4]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([7,6,4,3,1]))


    