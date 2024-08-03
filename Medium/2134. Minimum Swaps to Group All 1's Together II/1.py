class Solution:
    def minSwaps(self, nums) -> int:
        if len(nums) < 1:
            return 0

        num_of_one = 0

        for i in nums:
            if(i == 1):
                num_of_one += 1
    
        nums += nums

        i = 0
        j = i + num_of_one
        swaps = float('inf')

        while(i <= len(nums) - num_of_one):
            num_of_zero = 0
            for k in range(i , j):
                if nums[k] == 0 :
                    num_of_zero += 1
            
            swaps = min(swaps , num_of_zero)
            i += 1
            j += 1
        
        return swaps

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    print(solution.minSwaps([1,0,1,0,1])) # 1
    print(solution.minSwaps([0,0,0,1,0])) # 0
    print(solution.minSwaps([1,0,1,0,1,0,0,1,1,0,1])) # 2
    print(solution.minSwaps([1,1,1,0,0,0,1,1])) # 0