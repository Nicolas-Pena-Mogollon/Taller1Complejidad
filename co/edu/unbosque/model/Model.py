import random
import time


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
        for i in range(len(array) - 1):
            minim = i
            for j in range(i + 1, len(array)):
                if array[j] < array[minim]:
                    minim = j
            if minim != i:
                ordered_num = array[i]
                array[i] = array[minim]
                array[minim] = ordered_num
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
            return self.doQuickSort(left) + center + self.doQuickSort(right)
        else:
            return array

    # Función merge_sort
    def merge_sort(self,lista):

        """
        Lo primero que se ve en el psudocódigo es un if que
        comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
        ¿Por que? Ya esta ordenada.
        """
        if len(lista) < 2:
            return lista

        # De lo contrario, se divide en 2
        else:
            middle = len(lista) // 2
            right = self.merge_sort(lista[:middle])
            left = self.merge_sort(lista[middle:])
            return self.merge(right, left)

    # Función merge
    def merge(self,lista1, lista2):
        """
        merge se encargara de intercalar los elementos de las dos
        divisiones.
        """
        i, j = 0, 0  # Variables de incremento
        result = []  # Lista de resultado

        # Intercalar ordenadamente
        while (i < len(lista1) and j < len(lista2)):
            if (lista1[i] < lista2[j]):
                result.append(lista1[i])
                i += 1
            else:
                result.append(lista2[j])
                j += 1

        # Agregamos los resultados a la lista
        result += lista1[i:]
        result += lista2[j:]

        # Retornamos el resultados
        return result
