class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums1=[]
        for i in nums:
            if i in nums1:
                nums1.remove(i)
            else:
                nums1.append(i)

        return nums1[0]
