def BestTime(prices):
    profit = 0
    for index in range(len(prices)-1):
        if(prices[index] < prices[index+1]):
            profit += prices[index+1] - prices[index]
            print("Buy on day " + str(index + 1) + " (price = " + str(prices[index]) + ") and sell on day " + str(index + 2) + " (price = " + str(prices[index+1]) + 
                  "), profit = " + str(prices[index+1]) + "-" + str(prices[index]) + " = " + str(prices[index+1]-prices[index]) + ".")

    return profit


#Example 1:
#Input: 
prices = [7,1,5,3,6,4]
print(BestTime(prices))
#Output: 7
#Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#Total profit is 4 + 3 = 7.

#Example 2:
#Input: 
prices = [1,2,3,4,5]
print(BestTime(prices))
#Output: 4
#Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#Total profit is 4.

#Example 3:
#Input: 
prices = [7,6,4,3,1]
print(BestTime(prices))
#Output: 0
#Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

 