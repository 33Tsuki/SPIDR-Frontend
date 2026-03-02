import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QLabel, QLineEdit, QPushButton,
                              QFrame, QTabWidget, QProgressBar, QCheckBox,
                              QTextEdit)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QFont, QColor, QPalette
from styles import ModernDarkTheme
from Results_Visualization import MediThermApp

class StageTab(QWidget):
    def __init__(self, stage_num, stage_name, active=False):
        super().__init__()
        layout = QHBoxLayout()
        layout.setContentsMargins(12, 8, 12, 8)
        
        # Stage indicator
        indicator = QLabel(f"⊙ Stage {stage_num}")
        if active:
            indicator.setStyleSheet(f"color: {ModernDarkTheme.PRIMARY}; font-weight: 600; font-size: 12px;")
        else:
            indicator.setStyleSheet(f"color: {ModernDarkTheme.TEXT_SECONDARY}; font-size: 12px;")
        
        layout.addWidget(indicator)
        self.setLayout(layout)

class ConfigCard(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"""
            ConfigCard {{
                {ModernDarkTheme.card_style()}
                padding: 20px;
            }}
        """)
        
        layout = QVBoxLayout()
        
        # Header
        header = QHBoxLayout()
        icon = QLabel("⚙")
        icon.setStyleSheet("font-size: 18px; color: #3b82f6;")
        title = QLabel("Configuration Parameters")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        subtitle = QLabel("Set parameters for thermal analysis pipeline.")
        subtitle.setStyleSheet("color: #9ca3af; font-size: 11px;")
        
        header_text = QVBoxLayout()
        header_text.setSpacing(2)
        header_text.addWidget(title)
        header_text.addWidget(subtitle)
        
        header.addWidget(icon)
        header.addLayout(header_text)
        header.addStretch()
        
        # Advanced Mode toggle
        self.advanced_toggle = QCheckBox("Advanced Mode")
        self.advanced_toggle.setStyleSheet("""
            QCheckBox {
                font-size: 12px;
                color: #6b7280;
            }
            QCheckBox::indicator {
                width: 40px;
                height: 20px;
                border-radius: 10px;
                background-color: #e5e7eb;
            }
            QCheckBox::indicator:checked {
                background-color: #3b82f6;
            }
        """)
        header.addWidget(self.advanced_toggle)
        
        layout.addLayout(header)
        layout.addSpacing(20)
        
        # Case Number
        case_label = QLabel("Case Number")
        case_label.setStyleSheet("font-size: 12px; font-weight: 600; color: #374151;")
        layout.addWidget(case_label)
        
        case_input_layout = QHBoxLayout()
        case_icon = QLabel("#")
        case_icon.setStyleSheet("color: #9ca3af; font-size: 14px;")
        self.case_input = QLineEdit("CN-2023-4492")
        self.case_input.setStyleSheet("""
            QLineEdit {
                padding: 10px 10px 10px 5px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 12px;
                background-color: #f9fafb;
            }
        """)
        case_input_layout.addWidget(case_icon)
        case_input_layout.addWidget(self.case_input)
        
        copy_btn = QPushButton("📋")
        copy_btn.setFixedSize(36, 36)
        copy_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #f9fafb;
            }
        """)
        copy_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        case_input_layout.addWidget(copy_btn)
        
        layout.addLayout(case_input_layout)
        layout.addSpacing(15)
        
        # Configuration File
        config_label = QLabel("Configuration File")
        config_label.setStyleSheet("font-size: 12px; font-weight: 600; color: #374151;")
        layout.addWidget(config_label)
        
        config_layout = QHBoxLayout()
        config_icon = QLabel("📄")
        config_icon.setStyleSheet("font-size: 14px;")
        self.config_input = QLineEdit("config_staging_v4.json")
        self.config_input.setStyleSheet("""
            QLineEdit {
                padding: 10px 10px 10px 5px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 12px;
                background-color: #f9fafb;
            }
        """)
        config_layout.addWidget(config_icon)
        config_layout.addWidget(self.config_input)
        
        lock_btn = QPushButton("🔒")
        lock_btn.setFixedSize(36, 36)
        lock_btn.setStyleSheet(copy_btn.styleSheet())
        lock_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        config_layout.addWidget(lock_btn)
        
        layout.addLayout(config_layout)
        layout.addSpacing(15)
        
        # File Location Path
        path_label = QLabel("File Location Path")
        path_label.setStyleSheet("font-size: 12px; font-weight: 600; color: #374151;")
        layout.addWidget(path_label)
        
        path_layout = QHBoxLayout()
        path_icon = QLabel("📁")
        path_icon.setStyleSheet("font-size: 14px;")
        self.path_input = QLineEdit("C:/LocalData/MedScan/ThermalCases/2023/4492/input/")
        self.path_input.setStyleSheet("""
            QLineEdit {
                padding: 10px 10px 10px 5px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 12px;
                background-color: #f9fafb;
            }
        """)
        path_layout.addWidget(path_icon)
        path_layout.addWidget(self.path_input)
        
        browse_btn = QPushButton("📂")
        browse_btn.setFixedSize(36, 36)
        browse_btn.setStyleSheet(copy_btn.styleSheet())
        browse_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        path_layout.addWidget(browse_btn)
        
        layout.addLayout(path_layout)
        
        path_note = QLabel("ℹ Path is relative to the securely assigned volume.")
        path_note.setStyleSheet("font-size: 11px; color: #6b7280; margin-top: 5px;")
        layout.addWidget(path_note)
        
        layout.addSpacing(20)
        
        # Ready to execute
        ready_layout = QHBoxLayout()
        ready_label = QLabel("Ready to execute.")
        ready_label.setStyleSheet("font-size: 12px; color: #6b7280;")
        ready_layout.addWidget(ready_label)
        
        time_label = QLabel("Estimated time: ~4 sec")
        time_label.setStyleSheet("font-size: 12px; color: #9ca3af;")
        ready_layout.addStretch()
        ready_layout.addWidget(time_label)
        
        layout.addLayout(ready_layout)
        
        layout.addSpacing(10)
        
        # Run button
        self.run_btn = QPushButton("⊙ Run Stage 2 - Data Processing")
        self.run_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {ModernDarkTheme.PRIMARY};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 14px;
                font-size: 14px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: #2563eb;
            }}
        """)
        self.run_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(self.run_btn)
        
        layout.addSpacing(20)
        
        # Tabs for Previous Run and Disk Usage
        tabs = QTabWidget()
        tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #e5e7eb;
                border-radius: 6px;
                background-color: white;
            }
            QTabBar::tab {
                padding: 8px 16px;
                font-size: 12px;
                font-weight: 600;
                color: #6b7280;
                border: none;
            }
            QTabBar::tab:selected {
                color: #3b82f6;
                border-bottom: 2px solid #3b82f6;
            }
        """)
        
        # Previous Run tab
        prev_run = QWidget()
        prev_layout = QVBoxLayout(prev_run)
        prev_layout.setContentsMargins(15, 15, 15, 15)
        
        prev_label = QLabel("Today, 08:42 AM (Success)")
        prev_label.setStyleSheet("font-size: 12px; color: #6b7280;")
        prev_layout.addWidget(prev_label)
        
        tabs.addTab(prev_run, "Previous Run")
        
        # Disk Usage tab
        disk_usage = QWidget()
        disk_layout = QVBoxLayout(disk_usage)
        disk_layout.setContentsMargins(15, 15, 15, 15)
        
        disk_bar = QProgressBar()
        disk_bar.setValue(34)
        disk_bar.setTextVisible(False)
        disk_bar.setFixedHeight(8)
        disk_bar.setStyleSheet("""
            QProgressBar {
                border: none;
                border-radius: 4px;
                background-color: #e5e7eb;
            }
            QProgressBar::chunk {
                border-radius: 4px;
                background-color: #3b82f6;
            }
        """)
        disk_layout.addWidget(disk_bar)
        
        disk_label = QLabel("34% Used")
        disk_label.setStyleSheet("font-size: 12px; color: #6b7280; margin-top: 5px;")
        disk_layout.addWidget(disk_label)
        
        tabs.addTab(disk_usage, "Disk Usage")
        
        layout.addWidget(tabs)
        layout.addStretch()
        
        self.setLayout(layout)

class TerminalWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            TerminalWidget {
                background-color: #1e293b;
                border: 1px solid #334155;
                border-radius: 8px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header
        header = QWidget()
        header.setStyleSheet("background-color: #0f172a; border-radius: 8px 8px 0 0; padding: 10px;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(15, 8, 15, 8)
        
        title = QLabel("Stage 2 Execution")
        title.setStyleSheet("color: #cbd5e1; font-size: 13px; font-weight: 600;")
        header_layout.addWidget(title)
        
        subtitle = QLabel("Real-time terminal output")
        subtitle.setStyleSheet("color: #64748b; font-size: 11px;")
        header_layout.addWidget(subtitle)
        header_layout.addStretch()
        
        idle_badge = QLabel("IDLE")
        idle_badge.setStyleSheet("""
            background-color: #334155;
            color: #94a3b8;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 600;
        """)
        header_layout.addWidget(idle_badge)
        
        layout.addWidget(header)
        
        # Terminal content
        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)
        self.terminal.setStyleSheet("""
            QTextEdit {
                background-color: #1e293b;
                color: #e2e8f0;
                border: none;
                font-family: 'Courier New', monospace;
                font-size: 11px;
                padding: 15px;
            }
        """)
        
        # Add sample terminal output
        self.terminal.setHtml("""
            <div style='color: #cbd5e1;'>
                <span style='color: #10b981;'>user@medthermo:~$</span> python3 hot_processing_pipeline.py<br>
                <span style='color: #64748b;'>→ Checks</span><br>
                <span style='color: #10b981;'>  ✓ Initializing environment...</span><br>
                <span style='color: #10b981;'>  ✓ Checking dependencies... [OK]</span><br>
                <span style='color: #10b981;'>  ✓ GPU Acceleration: [DETECTED]</span><br>
                <span style='color: #e2e8f0;'>  ✓ Ready for input</span><br>
                <br>
                <span style='color: #10b981;'>user@medthermo:~$</span> <span style='color: #94a3b8;'>█</span>
            </div>
        """)
        
        layout.addWidget(self.terminal)
        
        # Footer
        footer = QWidget()
        footer.setStyleSheet("background-color: #0f172a; border-radius: 0 0 8px 8px;")
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(15, 8, 15, 8)
        
        runtime = QLabel("Runtime: 00h : 00m : 2s")
        runtime.setStyleSheet("color: #64748b; font-size: 11px;")
        footer_layout.addWidget(runtime)
        
        footer_layout.addStretch()
        
        details_btn = QPushButton("⚡ Show Full Details")
        details_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: 1px solid #334155;
                color: #94a3b8;
                border-radius: 4px;
                padding: 5px 12px;
                font-size: 11px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #334155;
                color: #cbd5e1;
            }
        """)
        details_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        footer_layout.addWidget(details_btn)
        
        layout.addWidget(footer)
        
        self.setLayout(layout)

class ExecutionPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"""
            ExecutionPanel {{
                {ModernDarkTheme.card_style()}
                padding: 20px;
                background-color: transparent;
                border: none;
            }}
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Last stage info
        last_stage = QLabel("Last stage: Tue Oct 23 03:38:31 on tty2023")
        last_stage.setStyleSheet("font-size: 11px; color: #6b7280; margin-bottom: 5px;")
        layout.addWidget(last_stage)
        
        # Terminal
        self.terminal = TerminalWidget()
        layout.addWidget(self.terminal)
        
        self.setLayout(layout)

class MedThermoStage2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MedThermo Analytics - Stage 2")
        self.setGeometry(100, 100, 1100, 650)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Apply global stylesheet
        self.setStyleSheet(ModernDarkTheme.get_stylesheet())
        
        # Header
        self.create_header(main_layout)
        
        # Content
        content = QWidget()
        content.setStyleSheet(f"background-color: {ModernDarkTheme.BACKGROUND};")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(40, 30, 40, 30)
        
        # Pipeline label
        pipeline = QLabel("📊 PROCESSING PIPELINE")
        pipeline.setStyleSheet("font-size: 11px; color: #3b82f6; font-weight: 600; letter-spacing: 0.5px;")
        content_layout.addWidget(pipeline)
        
        # Title and stage tabs
        title_row = QHBoxLayout()
        title = QLabel("Stage 2: Thermal Data Processing")
        title.setStyleSheet("font-size: 26px; font-weight: bold;")
        title_row.addWidget(title)
        title_row.addStretch()
        
        # Stage indicators
        stage1 = QPushButton("⊙ Stage 1")
        stage1.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 6px;
                padding: 8px 14px;
                font-size: 12px;
                color: #6b7280;
            }
            QPushButton:hover {
                background-color: #f9fafb;
            }
        """)
        stage1.setCursor(Qt.CursorShape.PointingHandCursor)
        title_row.addWidget(stage1)
        
        stage2 = QPushButton("⊙ Stage 2")
        stage2.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6;
                border: 1px solid #3b82f6;
                border-radius: 6px;
                padding: 8px 14px;
                font-size: 12px;
                font-weight: 600;
                color: white;
            }
        """)
        title_row.addWidget(stage2)
        
        stage3 = QPushButton("⊙ Stage 3")
        stage3.setStyleSheet(stage1.styleSheet())
        stage3.setCursor(Qt.CursorShape.PointingHandCursor)
        title_row.addWidget(stage3)
        
        content_layout.addLayout(title_row)
        
        # Subtitle
        subtitle = QLabel("Review configuration parameters for the current session and execute the thermal analysis algorithm.")
        subtitle.setStyleSheet("font-size: 13px; color: #6b7280; margin-top: 5px; margin-bottom: 20px;")
        content_layout.addWidget(subtitle)
        
        # Main panels
        panels = QHBoxLayout()
        panels.setSpacing(20)
        
        config = ConfigCard()
        execution = ExecutionPanel()
        
        panels.addWidget(config, stretch=1)
        panels.addWidget(execution, stretch=1)
        
        # Connect Run Button
        config.run_btn.clicked.connect(self.run_stage_2)
        
        content_layout.addLayout(panels)
        content_layout.addStretch()
        
        main_layout.addWidget(content)
        
    def run_stage_2(self):
        # Open Results Visualization
        self.results_window = MediThermApp()
        self.results_window.show()
        self.close()
    
    def create_header(self, layout):
        header = QWidget()
        header.setStyleSheet("""
            background-color: white;
            border-bottom: 1px solid #e5e7eb;
        """)
        header.setFixedHeight(55)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 0, 20, 0)
        
        # Logo
        logo = QLabel("🏥")
        logo.setStyleSheet("font-size: 20px;")
        header_layout.addWidget(logo)
        
        title = QLabel("MedThermo Analytics")
        title.setStyleSheet("font-size: 15px; font-weight: 600; color: #111827;")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        # System status
        status_dot = QLabel("●")
        status_dot.setStyleSheet("color: #10b981; font-size: 10px;")
        header_layout.addWidget(status_dot)
        
        status = QLabel("SYSTEM STATUS: LOCAL / OFFLINE")
        status.setStyleSheet("font-size: 11px; color: #6b7280; font-weight: 600;")
        header_layout.addWidget(status)
        
        header_layout.addSpacing(20)
        
        # User icon
        user = QPushButton("👤")
        user.setStyleSheet("""
            QPushButton {
                background-color: #f3f4f6;
                border: none;
                border-radius: 18px;
                font-size: 18px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #e5e7eb;
            }
        """)
        user.setFixedSize(36, 36)
        user.setCursor(Qt.CursorShape.PointingHandCursor)
        header_layout.addWidget(user)
        
        layout.addWidget(header)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModernDarkTheme.setup_theme(app)
    
    window = MedThermoStage2()
    window.show()
    
    sys.exit(app.exec())