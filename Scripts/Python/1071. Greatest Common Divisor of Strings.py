class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Checks if both strings have the same pattern
        if str1 + str2 != str2 + str1:
            return ""
        
        # Keeps grabbing the rest until it is zero
        result, rest = len(str1), len(str2)
        while rest > 0:
            result, rest = rest, result % rest

        # Returns the first string until the result pointer
        return str1[:result]