import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QLabel, QLineEdit, QPushButton,
                              QFrame, QFileDialog, QScrollArea, QGridLayout,
                              QSizePolicy)
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QPixmap, QFont, QPainter, QColor, QPen

class StatusBadge(QLabel):
    def __init__(self, text, color="#3b82f6"):
        super().__init__(text)
        self.setStyleSheet(f"""
            background-color: {color};
            color: white;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
        """)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

class StepIndicator(QWidget):
    def __init__(self, number, title, subtitle, status="pending"):
        super().__init__()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # Circle with number or checkmark
        self.circle = QLabel()
        self.circle.setFixedSize(36, 36)
        self.status = status
        self.number = number
        
        if status == "completed":
            self.circle.setText("✓")
            self.circle.setStyleSheet("""
                background-color: #10b981;
                color: white;
                border-radius: 18px;
                font-size: 18px;
                font-weight: bold;
            """)
        elif status == "running":
            self.circle.setText(str(number))
            self.circle.setStyleSheet("""
                background-color: #3b82f6;
                color: white;
                border-radius: 18px;
                font-size: 14px;
                font-weight: bold;
            """)
        else:
            self.circle.setText(str(number))
            self.circle.setStyleSheet("""
                background-color: #e5e7eb;
                color: #9ca3af;
                border-radius: 18px;
                font-size: 14px;
                font-weight: bold;
            """)
        
        self.circle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.circle)
        
        # Text
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        
        title_label = QLabel(title)
        if status == "running":
            title_label.setStyleSheet("font-weight: 600; font-size: 13px; color: #111827;")
        else:
            title_label.setStyleSheet("font-weight: 600; font-size: 13px; color: #6b7280;")
        
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet("font-size: 11px; color: #9ca3af;")
        
        text_layout.addWidget(title_label)
        text_layout.addWidget(subtitle_label)
        
        layout.addLayout(text_layout)
        layout.addStretch()
        
        self.setLayout(layout)

class ConfigPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
            ConfigPanel {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Header
        header = QHBoxLayout()
        icon = QLabel("⚙")
        icon.setStyleSheet("font-size: 18px;")
        title = QLabel("Input Configuration Panel")
        title.setStyleSheet("Color: black; font-weight: bold; font-size: 14px;")
        header.addWidget(icon)
        header.addWidget(title)
        header.addStretch()
        
        ready_badge = StatusBadge("READY", "#e0e7ff")
        ready_badge.setStyleSheet("""
            background-color: #e0e7ff;
            color: #3730a3;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
        """)
        header.addWidget(ready_badge)
        
        layout.addLayout(header)
        layout.addSpacing(20)
        
        # SEG File Address
        seg_label = QLabel("SEG File Address")
        seg_label.setStyleSheet("font-size: 12px; font-weight: 600; color: #374151; margin-bottom: 5px;")
        layout.addWidget(seg_label)
        
        file_layout = QHBoxLayout()
        self.seg_input = QLineEdit()
        self.seg_input.setPlaceholderText("C:/MedicalData/ThermalCases/2023/case_492_thermal.seg")
        self.seg_input.setText("C:/MedicalData/ThermalCases/2023/case_492_thermal.seg")
        self.seg_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 12px;
                background-color: #f9fafb;
            }
        """)
        file_layout.addWidget(self.seg_input)
        
        browse_btn = QPushButton("📁 Browse")
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 12px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #f9fafb;
            }
        """)
        browse_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        browse_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(browse_btn)
        
        layout.addLayout(file_layout)
        
        # File validated message
        validated = QLabel("✓ File validated successfully (143.8 MB)")
        validated.setStyleSheet("font-size: 11px; color: #10b981; margin-top: 5px;")
        layout.addWidget(validated)
        
        layout.addSpacing(15)
        
        # Visual Reference Image
        ref_label = QLabel("Visual Reference Image")
        ref_label.setStyleSheet("font-size: 12px; font-weight: 600; color: #374151; margin-bottom: 5px;")
        layout.addWidget(ref_label)
        
        img_layout = QHBoxLayout()
        self.img_input = QLineEdit()
        self.img_input.setPlaceholderText("C:/MedicalData/Visual/Cases/2023/case_492_vis.png")
        self.img_input.setText("C:/MedicalData/Visual/Cases/2023/case_492_vis.png")
        self.img_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 12px;
                background-color: #f9fafb;
            }
        """)
        img_layout.addWidget(self.img_input)
        layout.addLayout(img_layout)
        
        layout.addSpacing(10)
        
        # Image preview
        preview_container = QWidget()
        preview_layout = QVBoxLayout(preview_container)
        preview_layout.setContentsMargins(0, 0, 0, 0)
        
        self.image_preview = QLabel()
        self.image_preview.setFixedSize(150, 150)
        self.image_preview.setStyleSheet("""
            background-color: #f3f4f6;
            border: 2px dashed #d1d5db;
            border-radius: 8px;
        """)
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Set a placeholder medical image
        self.image_preview.setPixmap(self.create_placeholder_image())
        self.image_preview.setScaledContents(True)
        
        select_img_btn = QPushButton("🖼 Select Image")
        select_img_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #3b82f6;
                font-size: 11px;
                padding: 5px;
            }
            QPushButton:hover {
                color: #2563eb;
                text-decoration: underline;
            }
        """)
        select_img_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        select_img_btn.clicked.connect(self.select_image)
        
        preview_layout.addWidget(self.image_preview)
        preview_layout.addWidget(select_img_btn)
        
        layout.addWidget(preview_container)
        
        # Format note
        format_note = QLabel("✓ Image format valid (PNG)")
        format_note.setStyleSheet("font-size: 11px; color: #10b981; margin-top: 5px;")
        layout.addWidget(format_note)
        
        layout.addSpacing(20)
        
        # Run button
        run_btn = QPushButton("Run Stage 1 – Segmentation ▶")
        run_btn.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6;
                border: none;
                border-radius: 6px;
                padding: 14px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
        """)
        run_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(run_btn)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def create_placeholder_image(self):
        pixmap = QPixmap(150, 150)
        pixmap.fill(QColor("#f0f9ff"))
        
        painter = QPainter(pixmap)
        painter.setPen(QPen(QColor("#3b82f6"), 2))
        
        # Draw a simple medical imaging placeholder
        painter.drawEllipse(40, 40, 70, 70)
        painter.drawEllipse(50, 50, 50, 50)
        painter.drawLine(75, 40, 75, 110)
        painter.drawLine(40, 75, 110, 75)
        
        painter.end()
        return pixmap
    
    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select SEG File", "", "SEG Files (*.seg);;All Files (*)"
        )
        if file_name:
            self.seg_input.setText(file_name)
    
    def select_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg);;All Files (*)"
        )
        if file_name:
            self.img_input.setText(file_name)
            pixmap = QPixmap(file_name)
            if not pixmap.isNull():
                self.image_preview.setPixmap(pixmap.scaled(
                    150, 150, Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                ))

class ExecutionPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
            ExecutionPanel {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Header
        header = QHBoxLayout()
        icon = QLabel("▶")
        icon.setStyleSheet("font-size: 18px; color: #3b82f6;")
        title = QLabel("Stage 1 Execution")
        title.setStyleSheet("color: black; font-weight: bold; font-size: 14px;")
        header.addWidget(icon)
        header.addWidget(title)
        header.addStretch()
        
        running_badge = StatusBadge("⚡ Running", "#3b82f6")
        header.addWidget(running_badge)
        
        layout.addLayout(header)
        layout.addSpacing(20)
        
        # Execution script
        script_box = QWidget()
        script_box.setStyleSheet("""
            background-color: #f9fafb;
            border: 1px solid #e5e7eb;
            border-radius: 6px;
            padding: 12px;
        """)
        script_layout = QHBoxLayout(script_box)
        script_layout.setContentsMargins(10, 10, 10, 10)
        
        script_icon = QLabel("📄")
        script_icon.setStyleSheet("font-size: 16px;")
        script_label = QLabel("EXECUTING SCRIPT")
        script_label.setStyleSheet("font-size: 10px; color: #6b7280; font-weight: 600;")
        script_name = QLabel("stage_division_auto.py")
        script_name.setStyleSheet("font-size: 12px; font-weight: 600; color: #111827;")
        
        script_text_layout = QVBoxLayout()
        script_text_layout.setSpacing(2)
        script_text_layout.addWidget(script_label)
        script_text_layout.addWidget(script_name)
        
        script_layout.addWidget(script_icon)
        script_layout.addLayout(script_text_layout)
        script_layout.addStretch()
        
        layout.addWidget(script_box)
        layout.addSpacing(15)
        
        # Execution steps
        self.step1 = StepIndicator(1, "Input Validation", "Files and data verified", "completed")
        layout.addWidget(self.step1)
        
        self.step2 = StepIndicator(2, "Processing Segmentation", "Running thermal gradient analysis...", "running")
        layout.addWidget(self.step2)
        
        self.step3 = StepIndicator(3, "JSON Generation", "Awaiting completion...", "pending")
        layout.addWidget(self.step3)
        
        layout.addSpacing(20)
        
        # Pending output section
        output_label = QLabel("PENDING OUTPUT")
        output_label.setStyleSheet("font-size: 10px; color: #9ca3af; font-weight: 600; margin-bottom: 10px;")
        layout.addWidget(output_label)
        
        output_items = [
            ("Generated Findings", "—"),
            ("Output Path", "—"),
            ("Case Reference", "#492")
        ]
        
        for label, value in output_items:
            item_layout = QHBoxLayout()
            item_label = QLabel(label)
            item_label.setStyleSheet("font-size: 12px; color: #6b7280;")
            item_value = QLabel(value)
            item_value.setStyleSheet("font-size: 12px; color: #9ca3af;")
            
            item_layout.addWidget(item_label)
            item_layout.addStretch()
            item_layout.addWidget(item_value)
            
            layout.addLayout(item_layout)
        
        layout.addStretch()
        self.setLayout(layout)

class ThermalSegStage1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ThermalSeg Analytics - Stage 1")
        self.setGeometry(100, 100, 1100, 650)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Header
        self.create_header(main_layout)
        
        # Content area
        content = QWidget()
        content.setStyleSheet("background-color: #f9fafb;")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(40, 30, 40, 30)
        
        # Breadcrumb
        breadcrumb = QHBoxLayout()
        home_link = QLabel('<a href="#" style="color: #6b7280; text-decoration: none;">Home</a>')
        home_link.setStyleSheet("font-size: 12px;")
        breadcrumb.addWidget(home_link)
        breadcrumb.addWidget(QLabel('<span style="color: #d1d5db; font-size: 12px;">/</span>'))
        cases_link = QLabel('<a href="#" style="color: #6b7280; text-decoration: none;">Cases</a>')
        cases_link.setStyleSheet("font-size: 12px;")
        breadcrumb.addWidget(cases_link)
        breadcrumb.addWidget(QLabel('<span style="color: #d1d5db; font-size: 12px;">/</span>'))
        current = QLabel("Case #492 - Stage 1")
        current.setStyleSheet("font-size: 12px; color: #111827; font-weight: 600;")
        breadcrumb.addWidget(current)
        breadcrumb.addStretch()
        content_layout.addLayout(breadcrumb)
        
        content_layout.addSpacing(15)
        
        # Title and buttons
        title_row = QHBoxLayout()
        title = QLabel("Input Selection & Stage 1")
        title.setStyleSheet("Color: black; font-size: 26px; font-weight: bold;")
        title_row.addWidget(title)
        title_row.addStretch()
        
        history_btn = QPushButton("📋 History")
        history_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #f9fafb;
            }
        """)
        history_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        title_row.addWidget(history_btn)
        
        help_btn = QPushButton("❓ Help")
        help_btn.setStyleSheet(history_btn.styleSheet())
        help_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        title_row.addWidget(help_btn)
        
        content_layout.addLayout(title_row)
        
        subtitle = QLabel("Configure inputs and execute thermal stage segmentation algorithm.")
        subtitle.setStyleSheet("font-size: 13px; color: #6b7280; margin-bottom: 20px;")
        content_layout.addWidget(subtitle)
        
        # Main panels
        panels_layout = QHBoxLayout()
        panels_layout.setSpacing(20)
        
        config_panel = ConfigPanel()
        exec_panel = ExecutionPanel()
        
        panels_layout.addWidget(config_panel, stretch=1)
        panels_layout.addWidget(exec_panel, stretch=1)
        
        content_layout.addLayout(panels_layout)
        content_layout.addStretch()
        
        main_layout.addWidget(content)
    
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
        logo = QLabel("🔬")
        logo.setStyleSheet("font-size: 22px;")
        header_layout.addWidget(logo)
        
        title = QLabel("ThermalSeg Analytics")
        title.setStyleSheet("font-size: 15px; font-weight: 600; color: #111827;")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        # Server status
        status_indicator = QLabel("●")
        status_indicator.setStyleSheet("color: #10b981; font-size: 12px;")
        header_layout.addWidget(status_indicator)
        
        status_label = QLabel("Local Server Connected")
        status_label.setStyleSheet("font-size: 12px; color: #6b7280;")
        header_layout.addWidget(status_label)
        
        # Settings
        settings_btn = QPushButton("⚙")
        settings_btn.setStyleSheet("""
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
        settings_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        header_layout.addWidget(settings_btn)
        
        # User
        user_btn = QPushButton("👤")
        user_btn.setStyleSheet(settings_btn.styleSheet())
        user_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        header_layout.addWidget(user_btn)
        
        layout.addWidget(header)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    window = ThermalSegStage1()
    window.show()
    
    sys.exit(app.exec())