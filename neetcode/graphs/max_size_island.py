class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: # type: ignore
        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])

            # Caso seja uma célula fora dos limites ou já visitada (0), retorna 0
            if (min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0):
                return 0
            
            # Marca a célula atual como visitada, convertendo-a em água (0)
            grid[r][c] = 0

            # Conta a célula atual como parte da ilha
            count = 1

            # Expande para baixo, cima, direita e esquerda
            count += dfs(grid, r + 1, c)
            count += dfs(grid, r - 1, c)
            count += dfs(grid, r, c + 1)
            count += dfs(grid, r, c - 1)

            return count

        if not grid:
            return 0
        
        max_size = 0
        ROWS, COLS = len(grid), len(grid[0])

        # Aplica o DFS para cada célula, expandindo pela ilha
        for r in range(ROWS):
            for c in range(COLS):
                # Busca somente em células de Ilhas (1)
                if grid[r][c] == 1:
                    # Calcula o tamanho da ilha usando DFS e atualiza o máximo
                    max_size = max(max_size, dfs(grid, r, c))
        
        return max_size
