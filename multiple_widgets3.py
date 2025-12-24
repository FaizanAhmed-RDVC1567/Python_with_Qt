from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit,
                               QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton, QCheckBox, QHBoxLayout)
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

        # Making some radio button elements, then placing them in a horizontal box container that will be contained
        # inside the vertical box container below the other widget items.
        radio1 = QRadioButton('One')
        radio2 = QRadioButton('Two')
        radio3 = QRadioButton('Three')

        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)
        inner_layout.addWidget(radio1)
        inner_layout.addWidget(radio2)
        inner_layout.addWidget(radio3)

        # Creating a slider bar element, and then adding it to the GUI window. Without any specific code inside the
        # parentheses it will create a vertical slider bar. With a range, we cannot see what value it is referring to
        # when the slider is stopped at a particular range, but that value can be captured using the event that is
        # apparently called something like 'SliderValueChanged'.
        sliderBar = QSlider(Qt.Orientation.Horizontal)
        sliderBar.setRange(0, 100)

        # Simple progress bar without animation and without default value
        progress_bar = QProgressBar()
        progress_bar.setOrientation(Qt.Orientation.Horizontal)
        progress_bar.setRange(0, 100)

        # Now we add the labels and other items to the container
        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(line_edit)
        layout.addWidget(text_edit)
        layout.addWidget(combo_box)
        layout.addWidget(list_widget)
        layout.addWidget(inner_container)
        layout.addWidget(sliderBar)
        layout.addWidget(progress_bar)

        # A note about the above types of UI elements, interacting with them creates 'events' which can be checked
        # for, and an appropriate response be made in response to such events.


# Creating the application.
app = QApplication()

window = MainWindow()
window.show()

# To show the application
app.exec()
