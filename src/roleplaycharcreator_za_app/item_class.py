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

#Import and Library Management

class Item():

    def __init__(self, name: str, description: str, ingredients: list, char_clas: str):
        self.item_name = name
        self.item_description = description

        try:
            if (ingredients == NULL or ingredients.count == 0):
                self.item_ingredients = ["Not Applicable"]
            else:
                self.item_ingredients = ingredients

            if (char_class == NULL or char_class == ""): 
                self.item_class = "Not Applicable"
            else:
                self.item_class = char_class
        except Exception as ERR:
                QMessageBox.critical(self, "Error", f"Failed to laod file: {ERR}")