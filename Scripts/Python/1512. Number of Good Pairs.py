class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = {} 
        count = 0

        for index in range(len(nums)):
            if nums[index] in goodPairs: #checks if the number in the index already appeared
                count += goodPairs[nums[index]] #sums the count with the appearances of the number
            goodPairs[nums[index]] = goodPairs.get(nums[index], 0) + 1 #register the number in the hash table
        
        return count
