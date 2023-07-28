class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l <= r:
            c_area = min(height[l],height[r]) * ( r - l )
            maxArea = max(maxArea, c_area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return maxArea
