from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()

        # After the above line, UI elements can be added. The term 'self' will refer to the window
        # in this scope.
        self.setWindowTitle('Hello World Application')

        '''
        The widget is a container, you can put different UI elements as necessary into a container like QWidget.
        let's place multiple labels into the widget and display it on the screen, with a layout that defines how
        each label will be displayed.
        VBoxLayout means Vertical box layout.
        HBoxLayout means Horizontal box layout
        '''
        container = QWidget()
        self.setCentralWidget(container)

        '''
        Now we need to add a layout to the container and then add the labels to the container. This example
        uses VBoxLayout which will be applied to the container before adding any labels.
        '''
        layout = QVBoxLayout(container)

        # Labels for the app to be displayed inside a container like QWidget
        label1 = QLabel("One")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label2 = QLabel("Two")
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label3 = QLabel("Three")
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label4 = QLabel("Four")
        label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Now we add the labels to the container
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


# Creating the application.
app = QApplication()

window = MainWindow()
window.show()

# To show the application
app.exec()
