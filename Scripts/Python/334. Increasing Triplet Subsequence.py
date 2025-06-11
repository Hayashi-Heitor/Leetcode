class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # If there are less than 3 elements on the list we return False
        if len(nums) < 3:
            return False

        # Creates two infinite float variables
        # Because any numbers is lower than infinite
        potentialFirst = float("inf")
        potentialSecond = float("inf")

        # Checks every number until first < second < n
        # If thats the case return true, if not we swap n with first / secont
        for number in nums:
            if number <= potentialFirst:
                potentialFirst = number
            elif number <= potentialSecond:
                potentialSecond = number
            else:
                return True
        
        # If the exit the loop we checked every number so we return False
        return False