class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft = maxRight = res = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= maxLeft:
                    maxLeft = height[l]
                else:
                    res += maxLeft - height[l]
                l += 1
            else:
                if height[r] >= maxRight:
                    maxRight = height[r]
                else:
                    res += maxRight - height[r]
                r -= 1
        
        return res


