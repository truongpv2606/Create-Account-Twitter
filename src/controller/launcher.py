import os
import typing
import sys

from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QSharedMemory
from PySide6.QtGui import QIcon

from src.views.window import UIWindow

class SingleApplicationLauncher(QApplication):
    def __init__(self, argv: typing.List[str]):
        super(SingleApplicationLauncher, self).__init__(argv)



    

        self.setWindowIcon(QIcon("resources/icons/icon.png"))
        






        shared  = QSharedMemory("57794896-6574-42e2-b416-386ec659006f", self)
        if not shared.create(1):
            QMessageBox.critical(None, "Error", "An instance of the application is already running.")
            sys.exit(0)

        
        

        self.uiWindow = UIWindow()
        self.uiWindow.show()