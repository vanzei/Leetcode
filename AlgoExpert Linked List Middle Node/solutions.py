# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    lenList = Linkedlen(linkedList)
    mid = linkedList 
    for value in range(lenList//2):
        mid = mid.next
    return mid


def Linkedlen(linkedList):
    count = 0
    currentNode = linkedList
    while currentNode is not None:
        count += 1
        currentNode = currentNode.next
    return count
