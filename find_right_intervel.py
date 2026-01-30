def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        starts = [(interval[0], i) for i, interval in enumerate(intervals)]
        starts.sort()  # sort by start

        result = []
        for start, end in intervals:
            target = end
            left, right = 0, len(starts)
            # binary search for smallest start >= end
            while left < right:
                mid = (left + right) // 2
                if starts[mid][0] >= target:
                    right = mid
                else:
                    left = mid + 1

            if left < len(starts):
                result.append(starts[left][1])
            else:
                result.append(-1)

        return result
