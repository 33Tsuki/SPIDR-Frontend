from PyQt6.QtGui import QColor, QPalette, QFont

class ModernDarkTheme:
    # Color Palette
    PRIMARY = "#3b82f6"       # Blue-500
    SECONDARY = "#64748b"     # Slate-500
    ACCENT = "#8b5cf6"        # Violet-500
    SUCCESS = "#10b981"       # Emerald-500
    WARNING = "#f59e0b"       # Amber-500
    ERROR = "#ef4444"         # Red-500
    
    BACKGROUND = "#f8fafc"    # Slate-50
    SURFACE = "#ffffff"       # White
    TEXT_PRIMARY = "#1e293b"  # Slate-800
    TEXT_SECONDARY = "#64748b" # Slate-500
    BORDER = "#e2e8f0"        # Slate-200
    
    # Fonts
    FONT_FAMILY = "Segoe UI" # Fallback to system sans-serif usually works, but Segoe UI is good for Windows/standard
    
    @staticmethod
    def setup_theme(app):
        """Applies a global fusion style with custom palette adjustments if needed"""
        app.setStyle("Fusion")
        
        # We can add global palette tweaks here if we want a dark mode in the future
        # For now, we focusing on the light/clean theme described in the prompt
        pass

    @staticmethod
    def get_stylesheet():
        return f"""
            QMainWindow, QWidget {{
                background-color: {ModernDarkTheme.BACKGROUND};
                color: {ModernDarkTheme.TEXT_PRIMARY};
                font-family: '{ModernDarkTheme.FONT_FAMILY}', sans-serif;
            }}
            
            /* Buttons */
            QPushButton {{
                background-color: {ModernDarkTheme.PRIMARY};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 600;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: #2563eb; /* Blue-600 */
            }}
            QPushButton:pressed {{
                background-color: #1d4ed8; /* Blue-700 */
            }}
            QPushButton:disabled {{
                background-color: {ModernDarkTheme.SECONDARY};
                opacity: 0.7;
            }}
            
            /* Cards / Frames */
            QFrame {{
                border-radius: 8px;
            }}
            
            /* Inputs */
            QLineEdit, QComboBox, QTextEdit {{
                background-color: {ModernDarkTheme.SURFACE};
                border: 1px solid {ModernDarkTheme.BORDER};
                border-radius: 6px;
                padding: 8px;
                color: {ModernDarkTheme.TEXT_PRIMARY};
                selection-background-color: {ModernDarkTheme.PRIMARY};
            }}
            QLineEdit:focus, QComboBox:focus, QTextEdit:focus {{
                border: 2px solid {ModernDarkTheme.PRIMARY};
            }}
            
            /* Scroll Area */
            QScrollArea {{
                border: none;
                background-color: transparent;
            }}
            QScrollBar:vertical {{
                border: none;
                background: {ModernDarkTheme.BACKGROUND};
                width: 10px;
                margin: 0px 0px 0px 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {ModernDarkTheme.SECONDARY};
                min-height: 20px;
                border-radius: 5px;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
        """

    @staticmethod
    def card_style():
        return f"""
            background-color: {ModernDarkTheme.SURFACE};
            border: 1px solid {ModernDarkTheme.BORDER};
            border-radius: 12px;
        """
        
    @staticmethod
    def status_card_success_style():
        return """
            background-color: #f0fdf4; /* Emerald-50 */
            border: 1px solid #bbf7d0; /* Emerald-200 */
            border-radius: 8px;
        """
        
    @staticmethod
    def status_card_warning_style():
        return """
            background-color: #fffbeb; /* Amber-50 */
            border: 1px solid #fde68a; /* Amber-200 */
            border-radius: 8px;
        """

    @staticmethod
    def action_button_style():
        return f"""
            QFrame {{
                background-color: {ModernDarkTheme.SURFACE};
                border: 1px solid {ModernDarkTheme.BORDER};
                border-radius: 8px;
            }}
            QFrame:hover {{
                border: 1px solid {ModernDarkTheme.PRIMARY};
                background-color: #eff6ff; /* Blue-50 */
            }}
        """
