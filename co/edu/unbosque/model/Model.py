import random


class Sort:
    def __init__(self):
        pass

    def doBubbleSort(self, array):
        for i in range(len(array) - 1):
            for j in range(i, len(array)):
                if array[i] > array[j]:
                    aux = array[i]
                    array[i] = array[j]
                    array[j] = aux
        return array

    def createRandomList(self, quantity):
        randomList = []
        for i in range(quantity):
            randomList.append(random.randint(0, quantity))
        return randomList

    def doSelectionSort(self, array):
        for i in range(len(array)):
            minim = i
            for j in range(i, len(array)):
                if array[j] < array[minim]:
                    minim = j
            if minim != i:
                orderedNum = array[i]
                array[i] = array[minim]
                array[minim] = orderedNum

        return array

    def doRadixSort(self, array):
        for i in range(len(array)):
            array

    def doQuickSort(self, array):
        left = []
        center = []
        right = []
        if len(array) > 1:
            pivot = array[0]
            for i in array:
                if i < pivot:
                    left.append(i)
                elif i == pivot:
                    center.append(i)
                elif i > pivot:
                    right.append(i)
            return self.doQuickSorto(left) + center + self.doQuickSorto(right)
        else:
            return array

    def doMergeSort(self, array):
        for i in range(len(array)):
            array
