class Solution:
    def myAtoi(self, s: str) -> int:
        sign = "+"
        int_list = []
        number = 0

        integers = {"0","1","2","3","4","5","6","7","8","9"}

        for i in s:
            if len(int_list) == 0:
                if i == " ":
                    continue
                
                elif i == "+" or i == "-":
                    sign = i
                    int_list.append(sign)
                    continue
                
                elif not(i in integers):
                    break

            if i in integers:
                int_list.append(int(i))
            
            else:
                break

        for j in range(len(int_list)):
            if int_list[j] == "+" or int_list[j] == "-":
                continue
            number += int_list[j] * (10**(len(int_list) - j - 1))

        if(sign == "+"):
            if number > 2**31 - 1:
                return 2**31 - 1
            return number
        else:
            if number > (2**31):
                return -(2**31)
            return -number

# Driver code
if __name__ == "__main__":
    s = "-91283472332"
    solution = Solution()
    print(solution.myAtoi(s))