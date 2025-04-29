class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        #helper to map roman numerals to their values
        romanNumbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 

        for index in range(len(s)):
            #checks if it's not the last number and if the next number is larger
            if index + 1 < len(s) and romanNumbers[s[index]] < romanNumbers[s[index + 1]]:
                result -= romanNumbers[s[index]] 
            else:
                result += romanNumbers[s[index]]
        return result
