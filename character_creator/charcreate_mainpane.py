#
# ------------------------------------------------------------------
#  
# Character Creator Development - Project Dice Muncher
#
#
#   Version:                  0.0.1
#   Date Started:             02-02-2026
#   GPL-3.0 License(s):       Open Source and Open Curated Content
#   Development Curated By:   ZA Entertainment L.L.C.
#   Developed By:             Jace Zavarelli
#
# ------------------------------------------------------------------
#

# Import and Library Management
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMenuBar, QMenu, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon

# * Core class for the Character application to hold the tables and items that will appear during execution, will preceed the application start interface, an exterior class on launch. 
class CharMainPane(QWidget):

    ## -------- INIT CALLS ----------------------------------------------------------------

    # Initialization Class for the Applications initialized Window settings, Allows use of SELF from Super().
    def __init__(self):
        #-- Allows for the Base Class to be set properly while inheriting it. 
        super().__init__()
        icon_pathdir : str = r"..\assets\icons\dice_logo_icon.png"
        self.setWindowIcon(QIcon(icon_pathdir))
        self.setWindowTitle("Project Dice Muncher")
        self.setGeometry(300, 300, 1000, 750)

        self.setStyleSheet(
            """
            QWidget {
    
            }

            QLabel {
            
            }
            """
        )

        self._createCharMenuBar()
        self.charMenu_ui()

    def _createCharMenuBar(self):
        menuCharBar = QMenuBar(self)
        self.setMenuBar(menuCharBar)

        fileMenu = QMenu("&File", self)
        self.menuCharBar.addMenu(self.fileMenu)

        editMenu = self.menuCharBar.addMenu("&Edit")
        helpMenu = self.menuCharBar.addMenu("&Help")

    ## -------- WINDOW CALLS ----------------------------------------------------------------

    # User Interface Class that Holds Widgets and QT Application Button Prompting.
    def charMenu_ui(self):

        #TODO - Setup the initial configuration and button structure of the main window and file menu bar heirarchy. 
        mainpaneLayout = QVBoxLayout()

        self.label = QLabel("This is a Label")
        mainpaneLayout.addWidget(self.label)

        self.text_field = QLineEdit()
        self.text_field.setPlaceholderText("Enter Text Here...")
        mainpaneLayout.addWidget(self.text_field)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_action)
        mainpaneLayout.addWidget(self.submit_button)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)
        mainpaneLayout.addWidget(self.quit_button)

        self.setLayout(mainpaneLayout)


    ## -------- FUNCTION CALLS ----------------------------------------------------------------

    # Submit Application (Reaction Script for when button is pressed).
    def submit_action(self):
        user_input = self.text_field.text().strip()

        if user_input:
            QMessageBox.information(self, "Input Recieved", f"Hello, {user_input}")
        else:
            QMessageBox.warning(self, "No Input", "Please Enter Your Name.")


# TODO - Articulate to align with proper execution for Window Execution.
# * Main Calling Method instantiating the CharMainPane for execution when ran.
if __name__ == "__main__":
    charTTRPGapp = QApplication(sys.argv)
    window = CharMainPane()
    window.show()
    sys.exit(charTTRPGapp.exec())
