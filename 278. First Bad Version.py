from math import floor, ceil

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    if version >= 42:
        return True
    else:
        return False

class Solution:
    def firstBadVersion1(self, n: int) -> int:
        lower_bound = 1
        upper_bound = n
        if n == 1:
            return 1
        elif isBadVersion(1):
            return 1
        elif n == 2:
            return 2
        
        while upper_bound > lower_bound:
            current = floor(lower_bound + (upper_bound - lower_bound)/2)
            current_version = isBadVersion(current)

            if current_version:
                if current == lower_bound +1:
                    return current
                else:
                    upper_bound = current
            else:
                if current == upper_bound -1:
                    return upper_bound
                else:
                    lower_bound = current

    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while(left < right):
            middle = floor(left + (right - left)/2)
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left

sol = Solution()
print(sol.firstBadVersion(53))
#1. How is the loop made (for e.g. binary search)? Is it while True or something more clever, preventing possible infinite loops


