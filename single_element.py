def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            
            # Make mid even (so it's the first of a pair)
            if mid % 2 == 1:
                mid -= 1
            
            # If pair is aligned, single element is to the right
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                # Otherwise, it's to the left (including mid)
                right = mid
        
        return nums[left]
