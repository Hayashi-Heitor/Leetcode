class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # Checks edge cases
        if not s or k < 1:
            return 0
        
        # Creates a frozenset of the vowels and a vowels counter
        vowels = frozenset("aeiou")
        currentVowels = 0

        # Runs the first window counting the vowels
        for index in range(k):
            if s[index] in vowels:
                currentVowels += 1
        
        # Attributes the vowels to the max
        maxVowels = currentVowels

        # Keeps sliding windows, taking the vowel in the left out and the vowel in the right in 
        for index in range(k, len(s)):
            if s[index - k] in vowels:
                currentVowels -= 1
            if s[index] in vowels:
                currentVowels += 1
            
            # Checks if the currentVowels sum is greater than the previous max
            maxVowels = max(maxVowels, currentVowels)
        
        return maxVowels