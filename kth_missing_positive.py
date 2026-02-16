 def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i = 1
        j = 0
        
        while k > 0:
            if j < len(arr) and arr[j] == i:
                j += 1
            else:
                k -= 1
                if k == 0:
                    return i
            i += 1
