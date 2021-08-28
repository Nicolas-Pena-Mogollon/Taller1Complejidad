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
