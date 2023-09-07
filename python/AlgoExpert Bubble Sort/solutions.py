def bubbleSort(array):
    counter = 0
    isSorted = False
    while not isSorted:
        isSorted = True
        for index in range(len(array) - 1 - counter):
            if array[index] > array[index + 1]:
                swap(index, index + 1 , array)
                isSorted = False
        counter += 1
    return array
                
def swap(left, right, array):
    array[left], array[right] = array[right], array[left]
