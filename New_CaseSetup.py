import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton,
                              QFrame, QGridLayout)
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPainter, QColor

class StatusIndicator(QWidget):
    def __init__(self, color, size=8):
        super().__init__()
        self.color = color
        self.size = size
        self.setFixedSize(size, size)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(self.color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, self.size, self.size)

class InfoCard(QFrame):
    def __init__(self, title, icon_text="📋"):
        super().__init__()
        self.setFrameStyle(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
            InfoCard {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Header
        header = QHBoxLayout()
        icon_label = QLabel(icon_text)
        icon_label.setStyleSheet("font-size: 18px;")
        title_label = QLabel(title)
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        header.addWidget(icon_label)
        header.addWidget(title_label)
        header.addStretch()
        
        layout.addLayout(header)
        layout.addSpacing(15)
        
        self.content_layout = QVBoxLayout()
        layout.addLayout(self.content_layout)
        
        self.setLayout(layout)

class StatusCard(QFrame):
    def __init__(self, title, status_text, description, status_color, icon_text="✓"):
        super().__init__()
        self.setStyleSheet("""
            StatusCard {
                background-color: #f0fdf4;
                border: 1px solid #d1fae5;
                border-radius: 6px;
                padding: 12px;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Header with icon and title
        header = QHBoxLayout()
        icon_label = QLabel(icon_text)
        icon_label.setStyleSheet("font-size: 16px; color: #10b981;")
        title_label = QLabel(title)
        title_label.setStyleSheet("font-weight: 600; font-size: 13px;")
        header.addWidget(icon_label)
        header.addWidget(title_label)
        header.addStretch()
        
        layout.addLayout(header)
        
        # Description
        desc_label = QLabel(description)
        desc_label.setStyleSheet("font-size: 11px; color: #6b7280;")
        desc_label.setWordWrap(True)
        layout.addWidget(desc_label)
        
        # Status indicator
        status_layout = QHBoxLayout()
        indicator = StatusIndicator(status_color)
        status_label = QLabel(status_text)
        status_label.setStyleSheet("font-size: 11px; font-weight: 600; color: #059669;")
        status_layout.addWidget(indicator)
        status_layout.addWidget(status_label)
        status_layout.addStretch()
        
        layout.addLayout(status_layout)
        
        self.setLayout(layout)

class ActionButton(QFrame):
    def __init__(self, icon_text, label_text):
        super().__init__()
        self.setFrameStyle(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
            ActionButton {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 20px;
            }
            ActionButton:hover {
                background-color: #f9fafb;
                border-color: #d1d5db;
            }
        """)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        icon = QLabel(icon_text)
        icon.setStyleSheet("font-size: 24px; color: #6b7280;")
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        label = QLabel(label_text)
        label.setStyleSheet("font-size: 13px; color: #6b7280;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(icon)
        layout.addSpacing(8)
        layout.addWidget(label)
        
        self.setLayout(layout)

class ThermoMedAnalytics(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ThermoMed Analytics")
        self.setGeometry(100, 100, 1200, 750)
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create header
        self.create_header(main_layout)
        
        # Create content area
        content = QWidget()
        content.setStyleSheet("background-color: #f9fafb;")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(40, 30, 40, 30)
        
        # Back button
        back_btn = QPushButton("← Back to Dashboard")
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #3b82f6;
                font-size: 13px;
                text-align: left;
                padding: 5px;
            }
            QPushButton:hover {
                color: #2563eb;
            }
        """)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        content_layout.addWidget(back_btn)
        
        # Title and status
        title_layout = QHBoxLayout()
        title_label = QLabel("New Case Setup")
        title_label.setStyleSheet("font-size: 28px; font-weight: bold;")
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        
        status_badge = QLabel("● SYSTEM ONLINE")
        status_badge.setStyleSheet("""
            background-color: #d1fae5;
            color: #065f46;
            padding: 6px 12px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
        """)
        title_layout.addWidget(status_badge)
        content_layout.addLayout(title_layout)
        
        subtitle = QLabel("Initialize analysis parameters and verify local environment status.")
        subtitle.setStyleSheet("font-size: 13px; color: #6b7280; margin-bottom: 20px;")
        content_layout.addWidget(subtitle)
        
        # Main content grid
        grid = QHBoxLayout()
        grid.setSpacing(20)
        
        # Left column - Case Information
        case_info = InfoCard("Case Information", "📋")
        
        # Case Number
        case_num_label = QLabel("Case Number")
        case_num_label.setStyleSheet("font-size: 12px; font-weight: 600; color: #374151; margin-bottom: 5px;")
        case_info.content_layout.addWidget(case_num_label)
        
        case_num_input = QLineEdit()
        case_num_input.setPlaceholderText("e.g. 10245")
        case_num_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 13px;
            }
            QLineEdit:focus {
                border-color: #3b82f6;
            }
        """)
        case_info.content_layout.addWidget(case_num_input)
        
        help_text = QLabel("Enter the unique patient identifier for this session.")
        help_text.setStyleSheet("font-size: 11px; color: #9ca3af; margin-bottom: 15px;")
        case_info.content_layout.addWidget(help_text)
        
        # Target Organ
        target_label = QLabel("Target Organ")
        target_label.setStyleSheet("font-size: 12px; font-weight: 600; color: #374151; margin-bottom: 5px;")
        case_info.content_layout.addWidget(target_label)
        
        target_combo = QComboBox()
        target_combo.addItem("🔍 Select organ type...")
        target_combo.addItems(["Heart", "Liver", "Kidney", "Lung", "Brain"])
        target_combo.setStyleSheet("""
            QComboBox {
                padding: 10px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 13px;
            }
            QComboBox:focus {
                border-color: #3b82f6;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        case_info.content_layout.addWidget(target_combo)
        
        help_text2 = QLabel("Select the specific organ algorithm to apply.")
        help_text2.setStyleSheet("font-size: 11px; color: #9ca3af; margin-bottom: 15px;")
        case_info.content_layout.addWidget(help_text2)
        
        # Session Timestamp
        timestamp_label = QLabel("Session Timestamp")
        timestamp_label.setStyleSheet("font-size: 12px; font-weight: 600; color: #374151; margin-bottom: 5px;")
        case_info.content_layout.addWidget(timestamp_label)
        
        timestamp_display = QLabel(f"📅 {QDateTime.currentDateTime().toString('MMMM dd, yyyy — hh:mm AP')}")
        timestamp_display.setStyleSheet("""
            background-color: #f3f4f6;
            padding: 10px;
            border-radius: 6px;
            font-size: 13px;
            color: #4b5563;
        """)
        case_info.content_layout.addWidget(timestamp_display)
        
        case_info.content_layout.addStretch()
        grid.addWidget(case_info, stretch=1)
        
        # Right column - Environment Check
        env_card = QWidget()
        env_layout = QVBoxLayout(env_card)
        env_layout.setSpacing(15)
        
        env_info = InfoCard("Environment Check", "💻")
        
        # Python Environment status
        python_status = StatusCard(
            "Python Environment",
            "AVAILABLE",
            "Runtime v3.9.12 detected. All libraries loaded successfully.",
            "#10b981",
            "✓"
        )
        env_info.content_layout.addWidget(python_status)
        
        # Local Storage status
        storage_status = StatusCard(
            "Local Storage",
            "READY",
            "Write permission verified on /local/data/output.",
            "#10b981",
            "💾"
        )
        env_info.content_layout.addWidget(storage_status)
        
        env_info.content_layout.addStretch()
        env_layout.addWidget(env_info)
        
        # Initialize Analysis button
        init_button = QPushButton("Initialize Analysis →")
        init_button.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 14px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
            QPushButton:pressed {
                background-color: #1d4ed8;
            }
        """)
        init_button.setCursor(Qt.CursorShape.PointingHandCursor)
        init_button.clicked.connect(self.open_input_selection)
        env_layout.addWidget(init_button)
        
        secure_note = QLabel("🔒 Secure local processing initiated")
        secure_note.setStyleSheet("font-size: 11px; color: #9ca3af; text-align: center;")
        secure_note.setAlignment(Qt.AlignmentFlag.AlignCenter)
        env_layout.addWidget(secure_note)
        
        grid.addWidget(env_card, stretch=1)
        
        content_layout.addLayout(grid)
        
        # Bottom action buttons
        action_grid = QGridLayout()
        action_grid.setSpacing(15)
        
        action1 = ActionButton("🕐", "View Recent Cases")
        action2 = ActionButton("📁", "Browse File Archive")
        action3 = ActionButton("⚙", "Calibrate Sensors")
        action4 = ActionButton("❓", "Documentation")
        
        action_grid.addWidget(action1, 0, 0)
        action_grid.addWidget(action2, 0, 1)
        action_grid.addWidget(action3, 0, 2)
        action_grid.addWidget(action4, 0, 3)
        
        content_layout.addLayout(action_grid)
        content_layout.addStretch()
        
        main_layout.addWidget(content)
    
    def create_header(self, layout):
        header = QWidget()
        header.setStyleSheet("""
            background-color: white;
            border-bottom: 1px solid #e5e7eb;
        """)
        header.setFixedHeight(60)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 0, 20, 0)
        
        # Logo and title
        logo_label = QLabel("🏥")
        logo_label.setStyleSheet("font-size: 24px;")
        header_layout.addWidget(logo_label)
        
        title = QLabel("ThermoMed Analytics")
        title.setStyleSheet("font-size: 16px; font-weight: 600; color: #111827;")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        # Right side icons
        notif_btn = QPushButton("🔔")
        notif_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 18px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #f3f4f6;
                border-radius: 4px;
            }
        """)
        notif_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        header_layout.addWidget(notif_btn)
        
        settings_btn = QPushButton("⚙")
        settings_btn.setStyleSheet(notif_btn.styleSheet())
        settings_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        header_layout.addWidget(settings_btn)
        
        # User profile
        user_widget = QWidget()
        user_layout = QHBoxLayout(user_widget)
        user_layout.setContentsMargins(10, 0, 0, 0)
        user_layout.setSpacing(8)
        
        user_info = QWidget()
        user_info_layout = QVBoxLayout(user_info)
        user_info_layout.setContentsMargins(0, 0, 0, 0)
        user_info_layout.setSpacing(0)
        
        name_label = QLabel("Dr. A. Smith")
        name_label.setStyleSheet("font-size: 12px; font-weight: 600;")
        role_label = QLabel("Radiologist")
        role_label.setStyleSheet("font-size: 10px; color: #6b7280;")
        
        user_info_layout.addWidget(name_label)
        user_info_layout.addWidget(role_label)
        user_layout.addWidget(user_info)
        
        avatar = QLabel("👤")
        avatar.setStyleSheet("""
            font-size: 24px;
            background-color: #10b981;
            border-radius: 20px;
            padding: 5px;
        """)
        user_layout.addWidget(avatar)
        
        header_layout.addWidget(user_widget)
        
        layout.addWidget(header)
    
    def open_input_selection(self):
        """Open the Input Selection page"""
        self.input_selection_window = InputSelectionPage()
        self.input_selection_window.show()


class InputSelectionPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ThermoMed Analytics - Input Selection")
        self.setGeometry(100, 100, 1200, 750)
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create header
        self.create_header(main_layout)
        
        # Create content area
        content = QWidget()
        content.setStyleSheet("background-color: #f9fafb;")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(40, 30, 40, 30)
        
        # Back button
        back_btn = QPushButton("← Back to Case Setup")
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #3b82f6;
                font-size: 13px;
                text-align: left;
                padding: 5px;
            }
            QPushButton:hover {
                color: #2563eb;
            }
        """)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.clicked.connect(self.close)
        content_layout.addWidget(back_btn)
        
        # Title
        title_label = QLabel("Input Selection")
        title_label.setStyleSheet("font-size: 28px; font-weight: bold;")
        content_layout.addWidget(title_label)
        
        subtitle = QLabel("Select input source and configure data acquisition parameters.")
        subtitle.setStyleSheet("font-size: 13px; color: #6b7280; margin-bottom: 20px;")
        content_layout.addWidget(subtitle)
        
        # Input options grid
        options_grid = QGridLayout()
        options_grid.setSpacing(20)
        
        # File Upload Option
        file_option = self.create_input_option(
            "📁",
            "File Upload",
            "Import medical imaging files (DICOM, NIfTI, PNG, JPEG)",
            "#3b82f6"
        )
        options_grid.addWidget(file_option, 0, 0)
        
        # Camera Input Option
        camera_option = self.create_input_option(
            "📷",
            "Camera Input",
            "Use connected camera or imaging device for real-time capture",
            "#10b981"
        )
        options_grid.addWidget(camera_option, 0, 1)
        
        # Database Option
        database_option = self.create_input_option(
            "🗄️",
            "Database Query",
            "Retrieve existing case data from medical records database",
            "#8b5cf6"
        )
        options_grid.addWidget(database_option, 1, 0)
        
        # Device Stream Option
        device_option = self.create_input_option(
            "📡",
            "Device Stream",
            "Connect to thermal imaging device via network stream",
            "#f59e0b"
        )
        options_grid.addWidget(device_option, 1, 1)
        
        content_layout.addLayout(options_grid)
        content_layout.addStretch()
        
        main_layout.addWidget(content)
    
    def create_input_option(self, icon, title, description, color):
        """Create an input selection option card"""
        card = QFrame()
        card.setFrameStyle(QFrame.Shape.StyledPanel)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: white;
                border: 2px solid #e5e7eb;
                border-radius: 12px;
                padding: 30px;
            }}
            QFrame:hover {{
                border-color: {color};
                background-color: #fafafa;
            }}
        """)
        card.setCursor(Qt.CursorShape.PointingHandCursor)
        
        layout = QVBoxLayout(card)
        layout.setSpacing(15)
        
        # Icon
        icon_label = QLabel(icon)
        icon_label.setStyleSheet(f"font-size: 48px;")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(icon_label)
        
        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            font-size: 18px;
            font-weight: bold;
            color: #111827;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Description
        desc_label = QLabel(description)
        desc_label.setStyleSheet("font-size: 13px; color: #6b7280;")
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc_label.setWordWrap(True)
        layout.addWidget(desc_label)
        
        # Select button
        select_btn = QPushButton("Select")
        select_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 24px;
                font-size: 13px;
                font-weight: 600;
                margin-top: 10px;
            }}
            QPushButton:hover {{
                opacity: 0.9;
            }}
        """)
        select_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(select_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        return card
    
    def create_header(self, layout):
        header = QWidget()
        header.setStyleSheet("""
            background-color: white;
            border-bottom: 1px solid #e5e7eb;
        """)
        header.setFixedHeight(60)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 0, 20, 0)
        
        # Logo and title
        logo_label = QLabel("🏥")
        logo_label.setStyleSheet("font-size: 24px;")
        header_layout.addWidget(logo_label)
        
        title = QLabel("ThermoMed Analytics")
        title.setStyleSheet("font-size: 16px; font-weight: 600; color: #111827;")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        # Right side icons
        notif_btn = QPushButton("🔔")
        notif_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 18px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #f3f4f6;
                border-radius: 4px;
            }
        """)
        notif_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        header_layout.addWidget(notif_btn)
        
        settings_btn = QPushButton("⚙")
        settings_btn.setStyleSheet(notif_btn.styleSheet())
        settings_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        header_layout.addWidget(settings_btn)
        
        # User profile
        user_widget = QWidget()
        user_layout = QHBoxLayout(user_widget)
        user_layout.setContentsMargins(10, 0, 0, 0)
        user_layout.setSpacing(8)
        
        user_info = QWidget()
        user_info_layout = QVBoxLayout(user_info)
        user_info_layout.setContentsMargins(0, 0, 0, 0)
        user_info_layout.setSpacing(0)
        
        name_label = QLabel("Dr. A. Smith")
        name_label.setStyleSheet("font-size: 12px; font-weight: 600;")
        role_label = QLabel("Radiologist")
        role_label.setStyleSheet("font-size: 10px; color: #6b7280;")
        
        user_info_layout.addWidget(name_label)
        user_info_layout.addWidget(role_label)
        user_layout.addWidget(user_info)
        
        avatar = QLabel("👤")
        avatar.setStyleSheet("""
            font-size: 24px;
            background-color: #10b981;
            border-radius: 20px;
            padding: 5px;
        """)
        user_layout.addWidget(avatar)
        
        header_layout.addWidget(user_widget)
        
        layout.addWidget(header)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    window = ThermoMedAnalytics()
    window.show()
    
    sys.exit(app.exec())