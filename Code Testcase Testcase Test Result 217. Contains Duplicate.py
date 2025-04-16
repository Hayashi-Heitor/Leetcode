class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() #creates a hash set

        for number in nums:
            if number in seen: #check if the number is in the hash set
                return True
            seen.add(number) #adds the number to the hash set
        
        return False
