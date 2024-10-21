from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int: # type: ignore
        # Clear = 0
        # Shortest Path to Botton Right
        def bfs(grid):
            ROWS, COLS = len(grid), len(grid[0])

            # Corner case: Se o ponto inicial ou final estiver bloqueado
            if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
                return -1

            visit = set()
            queue = deque()

            # Adiciona o nó inicial
            queue.append((0, 0))
            visit.add((0, 0))

            lenght = 1

            # Aplica busca em largura
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    if row == ROWS - 1 and col == COLS -1:
                        return lenght
                    
                    neighbors = [
                        [0, 1],   # direita
                        [0, -1],  # esquerda
                        [1, 0],   # baixo
                        [-1, 0],  # cima
                        [1, 1],   # diagonal inferior direita
                        [1, -1],  # diagonal inferior esquerda
                        [-1, 1],  # diagonal superior direita
                        [-1, -1]  # diagonal superior esquerda
                    ]

                    for dr, dc in neighbors:
                        if (
                            min(row + dr, col + dc) < 0 or 
                            row + dr >= ROWS or
                            col + dc >= COLS or
                            (row + dr, col + dc) in visit or 
                            grid[row + dr][col + dc] == 1
                        ):
                            continue
                        queue.append((row + dr, col + dc))
                        visit.add((row + dr, col + dc))
                
                lenght += 1
            
            return -1
        
        return bfs(grid)