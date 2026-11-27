class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [prices[-1]]
        l  = len(prices) - 1
        for i in range(len(prices)):
            if i == 0:
                continue
           
            arr.append(max(arr[i-1], prices[l - i]))
            
        m = 0
        for i in range(len(prices)):
            m = max(m, arr[l-i] - prices[i])
      
        return m

