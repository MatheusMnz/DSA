def rotatedList(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
    
        # Parte Esquerda
        if array[start] <= array[mid]:
            if target > array[mid] or target < array[start]:
                start = mid + 1
            else:
                end = mid - 1
        # Parte direita
        else:
            if target < array[mid] or target > array[end]:
                end = mid - 1
            else:
                start = mid + 1
    return -1 


if __name__ == '__main__':
    numbers = [6,7,8,9,1,2,3,4,5]
    ret = rotatedList(numbers, 4)
    print(f'Index:{ret}\nValue:{numbers[ret]}')
