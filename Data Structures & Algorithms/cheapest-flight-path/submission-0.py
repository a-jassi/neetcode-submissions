class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, dest, price in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + price < tmpPrices[dest]:
                    tmpPrices[dest] = prices[s] + price
            prices = tmpPrices

        return -1 if prices[dst] == float('inf') else prices[dst]