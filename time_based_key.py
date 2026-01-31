class TimeMap(object):

    def __init__(self):
        self.times = defaultdict(list)   # key -> [timestamps]
        self.values = defaultdict(list)
   

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.times[key].append(timestamp)
        self.values[key].append(value)
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.times:
            return ""

        idx = bisect.bisect_right(self.times[key], timestamp) - 1
        if idx >= 0:
            return self.values[key][idx]
        return ""
