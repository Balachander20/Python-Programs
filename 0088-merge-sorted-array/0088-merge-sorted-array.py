class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            print(nums1)
        
        else:
            x=len(nums1)-n
            for i in range(n-1,-1,-1):
                nums1[x+i]=nums2[i]
            nums1.sort()
            print(nums1)