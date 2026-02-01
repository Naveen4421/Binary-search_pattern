class SnapshotArray(object):
    import bisect

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.data = [ [(0,0)] for _ in range(length) ] 
        

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.data[index].append((self.snap_id, val))
        

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        arr = self.data[index]
        # bisect to find right insertion point
        i = bisect.bisect_right(arr, (snap_id, float('inf'))) - 1
        return arr[i][1]
