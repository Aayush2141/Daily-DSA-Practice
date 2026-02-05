class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            count=0
            while i>0:
                a=i%2
                if a==1:
                    count+=1
                i//=2
            l.append(count)
        return l


