"""
Created on Sept 6,2021

@author: Nicolás Peña Mogollón - María Camila Lozano Gutiérrez
"""

from co.edu.unbosque.controller.Controller import Controller


class Main:
    def __init__(self=None):
        self.controller = Controller()


if __name__ == "__main__":
    try:
        main = Main()
    except KeyboardInterrupt:
        print('Interrupted')
        exit()
