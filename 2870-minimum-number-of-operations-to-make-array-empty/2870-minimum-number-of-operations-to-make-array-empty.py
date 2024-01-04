class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        x=Counter(nums).values()
        op=0
        for y in x:
            if y==1:
                return -1
            else:
                if y%3!=0:
                    op+=(y//3)+1
                else:
                    op+=y//3
        return op
                    
                
        