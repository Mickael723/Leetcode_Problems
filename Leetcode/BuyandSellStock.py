class Solution:
    def maxProfit(self, prices: list) -> int:
        
        accum_profit = 0
        min_price = float("inf")
        curr_best_prof = 0
        for price in prices:

            if price < min_price and curr_best_prof == 0:
                min_price = price
                continue
            
            if price - min_price > curr_best_prof:
                curr_best_prof = price - min_price
            
            else:
                accum_profit += curr_best_prof
                min_price = price
                curr_best_prof = 0
        
        if curr_best_prof > 0:
            accum_profit += curr_best_prof
            
        return accum_profit


        

if __name__=="__main__":
    s = Solution()
    print(s.maxProfit([2,1,2,0,1]))

    