# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        
        # While low is less or equal than high, we keep the binary search
        while low <= high:

            # Gets the midle value and tests with the result
            mid = (low + high) // 2
            result = guess(mid)

            # If we found the value we return it
            if result == 0:
                return mid
            
            # If the value is less than the guess we cut the high part
            elif result == -1:
                high = mid -1
            
            # Else we cut the low part
            else:
                low = mid +1