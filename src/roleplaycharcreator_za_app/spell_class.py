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

class Spells():

    def __init__(self, name: str, components: list, level: int, char_class: str):
        self.spell_name = name
        self.spell_components = components
        self.spell_level = level
        self.spell_class = char_class