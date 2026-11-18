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

# Import and Library Management
import os
import sys

from pathlib    import Path
from typing     import Final

from roleplaycharcreator_za_app.theme_manager          import ( ThemeManager, ThemeMode )

from PySide6.QtCore         import ( Qt, Slot )
from PySide6.QtGui          import ( QAction, QActionGroup, QKeySequence )
from PySide6.QtWidgets      import ( QApplication, QFrame, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QSplitter, QStackedWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget )

# System Suspression Management
os.environ["QT_LOGGING_RULES"] = "qt.qpa.wayland.textinput=false"

# Global Variables

### - Shortcuts
OPEN_SHORTCUT: Final[QKeySequence]      = QKeySequence.StandardKey.Open #(ctrl + O / cmd + O)
CLOSE_SHORTCUT: Final[QKeySequence]     = QKeySequence.StandardKey.Quit #(ctrl + Q / cmd + Q)
SAVE_SHORTCUT: Final[QKeySequence]      = QKeySequence.StandardKey.Save #(ctrl + S / cmd + S)
SAVEAS_SHORTCUT: Final[QKeySequence]    = QKeySequence.StandardKey.SaveAs #(ctrl + shift + S / cmd + shift + S)

## ---------------------------------------------------------------------------------------------------------------- ##
##                                        Module Panes                                                              ##
## ---------------------------------------------------------------------------------------------------------------- ##

