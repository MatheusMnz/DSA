class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: # type: ignore
        res = []  # Aqui armazenaremos todas as combinações que somam exatamente ao 'target'.
        self.backtrack(candidates, target, [], res, 0)  # Começamos a função 'backtrack' com a lista vazia 'current', 'res' e o índice inicial 0.
        return res  # No final, retornamos todas as combinações possíveis.

    def backtrack(self, candidates, target, current, result, start):
        # Se o alvo (target) for 0, quer dizer que encontramos uma combinação que soma exatamente ao target!
        if target == 0:
            result.append(current[:])  # Adicionamos uma cópia da combinação atual ao resultado.
            return  # Retornamos para parar a execução atual, pois encontramos uma solução.
        
        # Se o alvo for menor que 0, essa combinação não serve, então voltamos (backtrack).
        if target < 0:
            return  # Se passarmos do alvo, não faz sentido continuar, então interrompemos aqui.

        # Agora, começamos o loop para tentar incluir cada número a partir do índice atual 'start'.
        for i in range(start, len(candidates)):
            current.append(candidates[i])  # Adicionamos o número atual ao subconjunto atual.
            # Chamamos a função de backtracking, mas agora o novo alvo é target - candidates[i].
            # Como podemos reutilizar o mesmo número, passamos 'i' como índice inicial, e não 'i + 1'.
            self.backtrack(candidates, target - candidates[i], current, result, i)  
            current.pop()  # Fazemos o 'backtrack' propriamente dito: removemos o último número adicionado.
