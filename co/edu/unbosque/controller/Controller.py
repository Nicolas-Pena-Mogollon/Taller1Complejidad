import time

from co.edu.unbosque.view.View import View
from co.edu.unbosque.model.Model import Sort


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Sort()
        self.coordinateMenu()

    def coordinateMenu(self):

        """
        Coordina el menú de acuerdo a los datos de ingreso, primero pide el tipo de entrada, luego pide la cantidad
        de números a generar si se escogio números aleatorios o pide que se ingresen los números manuales y por
        último pide el ingreso de la opción del tipo de algoritmo para ordenar

        :return: las opciones del menú
        """
        number_type = "3"
        while number_type != "0":
            number_type = self.view.askNumberType()

            # Se pide el tipo de entrada
            if number_type == "0":
                self.view.printData("Gracias!")
                break
            elif number_type == "1":
                # Generados
                array = self.manageOrderOption()
                if len(array) == 0:
                    break

            elif number_type == "2":
                array = self.manageManualOption()

            else:
                self.view.printData("Opción incorrecta")
                continue

            takedTime = self.manageSortOption(array)
            if takedTime == -1:
                number_type = "0"

    def manageSortOption(self, numbers_array):
        """
        De acuerdo con la opción escogida para el algoritmo de ordenamiento, envia el array de números para que sea
        ordenado y lo regresa ya ordenado
        :param numbers_array: array ingresado
        :return: array ordenado de acuerdo al algoritmo de ordenamiento
        """
        sort_option = ""
        while sort_option != "0":
            sort_option = self.view.askSortOption()
            #  Opciones de ordenamiento
            if sort_option == "0":
                self.view.printData("Gracias!")
                return -1
            elif sort_option == "1":
                print("Espere mientras se organizan los valores")
                print("El tiempo obtenido fue: " + str(self.model.doBubbleSort(numbers_array)))
                return 0
            elif sort_option == "2":
                print("Espere mientras se organizan los valores")
                print("El tiempo obtenido fue: " + str(self.model.doSelectionSort(numbers_array)))
                return 0

            elif sort_option == "3":
                print("Espere mientras se organizan los valores")
                beforeTime = time.time()
                self.model.doRadixSort(numbers_array)
                print("El tiempo obtenido fue: " + str((time.time() - beforeTime)))
                return 0

            elif sort_option == "4":
                print("Espere mientras se organizan los valores")
                beforeTime = time.time()
                self.model.quickSort(numbers_array)
                print("El tiempo obtenido fue: " + str((time.time() - beforeTime)))
                return 0
            elif sort_option == "5":
                print("Espere mientras se organizan los valores")
                beforeTime = time.time()
                self.model.merge_sort(numbers_array)
                print("El tiempo obtenido fue: " + str((time.time() - beforeTime)))
                return 0
            else:
                self.view.printData("Opción incorrecta")

    def manageRandomNumOption(self):
        """
        Valida que al ingresar la opción de la longitud de los números aleatorios esta sea escogida para que se
        generen

        :return: opción escogida
        """
        rand_num_option = ""
        while rand_num_option != "0":
            rand_num_option = self.view.askNumberQuantity()
            if rand_num_option == "0":
                return 0
            elif rand_num_option == "1":
                return 4000
            elif rand_num_option == "2":
                return 40000
            elif rand_num_option == "3":
                return 400000
            elif rand_num_option == "4":
                return 4000000
            elif rand_num_option == "5":
                return 40000000
            else:
                self.view.printData("Opción incorrecta")

    def manageOrderOption(self):
        order_option = ""
        while order_option != "0":
            order_option = self.view.askNumbersOrder()

            if order_option == "0":
                return []

            elif order_option == "1":
                quantity = self.manageRandomNumOption()
                if quantity == 0:
                    return []
                print("Espere mientras se generan los números")
                return self.model.createAscendingList(quantity)

            elif order_option == "2":
                quantity = self.manageRandomNumOption()
                if quantity == 0:
                    return []
                print("Espere mientras se generan los números")
                return self.model.createDescendingList(quantity)

            elif order_option == "3":
                quantity = self.manageRandomNumOption()
                if quantity == 0:
                    return []
                print("Espere mientras se generan los números")
                return self.model.createRandomList(quantity)

            else:
                self.view.printData("Opción incorrecta")

    def manageManualOption(self):
        """
        Cuando ingresan los números manualmente, los separa por comas y los guarda en un arreglo. Tambien
        valida que se ingrese solo números

        :return: array con los números ingresados manualmente
        """
        num_array = self.view.askForNumbers().split(",")
        try:
            for i in range(len(num_array)):
                num_array[i] = int(num_array[i].strip())
            return num_array
        except ValueError:
            self.view.printData("Ha ingresado valores diferentes a números!")
            return []
