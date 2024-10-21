import heapq
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min-Heap para armazenar tuplas (distância, ponto)
        heap = []

        # Calculando a distância e adicionando a tupla (distância, ponto) ao heap
        for point in points:
            x, y = point
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (distance, point))

        # Resultado armazenará os 'k' pontos mais próximos
        res = []
        for _ in range(k):
            # Pegar apenas o ponto (não a distância)
            res.append(heapq.heappop(heap)[1])  

        return res
