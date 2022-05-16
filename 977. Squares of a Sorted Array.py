class Solution:
    def sortedSquares_oldest(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            nums[i]=nums[i]**2
        
        nums.sort()
        
        return nums
    
    def findMinSquareIndex(self, nums: List[int]) -> int:
        min_i = 0
        min = nums[min_i]**2
        
        for i in range(0,len(nums)):
            if nums[i]**2 <= min:
                min_i = i
                min = nums[min_i]**2
            else:
                break   #if values **2 start going up it means the minimum is not there anymore
        
        return min_i    
    
    def sortedSquares_old(self, nums: List[int]) -> List[int]:
        left = Solution.findMinSquareIndex(self, nums)
        ans = [nums[left]**2]
        right = left +1
        left -= 1
        len_nums = len(nums)
        
        while left >= 0 and right < len_nums:
            if nums[left]**2 > nums[right]**2:
                ans.append(nums[right]**2)
                right += 1
            else:
                ans.append(nums[left]**2)
                left -= 1
            
        while left < 0 and right < len_nums:
            ans.append(nums[right]**2)
            right += 1
            
        while left >= 0 and right >= len_nums:
            ans.append(nums[left]**2)
            left -= 1
            
        return ans

    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left = 0
        right = len(nums) -1
        square_left = nums[left]**2
        square_right = nums[right]**2
        ans_pointer = len(nums)-1
        
        #while left <= right:
        for ans_pointer in range(len(nums)-1,-1,-1):
            if square_left > square_right:
                ans[ans_pointer] = square_left
                left += 1
                square_left = nums[left]**2
            else:
                ans[ans_pointer] = square_right
                right -= 1
                square_right = nums[right]**2
                
        return ans