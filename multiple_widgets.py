from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit,
                               QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton)
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
        label = QLabel("Label")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Simple button
        button = QPushButton('Click Me')

        # A multi-line space for entering text
        line_edit = QLineEdit()
        # A simple text edit space
        text_edit = QTextEdit()

        # A combobox UI element (basically a drop-down list to choose from)
        combo_box = QComboBox()
        # You have to add items to the combo box in order to make it useful:
        combo_box.addItems(['One', 'Two', 'Three', 'Four'])

        # making a ListWidget element
        list_widget = QListWidget()
        list_widget.addItems(['One', 'Two', 'Three'])

        # Now we add the labels and other items to the container
        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(line_edit)
        layout.addWidget(text_edit)
        layout.addWidget(combo_box)
        layout.addWidget(list_widget)

        # A note about the above types of UI elements, interacting with them creates 'events' which can be checked
        # for, and an appropriate response be made in response to such events.


# Creating the application.
app = QApplication()

window = MainWindow()
window.show()

# To show the application
app.exec()
