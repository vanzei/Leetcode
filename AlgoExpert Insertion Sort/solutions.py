def insertionSort(array):
    for index in range(1,len(array)):
        j = index
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j-1, array)
            j -= 1
            
    return array

def swap(i, j , array):
    array[i], array[j] = array[j], array[i]

