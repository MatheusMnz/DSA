class HashTable:
    def __init__(self):
        self.MAX = 10
        # Cada índice agora armazena uma lista para lidar com colisões (Chaining)
        self.array = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        # Calcula o índice hash com base na soma dos valores ASCII dos caracteres
        ascii_value = sum(ord(char) for char in key)
        return ascii_value % self.MAX
    
    # Dunder method para adicionar itens
    def __setitem__(self, key, val):
        hash_index = self.get_hash(key)

        # Verifica se a chave já existe e atualiza o valor, se necessário
        for index, element in enumerate(self.array[hash_index]):
            if element[0] == key:  # Verifica se a chave já está presente
                self.array[hash_index][index] = (key, val)  # Atualiza o valor
                return
        # Caso a chave não exista, insere o novo par (chave, valor)
        self.array[hash_index].append((key, val))

    # Dunder method para obter itens
    def __getitem__(self, key):
        hash_index = self.get_hash(key)
        for element in self.array[hash_index]:
            if element[0] == key:
                return element[1]  # Retorna o valor associado à chave
        # Se a chave não for encontrada, lança uma exceção
        raise KeyError(f'{key} não encontrado')

    # Dunder method para deletar itens
    def __delitem__(self, key):
        hash_index = self.get_hash(key)
        for index, element in enumerate(self.array[hash_index]):
            if element[0] == key:
                del self.array[hash_index][index]  # Deleta o par (chave, valor)
                return
        # Se a chave não for encontrada, lança uma exceção
        raise KeyError(f'{key} não encontrado')


if __name__ == '__main__':
    t = HashTable()

    # Inserindo valores
    t['march 6'] = 130
    t['June 8'] = 202
    t['march 17'] = 777

    # Acessando valores
    print(f"Valor de 'march 6': {t['march 6']}")
    print(f"Valor de 'June 8': {t['June 8']}")

    # Exibindo a tabela antes e depois de deletar
    print(f'Hash Table antes de deletar March 17: {t.array}')
    del t['march 17']
    print(f'Hash Table após deletar March 17: {t.array}')
