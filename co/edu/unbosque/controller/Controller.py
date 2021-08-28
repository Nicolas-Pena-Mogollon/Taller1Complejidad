from co.edu.unbosque.view.View import View
from co.edu.unbosque.model.Model import Sort


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Sort()
        self.coordinateMenu()

    def coordinateMenu(self):
        option = "5"
        while option != "0":
            typeNumber = self.view.askNumberType()
            if typeNumber == "1":
                print("Numeros aleatorios")
            elif typeNumber == "2":
                print("Numeros manuales")
            else:
                print("Opción incorrecta")
                continue

            option = self.view.askSortOption()
            if option == "1":
                self.model.doBubbleSort()
            elif option == "2":
                self.model.doBubbleSort()
            elif option == "3":
                self.model.doBubbleSort()
            elif option == "4":
                self.model.doBubbleSort()
            elif option == "5":
                self.model.doBubbleSort()
            else:
                print("Opción incorrecta")
                continue
