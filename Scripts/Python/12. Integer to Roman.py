class Solution:
    def intToRoman(self, num: int) -> str:
        valueSymbols = [ #creates a list of tuples with values and symbols
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        result = []

        for value, symbol in valueSymbols: #gets each value and its symbol
            if num == 0:
                break
            count = num // value #gets the ammount of times the symbol will need to be used
            result.append(symbol * count) #appends the symnols
            num -= count * value #decreases the displayed value from the number
        
        return ''.join(result)
