from operator import mod
#from types import List


class Solution:
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
    
    def rotate2(self, nums, k: int) -> None: #: List[int]
        nums_len = len(nums)
        ans = [0 for i in range(0,nums_len)]
        
        for i in range (0,nums_len):
            ans[(i+k) % nums_len] = nums[i]

        nums = ans
        print(ans)
        # for i in range(0,k):
        #     temp = nums[i]
        #     for j in range(i,nums_len,k):
        #         next_pointer=(j+k) % (nums_len+1)
        #         temp2 = nums[next_pointer]
        #         nums[next_pointer] = temp
        #         temp = temp2
                
sol = Solution()
sol.rotate([1,2,3,4,5,6,7],3)

            
k = 3, n = 7
1,2,3,4,5,6,7
5,6,7,1,2,3,4