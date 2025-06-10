class Solution:
    def reverseWords(self, s: str) -> str:

        # Splits the string in a list and creates two pointers at the end and at the beginning
        s = s.split()
        left, right = 0, len(s) - 1
        
        # While the left pointer is smaller than the right one
        # We switch them with each other
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        # We join the list with spaces
        return " ".join(s)