from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        numbers_count=[0]*1001
        n = len(nums)
        for i in range(0,n):
            for j in range(0,len(nums[i])):
                numbers_count[nums[i][j]] += 1

        answer = []
        for k in range(1,1001):
            if(numbers_count[k]==n): answer.append(k)

        return answer