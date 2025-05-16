class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = maxLenght = 0
        charSet = set()

        # Uses sliding window with set
        for right in range(len(s)):

            while s[right] in charSet: # If the char is in the set slide the window to the right
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right]) # Adds the next char on the set
            if (right - left) + 1> maxLenght: # Checks if the combination have more chars than the last max
                maxLenght = right - left + 1

        return maxLenght