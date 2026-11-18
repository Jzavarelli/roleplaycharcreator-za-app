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
import sys

class Character:

    def __init__(self, name, age, race, level, char_class):
        self.character_name = name
        self.character_age = age
        self.character_race = race
        self.base_level = level
        self.base_class = char_class