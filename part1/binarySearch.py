def binary_search(array, valor_procurado):
    inicio = 0
    fim = len(array) - 1

    while inicio <= fim:
        mid = (inicio + fim) // 2

        # Se encontramos o valor
        if array[mid] == valor_procurado:
            return mid

        # Se o valor está à esquerda do meio
        elif array[mid] > valor_procurado:
            fim = mid - 1

        # Se o valor está à direita do meio
        else:
            inicio = mid + 1

    return -1  # Valor não encontrado


if __name__ == '__main__':
    numbers = [ 1,2,3,4,5,6,7,8,9]
    ret = binary_search(numbers, 2)
    print(f'Index:{ret}\nValue:{numbers[ret]}')

