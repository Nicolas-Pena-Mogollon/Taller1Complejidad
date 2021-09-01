class View:
    def __init__(self):
        pass

    def askSortOption(self):
        """
        Pide el tipo de algoritmo de ordenamiento

        :return: opción del menú escogida
        """
        option = input("Escoja el algoritmo que quiere usar\n0. Salir\n1. Ordenamiento Burbuja" +
                       "\n2. Ordenamiento Selección\n3. Ordenamiento Radix\n4. Ordenamiento QuickSort" +
                       "\n5. Ordenamiento MergeSort")
        return option

    def askNumberQuantity(self):
        """
        Pide la cantidad de números a generar en aleatorio

        :return: opción del menú escogida
        """
        option = input("Escoja la cantidad de numeros a generar\n0. Salir\n1. 4000\n2. 40000" +
                       "\n3. 400000 Números \n4. 4000000\n5. 40000000")
        return option

    def askNumberType(self):
        """
        Pide que tipo de entrada solicitar (aleatoria o manual)

        :return: opción del menú escogida
        """
        numberType = input("Escoja el tipo de ingreso de datos:\n0. Salir\n1. Números aleatorios" +
                           "\n2. Ingreso manual")
        return numberType

    def askForNumbers(self):
        """
        Pide y recibe los números escogidos manualmente

        :return: opción del menú escogida
        """
        numbers = input("Ingrese los números separados por comas ej: '1,2,3'")
        return numbers

    def askNumbersOrder(self):
        """
        Pide el tipo de orden que se quiera usar

        :return: opción del menú escogida
        """
        option = input("¿Qué orden desea?\n0. Salir\n1. Ascendente\n2. Descendente" +
                       "\n3. Aleatorio")
        return option

    def printData(self, data):
        """
        Imprime la información ingresada

        :param data: la información a imprimir
        """
        print(data)
