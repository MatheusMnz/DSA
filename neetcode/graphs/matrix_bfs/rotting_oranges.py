from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: # type: ignore
        ROWS, COLS  = len(grid), len(grid[0])

        queue = deque()
        fresh_orange = 0

        # Adiciona somente a laranjas inicialmente podres na queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_orange += 1
                
            
        if fresh_orange == 0:
            return 0
    
        # (direita, esquerda, baixo, cima)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0  
        
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()

                # Contamina os vizinhos
                for dr, dc in directions:
                    # Fresca e dentro dos limites
                    if (
                        row + dr < 0 or row + dr >= ROWS or
                        col + dc < 0 or col + dc >= COLS or
                        grid[row + dr][col + dc] != 1
                       ):
                       continue
                
                    # Contamina
                    grid[row + dr][col + dc] = 2
                    queue.append((row + dr, col + dc))
                    fresh_orange -= 1
        
        # Subtrai 1 minuto, pois na ultima rodada posso ter laranja podre na fila
        # Mesmo todas estando contaminadas
        return minutes - 1 if fresh_orange == 0 else -1