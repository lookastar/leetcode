class Solution:
    def fib2(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        ans, prev_n = 1, 0
        for i in range(2, n+1):
            temp = ans
            ans = ans + prev_n
            prev_n = temp
        return ans

    def fib(self, n: int, memo = {}) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n in memo.keys(): return memo[n]
        memo[n] = Solution.fib(self, n-1, memo) + Solution.fib(self, n-2, memo)
        return memo[n]

sol = Solution
print("Fibonacci of 2 is", sol.fib(sol, 2))
print("Fibonacci of 3 is", sol.fib(sol, 3))
print("Fibonacci of 4 is", sol.fib(sol, 4))
print("Fibonacci of 5 is", sol.fib(sol, 5))
print("Fibonacci of 6 is", sol.fib(sol, 6))
print("Fibonacci of 30 is", sol.fib(sol, 30))
print("Fibonacci of 50 is", sol.fib(sol, 50))