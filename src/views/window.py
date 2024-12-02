

from PySide6.QtWidgets import QMainWindow, QApplication, QStyle, QWidget, QHBoxLayout, QTabWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


from typing import Union, Optional

from src.views.tabs.dashboard import DashboardTab
from src.views.tabs.process import ProcessTab
from src.views.tabs.settings import SettingsTab


class UIWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None):
        super(UIWindow, self).__init__(parent)

        self.__initUi()



        

    def __initUi(self):
        self.resize(1600, 700)

        self.centralWidget = QWidget()  


        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        self.tabWidget = QTabWidget()



        self.dashboardTab = DashboardTab()
        self.processTab = ProcessTab()
        self.settingsTab = SettingsTab()

        self.tabWidget.addTab(self.dashboardTab, "Quản lý tài khoản")
        self.tabWidget.addTab(self.processTab, "Quản lý tiến trình")
        self.tabWidget.addTab(self.settingsTab, "Cài đặt")
        self.verticalLayout.addWidget(self.tabWidget)

  





        self.centralWidget.setLayout(self.verticalLayout)

        self.setCentralWidget(self.centralWidget)

     
        screen = QApplication.primaryScreen()
        rect = screen.availableGeometry()
        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                self.size(),
                rect
            )
        )




    

