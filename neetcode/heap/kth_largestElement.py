import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]): # type: ignore
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Limita o Heap aos K maiores elementos (Elimando sempre o root, que é o menor valor. Min Heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Adiciona o novo valor à estrutura de Heap
        heapq.heappush(self.heap, val)
        # Se o tamanho excecer o limite, removo o root
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
