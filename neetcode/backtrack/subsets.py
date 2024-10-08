def subsets(nums):
    result = []
    
    # Função auxiliar para gerar os subconjuntos com backtracking
    def backtrack(start, current):
        print(f"Chamada: start={start}, current={current}")
        result.append(current[:])  # Adiciona o subconjunto atual ao resultado
        print(f"Subconjunto adicionado: {current[:]}")
        
        # Itera sobre os números a partir de 'start'
        for i in range(start, len(nums)):
            print(f"Incluindo {nums[i]} no subconjunto atual.")
            current.append(nums[i])  # Inclui nums[i] no subconjunto atual
            print(f"Subconjunto atualizado: {current}")
            
            backtrack(i + 1, current)  # Recursão para os próximos elementos
            
            print(f"Backtracking, removendo {current[-1]} do subconjunto.")
            current.pop()  # Remove o último elemento para voltar atrás
            print(f"Subconjunto após remoção: {current}")
    
    # Inicia o processo com um subconjunto vazio
    backtrack(0, [])
    
    return result


nums = [1, 2, 3]
print(f"Subconjuntos de {nums}:")
result = subsets(nums)
print("\nResultado final:", result)
