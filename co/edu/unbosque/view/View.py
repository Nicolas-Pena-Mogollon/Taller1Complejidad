class View:
    def __init__(self):
        pass

    def askSortOption(self):
        """
            Menú para pedir el tipo de algoritmo de ordenamiento

        :return: opción del menú escogida
        """
        option = input("Escoja el algoritmo que quiere usar\n0. Salir\n1. Ordenamiento Burbuja" +
                       "\n2. Ordenamiento Selección\n3. Ordenamiento Radix\n4. Ordenamiento QuickSort" +
                       "\n5. Ordenamiento MergeSort")
        return option

    def askNumberQuantity(self):
        """
            Menú para pedir la cantidad de números a generar en aleatorio

        :return: opción del menú escogida
        """
        option = input("Escoja la cantidad de numeros a generar\n0. Salir\n1. 4000\n2. 40000" +
                       "\n3. 400000 Números \n4. 4000000\n5. 40000000")
        return option

    def askNumberType(self):
        """
            Menú para pedir que tipo de entrada solicitar (aleatoria o manual)

        :return: opción del menú escogida
        """
        numberType = input("Escoja el tipo de ingreso de datos:\n0. Salir\n1. Números aleatorios" +
                           "\n2. Ingreso manual")
        return numberType

    def askForNumbers(self):
        """
            Ingreso de los números escogidos manualmente

        :return: opción del menú escogida
        """
        numbers = input("Ingrese los números separados por comas ej: '1,2,3'")
        return numbers

    def printData(self, data):
        print(data)
