class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0

        for index in range(len(nums)):

            # Decreases the current index from the right
            right -= nums[index]

            # If right and left have the same value returns the index
            if right == left:
                return index

            # Sums the current index in the left
            left += nums[index]
        
        # Returns -1 if we get out of the for loop
        return -1