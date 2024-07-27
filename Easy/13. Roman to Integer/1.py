class Solution:
    def romanToInt(self, s: str) -> int:
        conversions : dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        numeral : int = 0
        previous : int = 0
        for i in s[::-1]:
            value = conversions.get(i)

            if value < previous:
                numeral -= value

            else:
                numeral += value
            previous = value
        
        return numeral