class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        lcp = ""
        strs.sort(key=len)

        for i in range(0 , len(strs[0])):
            occurrences = 1
            end = False
            for j in range(1 , len(strs)):
                if(strs[j][i] == strs[0][i]):
                    occurrences += 1
                else:
                    end = True
                    break
            if(end):
                break
            if(occurrences == len(strs)):
                lcp += strs[0][i]
            
        return lcp