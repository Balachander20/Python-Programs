class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=len(s)
        count=0
        for i in range(x-1,-1,-1):
            if s[i]==" ":
                continue
            else:
                for j in range(i,-1,-1):
                    if s[j]!=" ":
                        count+=1
                    else:
                        break
                return count
        return count
       
                        
                