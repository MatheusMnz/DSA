import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: # type: ignore
        # Inverter os valores para simular uma max-heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Pega os dois maiores elementos (invertidos para simular max-heap)
            element1 = -heapq.heappop(heap) # Elemento 1
            element2 = -heapq.heappop(heap) # Elemento 2

            # Se eles não forem iguais, insira a diferença de volta na heap
            if element1 != element2:
                new_value = element1 - element2
                heapq.heappush(heap, -new_value) # Inserindo o negativo para simular max-heap

        # Se sobrou uma pedra, retorna ela, senão retorna 0
        return -heap[0] if heap else 0
