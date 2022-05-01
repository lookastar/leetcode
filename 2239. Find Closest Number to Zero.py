from types import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        def findDistance(self, num: int) -> int:
            if num >= 0:
                return num
            else:
                return num * -1

        min = nums[0]

        for i in nums:
            if findDistance(self, i) < findDistance(self, min) or (findDistance(self, i) == findDistance(self, min) and i > min):
                min = i

        return min

    def findClosestNumber1(self, nums: List[int]) -> int:
        closest = nums[0]
        for a in nums: 
            if abs(closest) > abs(a):
                closest = a
            elif abs(closest) == abs(a):
                closest = max(closest, a)
        return closest 

