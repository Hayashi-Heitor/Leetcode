class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = set(allowed)

        for currentWord in words:
            for currentLetter in currentWord:
                if currentLetter not in allowed: #checks if the letter is allowed
                    count += 1 #counts the string that is not allowed
                    break

        return len(words) - count #returns all strings minus the count
