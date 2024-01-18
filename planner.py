from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class PyPlannerWindow(QMainWindow):
    def __init__(self):
        # Initialize, set title, set size
        super().__init__()
        self.setWindowTitle("PyPlanner")
        self.setFixedSize(QSize(1000, 500))

        # Draw UI components
        self.uiComponents()

    def uiComponents(self):
        # Create task button in top left corner
        button = QPushButton("Create task", self)
        button.setGeometry(0, 0, 333, 125)


app = QApplication(sys.argv)

window = PyPlannerWindow()
window.show()

app.exec()