class Solution:
    # def maxProfit(self, prices: list[int]) -> int:
    #     best_pricec = 0

    #     for i in range(len(prices)):
    #         for j in range(i+1, len(prices)):
    #             if prices[i] < prices[j]:
    #                 price =  prices[j] - prices[i]
    #                 if price > best_pricec:
    #                     best_pricec = price
        
    #     print(best_pricec)
    #     return best_pricec   
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in prices:
            if min_price > i:
                min_price = i
            profit = i - min_price
            if max_profit < profit:
                max_profit = profit
       
        return max_profit

            


obj = Solution()
result = obj.maxProfit([7,2,1,5,6,4,8])
print(result)
result = obj.maxProfit([7,6,4,3,1])

print(result)