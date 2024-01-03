class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        l=[]
        result=0
        for i in bank:
            ones=0
            for j in i:
                if j=='1':
                    ones+=1
            l.append(ones)
        x=l.count(0)
        for i in range(x):
            l.remove(0)
        for i in range(len(l)-1):
            mul=l[i]*l[i+1]
            result=result+mul
        return result
            
            
        
            