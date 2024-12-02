from typing import Optional
from PySide6.QtWidgets import QWidget



class SettingsTab(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super(SettingsTab, self).__init__(parent)
