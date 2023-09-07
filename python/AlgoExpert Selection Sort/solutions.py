def selectionSort(array):
    currentIndex = 0
    while currentIndex < len(array)-1:
        smallestindex = currentIndex
        for i in range(smallestindex + 1, len(array)):
            if array[smallestindex] > array[i]:
                smallestindex = i
        swap(currentIndex, smallestindex,array)
        currentIndex +=1
    return array

def swap(value1, value2, array):
    array[value1],array[value2] = array[value2],array[value1]
