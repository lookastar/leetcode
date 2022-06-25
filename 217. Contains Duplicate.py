#from types import List
class Solution:
    def containsDuplicate(self, nums) -> bool: #: List[int]
        numsDict = {}
        for i in nums:
            if numsDict.get(i)==True:
                return True
            else:
                numsDict[i] = True
        return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,4]))

