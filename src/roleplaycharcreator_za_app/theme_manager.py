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
import sys

from enum               import ( StrEnum ) 
from PySide6.QtCore     import ( Qt )
from PySide6.QtGui      import ( QColor, QPalette )
from PySide6.QtWidgets  import ( QApplication )

# String Enumeration of Themes
class ThemeMode(StrEnum):
    LIGHT   = "Light"
    DARK    = "Dark"

# Theme Management Tool
class ThemeManager:
    @staticmethod
    def apply_dark_theme(charapp: QApplication):
        charapp.setStyle("Fusion")
        dark_palette = QPalette()

        # Base background colors
        dark_palette.setColor(QPalette.ColorRole.Window, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(35, 35, 35))

        # Tooltips
        dark_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(220, 220, 220))
        dark_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(35, 35, 35))

        # Text and Inputs
        dark_palette.setColor(QPalette.ColorRole.Text, QColor(220, 220, 220))
        dark_palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(120, 120, 120))

        # Buttons and Controls
        dark_palette.setColor(QPalette.ColorRole.Button, QColor(45, 45, 45))
        dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
        dark_palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)

        # Selection / Highlights (Accent blue)
        dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))

        # Disabled States (Grays out unavailable buttons/inputs)
        dark_palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.WindowText,
            QColor(120, 120, 120),
        )
        dark_palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.Text,
            QColor(120, 120, 120),
        )
        dark_palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.ButtonText,
            QColor(120, 120, 120),
        )

        charapp.setPalette(dark_palette)

    @staticmethod
    def apply_light_theme(charapp: QApplication):
        charapp.setStyle("Fusion")
        light_palette = QPalette()

        # Canvas & Window: Muted soft warm gray/slate (reduces eye strain)
        window_bg = QColor("#ECEEF2")
        light_palette.setColor(QPalette.ColorRole.Window, window_bg)

        # Base: Input boxes, text fields, and tables (crisp off-white to lift from window)
        input_bg = QColor("#FAFBFC")
        light_palette.setColor(QPalette.ColorRole.Base, input_bg)
        light_palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#E2E5EA"))

        # Text: Deep slate/charcoal instead of stark pitch black (#000000)
        main_text = QColor("#2D3748")
        light_palette.setColor(QPalette.ColorRole.WindowText, main_text)
        light_palette.setColor(QPalette.ColorRole.Text, main_text)

        # Muted placeholder hints
        light_palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("#8D96A5"))

        # Buttons & Controls: Subtle contrast against the window background
        button_bg = QColor("#DEE2E8")
        light_palette.setColor(QPalette.ColorRole.Button, button_bg)
        light_palette.setColor(QPalette.ColorRole.ButtonText, main_text)

        # Accents: Softer corporate/slate blue for selections
        accent_blue = QColor("#3B82F6")
        light_palette.setColor(QPalette.ColorRole.Highlight, accent_blue)
        light_palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#FFFFFF"))

        # Subtle borders and dividers
        light_palette.setColor(QPalette.ColorRole.Midlight, QColor("#D8DCE3"))
        light_palette.setColor(QPalette.ColorRole.Mid, QColor("#C4C9D3"))
        light_palette.setColor(QPalette.ColorRole.Dark, QColor("#9AA0AC"))

        # Tooltips: Dark card with light text for readable popups
        light_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#1E293B"))
        light_palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#F8FAFC"))

        # Disabled States: Gently muted text and controls
        disabled_text = QColor("#A0AEC0")
        light_palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.WindowText,
            disabled_text,
        )
        light_palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.Text,
            disabled_text,
        )
        light_palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.ButtonText,
            disabled_text,
        )

        charapp.setPalette(light_palette)