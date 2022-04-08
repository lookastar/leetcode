from math import floor


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int], target: int
        :rtype: int
        """
        a=0
        b=len(nums)-1

        while b>=a:
            center=floor((a+b)/2)
            
            if target==nums[center]:
                return center

            if a==b:
                if target>nums[center]:
                    return center+1
                else:
                    return center

            if target>nums[center]:
                a=center+1
            else:
                b=center-1

        return a