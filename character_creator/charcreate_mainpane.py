#Import and Library Management
import sys;
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox;

#QT Application Window Initialization Instance
app = QApplication(sys.argv)
window = QWidget() #-- Pass to all window variables to connect to this window, other windows will be defined likewise.
window.setWindowTitle("Character TTRPG Creator")
window.setGeometry(300, 300, 500, 750)

layout = QVBoxLayout()

#Example Label Text Field to interact with the QT Window
label = QLabel("This is a Label", window)
layout.addWidget(label)
text_field = QLineEdit(window)
text_field.setPlaceholderText("Enter Text Here...")
layout.addWidget(text_field)

def submit_action():
    user_input = text_field.text().strip()

    if user_input:
        QMessageBox.information(window, "Input Recieved", f"Hello, {user_input}")
    else:
        QMessageBox.warning(window, "No Input", "Please Enter Your Name.")

## Submits that which is connected to the interface.
submit_button = QPushButton("Submit", window)
submit_button.clicked.connect(submit_action)
layout.addWidget(submit_button)

## Quits out of the window view.
quit_button = QPushButton("Quit", window)
quit_button.clicked.connect(window.close)
layout.addWidget(quit_button)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
