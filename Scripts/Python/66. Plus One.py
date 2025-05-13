class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for index in range(len(digits) -1, -1, -1): #starts the loop at the end and decrases the index
            if digits[index] + 1 != 10:
                digits[index] += 1
                return digits #if the digit isn't nine returns the digits + 1
            digits[index] = 0 #else the digit is zero and the loop continues
        
        if digits[index] == 0: #if all the numbers are zeroes and there is still a carry returns 1 + digits
            return [1] + digits
