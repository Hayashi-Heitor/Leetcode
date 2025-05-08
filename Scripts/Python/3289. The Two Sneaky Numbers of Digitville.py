class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        allNums = set(nums) #creates a set without duplicates

        for num in allNums: 
            if num in nums: #checks if the number is in the set
                nums.remove(num) #removes the number in set from the array

        return nums #returns the array with just the repeated numbers