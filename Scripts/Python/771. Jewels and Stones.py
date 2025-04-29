class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for index in range(len(stones)):
            if stones[index] in jewels: #checks if the letter is in "jewels" string
                count += 1
        
        return count
