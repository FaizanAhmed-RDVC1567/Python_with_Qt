from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()

        # After the above line, UI elements can be added. The term 'self' will refer to the window
        # in this scope.
        self.setWindowTitle('Hello World Application')

        # Label for the app
        label = QLabel("Hello World")

        # To align the label in the center
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # As we have only one widget, we can just add the above label and set it as the central widget
        self.setCentralWidget(label)


# Creating the application.
app = QApplication()

window = MainWindow()
window.show()

# To show the application
app.exec()
