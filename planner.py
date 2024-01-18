from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class PyPlannerWindow(QMainWindow):
    def __init__(self):
        # Initialize, set title, set size
        super().__init__()
        self.buttonChecked = False
        self.setWindowTitle("PyPlanner")
        self.setFixedSize(QSize(1000, 500))

        # Draw UI components
        self.uiComponents()


    def uiComponents(self):
        # Create task button in top left corner, listening for click
        button = QPushButton("Create task", self)
        button.setGeometry(0, 0, 333, 125)
        button.setCheckable(True)

        button.clicked.connect(self.createTaskToggled)

    def createTaskToggled(self):
        self.buttonChecked = True
        print(self.buttonChecked)

app = QApplication(sys.argv)
window = PyPlannerWindow()
window.show()

app.exec()