class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Starts a left pointer at the beginning of the list and a right pointer at the end
        left = 0
        right = len(height) - 1
        maxArea = 0

        # Keeps a loop while left and right are not in the same position
        while left < right:
            # Gets the maxArea comparing the previous max and the new area
            maxArea = max(maxArea, (right - left) * min(height[left], height[right]))

            # Checks what pointer is greater and adjust accordingly
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea