class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = math.inf
        l, r = max(weights), sum(weights)

        while l <= r:
            mid = (l + r) // 2

            currDays = 1
            currW = 0

            for w in weights:
                if currW + w > mid:
                    currDays += 1
                    currW = 0
                currW += w

            if currDays <= days:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
                


