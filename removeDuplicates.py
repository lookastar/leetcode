class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        bi=0; fi=1

        while fi<len(nums):
            while fi<len(nums) and nums[fi] == nums[bi]:
                    fi=fi+1
                    if fi==len(nums):
                        return bi+1
            else:
                bi+=1

            if fi != bi and fi<len(nums):
                nums[bi] = nums[fi]
                
            fi+=1
        return bi+1