## ---------------------------------------------------------------------------------------------------------------- ##
##                                        Character Pane                                                            ##
## ---------------------------------------------------------------------------------------------------------------- ##
# Core class for the Character application to hold the tables and items that will appear 
# during execution, will preceed the application start interface, an exterior class on launch. 
class CharMainPane(QMainWindow):

    ##-------------------------------------
    ## -------- INIT CALLS ----------------
    ##-------------------------------------

    def __init__(self):
        super().__init__()
        # WINDOW CONFIG
        self.setWindowTitle("Character Creator")
        self.resize(1000,500)

        # STATUS MENU BAR CONFIG

        # -- Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        setting_menu = menu_bar.addMenu("&Settings")
        tool_menu = menu_bar.addMenu("&Tools")
        help_menu = menu_bar.addMenu("&Help")

        # -- File Menu 
        open_action = QAction("&Open...", self)
        open_action.setShortcut(OPEN_SHORTCUT)
        open_action.triggered.connect(self.open_file_dialog)
        file_menu.addAction(open_action)

        save_action = QAction("&Save", self)
        save_action.setShortcut(SAVE_SHORTCUT)
        #save_action.triggered.connect(self.open_file_dialog)
        file_menu.addAction(save_action)

        saveas_action = QAction("&Save As...", self)
        saveas_action.setShortcut(SAVEAS_SHORTCUT)
        #saveas_action.triggered.connect(self.open_file_dialog)
        file_menu.addAction(saveas_action)

        exit_action = QAction("&Exit", self)
        exit_action.setShortcut(CLOSE_SHORTCUT)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # -- Setting Menu 
        theme_submenu = setting_menu.addMenu("&Theme")

        # --- Theme Options
        self.theme_action_group = QActionGroup(self)
        self.theme_action_group.setExclusive(True)

        self.action_lightmode = QAction("&Light Mode", self)
        self.action_lightmode.setCheckable(True)
        self.theme_action_group.addAction(self.action_lightmode)
        theme_submenu.addAction(self.action_lightmode)

        self.action_darkmode = QAction("&Dark Mode", self)
        self.action_darkmode.setCheckable(True)
        self.theme_action_group.addAction(self.action_darkmode)
        theme_submenu.addAction(self.action_darkmode)

        self.theme_action_group.triggered.connect(self.change_theme)
        self.action_darkmode.setChecked(True)
        self.change_theme(self.action_darkmode)

        # _action = QAction("&", self)
        # _action.setShortcut(_SHORTCUT)
        # _action.triggered.connect(self.)
        # setting_menu.addAction(_action)

        # -- Tool Menu 
        create_item_action = QAction("&Create Item...", self)
        # create_item_action.setShortcut(_SHORTCUT)
        # create_item_action.triggered.connect(self.)
        tool_menu.addAction(create_item_action)

        create_spell_action = QAction("&Create Spell...", self)
        # create_spell_action.setShortcut(_SHORTCUT)
        # create_spell_action.triggered.connect(self.)
        tool_menu.addAction(create_spell_action)

        # _action = QAction("&", self)
        # _action.setShortcut(_SHORTCUT) 
        # _action.triggered.connect(self.)
        # tool_menu.addAction(_action)

        # -- Help Menu
        wiki_action = QAction("&Wiki", self)
        # wiki_action.setShortcut(_SHORTCUT) 
        # wiki_action.triggered.connect(self.)
        help_menu.addAction(wiki_action)

        # _action = QAction("&", self)
        # _action.setShortcut(_SHORTCUT) 
        # _action.triggered.connect(self.)
        # help_menu.addAction(_action)

        # SPLIT PANE
        self.split_box = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(self.split_box)

        # LEFT PANE
        self.nav_widget = QTreeWidget()
        self.nav_widget.setHeaderHidden(True)
        self.nav_widget.setColumnCount(1)
        self.split_box.addWidget(self.nav_widget)

        # RIGHT PANE
        self.module_widget = QStackedWidget()
        self.split_box.addWidget(self.module_widget)

        # SPLIT CONFIG  
        self.split_box.setSizes([220,630])
        self.getNavigationTree()

        self.nav_widget.currentItemChanged.connect(self.set_nav_select)


    # def setModuleView(self):

    #     #TBD

    def getNavigationTree(self):

        # First-Level Character Modules
        character_section = QTreeWidgetItem(self.nav_widget, ["Character Sheet"])
        character_section.setExpanded(True)

        # -- Character Sub Items
        overview_tab = QTreeWidgetItem(character_section, ["Overview"])
        # sub_item_a.setData(0, Qt.ItemDataRole.UserRole, self.idx_attribute)

        attribute_tab = QTreeWidgetItem(character_section, ["Attributes"])
        # sub_item_a.setData(0, Qt.ItemDataRole.UserRole, self.idx_attribute)

        ability_tab = QTreeWidgetItem(character_section, ["Abilities"])
        # sub_item_a.setData(0, Qt.ItemDataRole.UserRole, self.idx_attribute)

        inventory_tab = QTreeWidgetItem(character_section, ["Inventory"])
        # sub_item_a.setData(0, Qt.ItemDataRole.UserRole, self.idx_attribute)

        # Second-Level Shop Modules
        shop_section = QTreeWidgetItem(self.nav_widget, ["Item Shop"])

        # -- Shop Sub Items
        overview_tab = QTreeWidgetItem(shop_section, ["Item Selection"])
        # sub_item_a.setData(0, Qt.ItemDataRole.UserRole, self.idx_attribute)

        attribute_tab = QTreeWidgetItem(shop_section, ["Add Item"])
        # sub_item_a.setData(0, Qt.ItemDataRole.UserRole, self.idx_attribute)

        # Third-Level Spells Modules
        spell_section = QTreeWidgetItem(self.nav_widget, ["Spell Book"])

        # -- Spell Sub Items
        overview_tab = QTreeWidgetItem(spell_section, ["Spell Selection"])
        # sub_item_a.setData(0, Qt.ItemDataRole.UserRole, self.idx_attribute)

        attribute_tab = QTreeWidgetItem(spell_section, ["Add Spell"])
        # sub_item_a.setData(0, Qt.ItemDataRole.UserRole, self.idx_attribute)

        # Fourth-Level Notes Modules
        note_section = QTreeWidgetItem(self.nav_widget, ["Game Notes"])

        # Navigation Tree Config
        self.nav_widget.setCurrentItem(character_section)

    ##-------------------------------------
    ## -------- FUNC CALLS ----------------
    ##-------------------------------------

    def set_nav_select(self, current: QTreeWidgetItem, previous: QTreeWidgetItem):
        if not current:
            return

        target_item = current.data(0, Qt.ItemDataRole.UserRole)

        if target_item is not None:
            self.view_stack.setCurrentItem(target_item)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, caption="Open Text File", dir="", filter="Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.editor.setPlainText(file.read())
                self.status_bar.showMessage(f"Loaded: {file_path}", 4000)
            except Exception as ERR:
                QMessageBox.critical(self, "Error", f"Failed to laod file: {ERR}")

    def change_theme(self, chngtheme: QAction):
        charapp_instance = QApplication.instance()
        if not charapp_instance:
            return

        if (chngtheme == self.action_darkmode):
            ThemeManager.apply_dark_theme(charapp_instance)
        elif (chngtheme == self.action_lightmode):
            ThemeManager.apply_light_theme(charapp_instance)


## ---------------------------------------------------------------------------------------------------------------- ##
##                                        Main Method                                                               ##
## ---------------------------------------------------------------------------------------------------------------- ##     
def main():
    charTTRPGapp = QApplication(sys.argv)
    charTTRPGapp.setStyle("Fusion")

    window = CharMainPane()
    window.show()
    sys.exit(charTTRPGapp.exec())

if __name__ == "__main__":
    main()
