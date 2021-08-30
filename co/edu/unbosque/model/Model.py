import random
import time


class Sort:
    def __init__(self):
        pass

    def createRandomList(self, quantity):
        """
        Genera una lista de números aleatorios de acuerdo a la cantidad que se pida

        :param quantity: tamaño de la lista de número aleatorios
        :return: lista de números aleatorios
        """
        randomList = []
        for i in range(quantity):
            randomList.append(random.randint(0, quantity))
        return randomList

    def doBubbleSort(self, array):
        """
        Ordena el arreglo comparando cada número del arreglo con los demás números
        de este y si alguno de estos es menor, intercambia la posición

        :param array: arreglo desordenado
        :return: arreglo ordenado
        """
        for i in range(len(array) - 1):
            for j in range(i, len(array)):
                if array[i] > array[j]:
                    aux = array[i]
                    array[i] = array[j]
                    array[j] = aux
        return array

    def doSelectionSort(self, array):
        """
        Ordena el arreglo guardando la posición del número mínimo, que se obtiene comparando
        el número de la posición del supuesto número mínimo con los números de las demás posiciones.
        Luego de esto, si la posición del número mínimo cambió, se intercambian la posición del número
        mínimo anterios y la del nuevo

        :param array: arreglo desordenado
        :return: arreglo ordenado
        """
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
        """
        Crea un arreglo bidimensional de 1x10 y almacena los números en este según su valor posicional (decimales)
        y su dígito más significativo, luego de esto, los sobrescribe el arreglo original en ese nuevo orden,
        buscando desde unidades, decenas, en adelante.

        :param array: arreglo desordenado
        :return: arreglo ordenado
        """
        bucketsLength = 10
        maxLenNum = False
        decimalCount = 1  # Se inicializa decimalCount en 1
        while not maxLenNum:
            maxLenNum = True
            buckets = [list() for _ in range(bucketsLength)]  # Creación arreglo bidimensional

            for i in array:
                # Se divide el elemento del arreglo entre unidad, decena, etc, dependiendo el recorrido
                tmp = int(i / decimalCount)
                # Se determina en que sub arreglo se va a añadir y se agrega
                buckets[tmp % bucketsLength].append(i)
                # Determina si ese número es el más largo
                if maxLenNum and tmp > 0:
                    maxLenNum = False

            arrayPos = 0
            # Se sobrescribe el arreglo original con los números en el orden en el que estan en el arreglo buckets
            for j in range(bucketsLength):
                buck = buckets[j]
                for i in buck:
                    array[arrayPos] = i
                    arrayPos += 1
            decimalCount *= bucketsLength
        return array

    def doQuickSort(self, array):
        """
        Ordena el arreglo, dividiendolo en tres sub listas, donde el pivote es el primer número del arreglo.
        Las sublistas se llenan con los números menores que el pivote a la lista izquierda, mayores a la lista derecha
        e iguales a la lista centro, luego, hace una llamada recursiva con la lista de la izquierda y la derecha,
        concatenandolas con la del centro

        :param array: arreglo desordenado
        :return: arreglo ordenado
        """
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

    def merge_sort(self, array):
        """
        Divide el arreglo por la mitad y con llamadas recursivas continua dividiendolo hasta que queden arreglos
        individuales, para luego retornar el resultado de la mezcla de estos hasta obtener el arreglo principal

        :param array: arreglo desordenado
        :return: arreglo ordenado
        """
        if len(array) < 2:  # Si es menor que dos, no se divide y lo retorna
            return array


        else:
            middle = len(array) / 2  # Se divide la longitud del arreglo a la mitad
            right = self.merge_sort(array[:middle])  # Merge sort a la primera mitad
            left = self.merge_sort(array[middle:])  # Merge sort a la segunda mitad
            return self.merge(right, left)

    def merge(self, right, left):

        """
        Se intercala y ordena la división de los arreglos, comparando los números de ambos

        :param right: primera mitad del arreglo
        :param left: segunda mitad del arreglo
        :return: resultado de ordenar los arreglos
        """
        i = 0
        j = 0
        result = []

        '''
        Compara los números de ambos arreglos,hasta que en la lista de resultados se hayan incluido todos los números
        de alguna de ambas listas
        '''
        while i < len(right) and j < len(left):
            if right[i] < left[j]:
                result.append(right[i])
                i += 1
            else:
                result.append(left[j])
                j += 1

        # Se añaden a la lista resultante los números faltantes
        result += right[i:]
        result += left[j:]

        return result
