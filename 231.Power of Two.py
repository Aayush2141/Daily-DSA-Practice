class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False

        st=""
        while n>0:
            a=n%2
            st+=str(a)
            n//=2
        
        count=0
        for i in st:
            if i=="1":
                count+=1
        if count>1:
            return False
        else:
            return True
