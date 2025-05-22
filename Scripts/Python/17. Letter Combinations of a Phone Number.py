class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If there is no digits return a empty array
        if not digits:
            return []
        
        # Creates a hashmap of digits and the correspondent letters
        digitToLetters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtracking(index, combination):

            # If the index has the lenght of digits append on the current combination
            if index == len(digits):
                result.append(combination[:])
                # Returns nothing to get out of the function
                return
            
            # Advances the backtracking increasing the index
            for letter in digitToLetters[digits[index]]:
                backtracking(index + 1, combination + letter)
            
        # Creates the result empty array and calls backtrack function
        result = []
        backtracking(0, "")

        return result
