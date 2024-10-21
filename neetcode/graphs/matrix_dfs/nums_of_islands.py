class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: # type: ignore
        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])

            # Caso seja um nó visitado ou água, passa para a próxima célula
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == '0'):
                return 
            
            # Marca célula como visitada
            visit.add((r, c))

            # Percorre toda a ilha
            dfs(grid, r + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c - 1, visit)

        if not grid:
            return 0
        
        visit = set()
        islands = 0

        ROWS, COLS = len(grid), len(grid[0])

        # Aplica o DFS para célula, expandindo pela ilha
        for r in range(ROWS):
            for c in range(COLS):
                # Busca somente em células de Ilhas
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(grid, r, c, visit)
                    islands += 1
        
        return islands
            