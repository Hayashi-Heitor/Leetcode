class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersHashMap = {}

        for index in range(len(nums)):
            complement = target - nums[index] #get how much the number needs to reach the target
            if complement in numbersHashMap:
                return [numbersHashMap[complement], index] #returns the position of the complement and the index
            numbersHashMap[nums[index]] = index

        return [] #empty array if solution was not found
