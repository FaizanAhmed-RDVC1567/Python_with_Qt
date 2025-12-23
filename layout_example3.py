from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout
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
        QVBoxLayout means Vertical box layout.
        QHBoxLayout means Horizontal box layout
        QGridLayout means a grid with coordinates will be used for layout.
        '''
        container = QWidget()
        self.setCentralWidget(container)

        '''
        Now we need to add a layout to the container and then add the labels to the container. This example
        uses QGridLayout which will be applied to the container before adding any labels.
        '''
        layout = QGridLayout(container)

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
        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 1, 0)
        layout.addWidget(label4, 1, 1)
        """
        With a grid layout, we have to specify the coordinates at which the label/widget will be located.
        In the example above:
        0,0 is top left or 1st row & 1st column
        0,1 is top right or 1st row & 2nd column
        1,0 is bottom left or 2nd row & 1st column
        1,1 is bottom right or 2nd row & 2nd column
        """


# Creating the application.
app = QApplication()

window = MainWindow()
window.show()

# To show the application
app.exec()
