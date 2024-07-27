class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1 : 
            return 0
        
        k : int = 1

        for i in range(1 , len(nums)):
            if(not (nums[i] == nums[i-1])):
                nums[k] = nums[i]
                k += 1
            
        return k