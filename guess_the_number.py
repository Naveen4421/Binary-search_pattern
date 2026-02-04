def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r=0,n
        while l<=r:
            mid=(l+r)//2
            ges=guess(mid)
            if ges==0:
                return mid
            elif ges>0:
                l=mid+1
            else:
                r=mid-1
