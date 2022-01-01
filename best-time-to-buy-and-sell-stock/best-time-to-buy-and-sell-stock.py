class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=math.inf
        maxprofit=-math.inf
        length=len(prices)
        mintillnow=[0]*length
        for i in range(length):
            # print("i",prices[i])
            minprice=min(prices[i],minprice)
            maxprofit=max(prices[i]-minprice,maxprofit)
            # print("minprice,maxprofit",minprice,maxprofit)
        return maxprofit