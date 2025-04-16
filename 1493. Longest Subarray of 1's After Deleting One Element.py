class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        if all(nums): #checks the hard case os all the numbers being 1
            return len(nums) - 1

        size = len(nums)
        low, high = 0, 0
        current, longestSubarray = 0, 0
        zeroes = 0

        while high < size: #while the window is not at the end of the array
            current += nums[high] #current recives the element on the high pointer, + 1 or + 0
            longestSubarray = max(longestSubarray, current)
            if nums[high] == 0:
                zeroes += 1
            while zeroes > 1: #while there is more than 1 zero in the subarray
                if nums[low] == 0:  #if the low contains the zero we just decrease it from the var
                    zeroes -= 1
                else:
                    current -= 1 #while we dont find the zero we keep decreasing the size
                low += 1
            high += 1
        
        return longestSubarray
