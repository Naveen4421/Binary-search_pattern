def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                return i-1
