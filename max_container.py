class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_cont = 0
        while left < right:
            cur_cont = min(height[left], height[right]) * (right - left)
            if cur_cont > max_cont:
                max_cont = cur_cont
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_cont