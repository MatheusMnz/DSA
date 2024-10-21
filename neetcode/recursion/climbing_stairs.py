class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        # Degrau 0, uma maneira de estar ali
        # Degrau 1, um passo
        # Degrau 2, um passo tamanho 2 saindo do 0
        # Ou um passo tamanho 1, saindo de 1

        if n in memo:
            return memo[n]

        if n==0 or n==1:
            return 1

        memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n]