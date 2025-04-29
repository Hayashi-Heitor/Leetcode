class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #checks if the strings have the same length
            return False

        counterS, counterT = {}, {} #creates the hash maps

        for index in range(len(s)): #sort the hash maps
            counterS[s[index]] = 1 + counterS.get(s[index], 0)
            counterT[t[index]] = 1 + counterT.get(t[index], 0)
        
        return counterS == counterT #returns False if they are different and True if they are the same
