class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value=0
        count1=0
        prevcount=0
        s=set(nums)
        for i in s:
            count1=nums.count(i)
            if prevcount<count1:
                prevcount=count1
                value=i
        return value
        