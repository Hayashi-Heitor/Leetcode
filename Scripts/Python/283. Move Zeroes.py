class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        # While the fast pointer is not at the ent of the list
        for fast in range(len(nums)):
            
            # If fast is not zero and slow is zero we swap both
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            
            # If slow is not zero we go foward
            if nums[slow] != 0:
                slow += 1