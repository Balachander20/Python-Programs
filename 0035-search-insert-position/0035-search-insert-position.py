class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index_list=[]
        for i in range(len(nums)):
            if target==nums[i]:
                return i
            
        for num in nums:
            if target>num:
                index_list.append(num)
            else:
                break
        return len(index_list)
                
        
        
        
            
        