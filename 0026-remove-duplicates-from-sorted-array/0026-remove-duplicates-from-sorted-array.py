class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l2=[]
        index=0
        for i in range(len(nums)):
            if nums[i] not in l2:
                l2.append(nums[i])
                nums[index]=nums[i]
                index+=1
                
        return index
        