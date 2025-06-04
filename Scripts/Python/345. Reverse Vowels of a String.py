class Solution:
    def reverseVowels(self, s: str) -> str:
        # Creates a vowel string, end index and a list of chars from the string
        vowels = "aeiouAEIOU"
        end = len(s) - 1
        chars = list(s)

        # Start pointer checks all values in the string
        for start in range(len(s)):

            # If start pointer is a vowel and it is lower than the end pointer
            if chars[start] in vowels and end > start:

                # While end pointer is not a vowel we keep decreasing
                while end > start and chars[end] not in vowels:
                    end -= 1

                # If the end and start are not pointing at the same value we swap
                if end != start:
                    chars[start], chars[end] = chars[end], chars[start]
                    end -= 1
        
        # Returns the list in a string format
        return "".join(chars)