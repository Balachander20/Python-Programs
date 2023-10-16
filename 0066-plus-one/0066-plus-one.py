class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[]
        sum=0
        for i in digits:
            sum=sum*10+i
            
        sum=sum+1
        while sum!=0:
            x=sum%10
            l.insert(0,x)
            sum=sum//10
        
        return l
        
            
        
        