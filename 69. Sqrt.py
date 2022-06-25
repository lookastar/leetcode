class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1: return 1
        lb = 0
        rb = x

        while lb <= rb:
            mid = (lb + rb)//2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid * mid < x:
                lb = mid
            else:
                rb = mid
