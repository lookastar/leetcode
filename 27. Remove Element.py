class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fwd, rear = 0, 0
        while fwd < len(nums):
            if nums[fwd] != val:
                nums[rear] = nums[fwd]
                rear += 1
            fwd += 1
            
        return rear