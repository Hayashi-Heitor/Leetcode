class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Creates both start and end pointers
        left = 0
        right = len(nums) - 1

        # While left is not greater than right 
        while left <= right:

            # We get the middle between them
            middle = (left + right) // 2

            # If the middle is the target we return it
            if nums[middle] == target:
                return middle
            
            # If the target is greater than the middle, we cut out the low part
            elif nums[middle] < target:
                left = middle +1
            
            # Else we cut out the high part
            else:
                right = middle -1

        # If we get out of the loop the value does not exists
        return -1