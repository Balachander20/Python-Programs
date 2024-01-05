"""class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l=[]
        prevlength=0
        x=len(nums)
        for i in range(x):
            y=nums[i]
            l.append(nums[i])
            for j in range(i+1,x):
                if nums[j]>y:
                    l.append(nums[j])
                    y=nums[j]
            print(len(l))
                    
            if prevlength<len(l):
                prevlength=len(l)
            l.clear()
        return prevlength"""
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        arr = [nums.pop(0)]                 
 
        for n in nums:                     
            
            if n > arr[-1]:                  
                arr.append(n)

            else:                            
                arr[bisect_left(arr, n)] = n 

        return len(arr)
        