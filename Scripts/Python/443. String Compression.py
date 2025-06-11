class Solution:
    def compress(self, chars: List[str]) -> int:
        index, write = 0, 0
        size = len(chars)

        # With the index we check every number in chars
        while index < size:
            # Gets the current letter and resets the count
            currentLetter = chars[index]
            letterCount = 0

            # While the index letter is the same as currentLetter we increase the count
            while index < size and chars[index] == currentLetter:
                index += 1
                letterCount += 1
            
            # If the index letter is different from the current we write the current
            chars[write] = currentLetter
            write += 1

            # If the count is greater than 1 we write its digits
            if letterCount > 1:
                for digit in str(letterCount):
                    chars[write] = digit
                    write += 1
        
        # Removes the chars after the write index
        chars[:] = chars[:write]