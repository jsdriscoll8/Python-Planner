from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class PyPlannerWindow(QMainWindow):
    def __init__(self):
        # Initialize, set title, set size, class vars
        super().__init__()
        self.addButton = None
        self.textbox = None
        self.setWindowTitle("PyPlanner")
        self.setFixedSize(QSize(500, 500))

        # Toolbar
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        # Buttons
        addTaskButton = QAction("Add task", self)
        addTaskButton.setStatusTip("Add task")
        addGoalButton = QAction("Add goal", self)
        addGoalButton.setStatusTip("Add goal")

        # Implement triggers
        addTaskButton.triggered.connect(self.addTask)
        addGoalButton.triggered.connect(self.addGoal)

        # Insert buttons into toolbar
        toolbar.addAction(addTaskButton)
        toolbar.addAction(addGoalButton)

    # Pulls up task layout
    def addTask(self):
        # Textbox
        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(150, 235, 200, 30)
        self.textbox.setPlaceholderText("Add task here")
        self.textbox.show()

        # Textbox submission button & child triggers
        self.addButton = QPushButton("Add", self)
        self.addButton.setGeometry(225, 265, 50, 30)
        self.addButton.setCheckable(True)
        self.addButton.clicked.connect(self.addButtonTrigger)
        self.addButton.show()

    def addGoal(self):
        textbox = QLineEdit("Add goal: ", self)
        textbox.setGeometry(150, 235, 200, 30)
        textbox.show()

    # Trigger function that hides add widgets & submits task info
    def addButtonTrigger(self):
        self.textbox.hide()
        self.addButton.hide()


# Initialization, execution
app = QApplication(sys.argv)
window = PyPlannerWindow()
window.show()

app.exec()