def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #from typing import List
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element > rightmost element,
            # the minimum is to the right side
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, the minimum is at mid or left side
                right = mid
        
        # left == right is the index of minimum
        return nums[left]
