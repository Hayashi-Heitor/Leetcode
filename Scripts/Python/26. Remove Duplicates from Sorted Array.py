class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        solution = 0 #creates the pointer for the array without duplicates

        for original in range(1, len(nums)):
            if nums[solution] != nums[original]: #checks if the pointers numbers are different
                solution += 1
                nums[solution] = nums[original] #swaps one pointer number for the other

        return solution + 1
