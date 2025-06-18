class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        # Checks all the elements with right pointer
        for right in range(len(nums)):

            # If the right of the window is zero we swap it for a one
            if nums[right] == 0:
                k -= 1
            
            # If we have no more ones to swap we move the left part of the window
            if k < 0:
                
                # If the part we removed was a zero we replace the one we had used
                if nums[left] == 0:
                    k += 1
                left += 1
                
        return right - left + 1