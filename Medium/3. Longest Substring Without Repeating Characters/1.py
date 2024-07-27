class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        length = 0
        i = 0
        for j in range(len(s)):
            if(s[j] in table):
                i = max(i , table[s[j]]+ 1)

            length = max(length , j - i + 1)

            table[s[j]] = j
        
        return length
