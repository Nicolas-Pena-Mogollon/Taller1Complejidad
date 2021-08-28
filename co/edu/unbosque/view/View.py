class View:
    def __init__(self):
        pass

    def askSortOption(self):
        print("Escoja el algoritmo que quiere usar")
        option = input("1. Ordenamiento Burbuja \n2. Ordenamiento Selección "
                       "\n3. Ordenamiento Radix \n4. Ordenamiento QuickSort"
                       "\n5. Ordenamiento MergeSort")
        return option

    def askNumberType(self):
        print("Escoja el tipo de ingreso de datos: ")
        numberType = input("1. Números aleatorios \n2. Ingreso manual")

        return numberType
