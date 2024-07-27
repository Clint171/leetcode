class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        def merge(arr, l , m , r):
            lsize = m - l + 1
            rsize = r - m

            larr = [0] * lsize
            rarr = [0] * rsize

            for i in range(0 , lsize):
                larr[i] = arr[l + i]
            
            for j in range(0 , rsize):
                rarr[j] = arr[m + j +1]
            
            i = 0
            j = 0
            k = l

            while i < lsize and j < rsize:
                if larr[i] < rarr[j]:
                    arr[k] = larr[i]
                    i += 1
                
                else:
                    arr[k] = rarr[j]
                    j += 1

                k += 1
            
            while i < lsize:
                arr[k] = larr[i]
                i += 1
                k += 1
            
            while j < rsize:
                arr[k] = rarr[j]
                j += 1
                k += 1
        
        def mergeSort(arr , l , r):
            if(l < r):
                m = l + ((r-l))//2

                mergeSort(arr , l , m)
                mergeSort(arr , m+1 , r)
                merge(arr , l , m , r)
            
            return arr


        return mergeSort(nums , 0 , len(nums)-1)
