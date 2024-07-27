class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ROWS = numRows
        reverse = False
        reversenum = numRows - 2 if numRows > 2 else 0
        matrix = []
        column = []
        reversecount = 2
        rets = ""
        if numRows == 1:
            return s
        elif numRows == 2:
            for i in range(0, len(s) , 2):
                rets += s[i]
            for j in range(1 , len(s) , 2):
                rets += s[i]
            return rets
        for i in range(len(s)):
            if not(reverse):
                column.append(s[i])

            else:
                for j in range(ROWS):
                    column.append(0)
                column[ROWS - reversecount] = s[i]
                matrix.append(column)
                reversecount += 1
                column = []

            if (i == numRows-1 and not(reverse)) or(i == len(s) -1):
                while(len(column) < ROWS):
                    column.append(0)

                matrix.append(column)
                column = []
                reverse = True
                numRows += reversenum + 1

            elif(i == numRows-2 and reverse):
                reverse = False
                numRows += reversenum +1
                reversecount = 2
        
        for m in range(len(matrix)):
            print(*matrix[m])
        for k in range(ROWS):
            for l in range(len(matrix)):
                if not(matrix[l][k] == 0):
                    rets += matrix[l][k]

        return rets
