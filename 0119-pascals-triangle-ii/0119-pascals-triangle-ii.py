class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r=[1]
        for i in range(rowIndex):
            r1=r.copy()
            r2=r.copy()
            print(r1)
            print(r2)
            r1.append(0)
            print(r1)
            r2.insert(0,0)
            print(r2)
            r.clear()
            for i in range (len(r1)):
                r.append(r1[i]+r2[i])
        return r
            
        