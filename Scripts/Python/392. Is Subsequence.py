class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = 0
        fast = 0

        # While fast and slow are not at the end of their string
        while fast < len(t) and slow < len(s):

            # If slow and fast positions have the same value advances slow
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        
        # Returns True if slow is at the end of the string and false otherwise
        return slow == len(s)