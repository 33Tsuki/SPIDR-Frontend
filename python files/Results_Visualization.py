import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QFrame, QScrollArea,
                             QGridLayout, QSizePolicy)
from PyQt6.QtCore import Qt, QSize, QRect, QPoint
from PyQt6.QtGui import QFont, QPixmap, QPainter, QColor, QLinearGradient, QPen
from PyQt6.QtGui import QFont, QPixmap, QPainter, QColor, QLinearGradient, QPen
import numpy as np
from styles import ModernDarkTheme

class ThermalImageWidget(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.title = title
        self.setMinimumSize(280, 200)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Create thermal gradient
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(255, 200, 0))
        gradient.setColorAt(0.3, QColor(255, 0, 255))
        gradient.setColorAt(0.6, QColor(128, 0, 200))
        gradient.setColorAt(1, QColor(0, 0, 100))
        
        painter.fillRect(0, 0, self.width(), self.height(), gradient)
        
        # Add some variation
        painter.setPen(Qt.PenStyle.NoPen)
        for _ in range(50):
            x = np.random.randint(0, self.width())
            y = np.random.randint(0, self.height())
            size = np.random.randint(20, 60)
            alpha = np.random.randint(30, 80)
            color = QColor(np.random.randint(100, 255), 
                          np.random.randint(0, 100), 
                          np.random.randint(100, 255), alpha)
            painter.setBrush(color)
            painter.drawEllipse(x, y, size, size)

class BarChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(180, 200)
        self.data = [3.5, 5.2, 1.8, 6.1]
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Background
        painter.fillRect(self.rect(), Qt.GlobalColor.white)
        
        # Draw bars
        bar_width = 30
        spacing = 50
        max_val = max(self.data)
        x_offset = 30
        
        for i, val in enumerate(self.data):
            x = x_offset + i * spacing
            height = int((val / max_val) * 150)
            y = 180 - height
            
            painter.fillRect(x, y, bar_width, height, QColor(ModernDarkTheme.PRIMARY))
            
        # Draw title
        painter.setPen(Qt.GlobalColor.black)
        painter.setFont(QFont('Arial', 8))
        painter.drawText(10, self.height() - 5, "Tissue Perfusion Rates")

class LineChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(180, 150)
        self.data = [2.1, 2.3, 2.2, 2.5, 2.4, 2.8, 2.6, 3.0]
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Background
        painter.fillRect(self.rect(), Qt.GlobalColor.white)
        
        # Draw line
        max_val = max(self.data)
        x_step = (self.width() - 40) / (len(self.data) - 1)
        y_scale = (self.height() - 40) / max_val
        
        pen = QPen(QColor(ModernDarkTheme.ACCENT), 2)
        painter.setPen(pen)
        
        for i in range(len(self.data) - 1):
            x1 = 20 + i * x_step
            y1 = self.height() - 20 - self.data[i] * y_scale
            x2 = 20 + (i + 1) * x_step
            y2 = self.height() - 20 - self.data[i+1] * y_scale
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))
            
        # Draw title
        painter.setPen(Qt.GlobalColor.black)
        painter.setFont(QFont('Arial', 8))
        painter.drawText(10, self.height() - 5, "Thermal Stability Index")

class CircularProgressWidget(QWidget):
    def __init__(self, value=85, title="Confidence", color="#2ecc71", parent=None):
        super().__init__(parent)
        self.value = value
        self.title = title
        self.color = color
        self.setMinimumSize(100, 100)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Background
        painter.fillRect(self.rect(), Qt.GlobalColor.white)
        
        rect = self.rect().adjusted(10, 10, -10, -10)
        size = min(rect.width(), rect.height())
        rect = QRect(rect.center().x() - size//2, rect.center().y() - size//2, size, size)
        
        # Draw background circle
        painter.setPen(QPen(QColor("#f0f0f0"), 6))
        painter.drawEllipse(rect)
        
        # Draw progress arc
        painter.setPen(QPen(QColor(self.color), 6, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        span_angle = int(-(self.value / 100) * 360 * 16)
        painter.drawArc(rect, 90 * 16, span_angle)
        
        # Draw value text
        painter.setPen(Qt.GlobalColor.black)
        painter.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, f"{self.value}%")
        
        # Draw title
        painter.setFont(QFont('Arial', 7))
        painter.drawText(rect.adjusted(0, 30, 0, 30), Qt.AlignmentFlag.AlignCenter, self.title)

class MetricCard(QFrame):
    def __init__(self, title, value, unit, color, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.Shape.StyledPanel)
        self.setStyleSheet(f"""
            QFrame {{
                {ModernDarkTheme.card_style()}
            }}
        """)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(15, 10, 15, 10)
        
        # Icon/Indicator
        icon_label = QLabel(self.get_icon(title))
        icon_label.setStyleSheet(f"color: {color}; font-size: 20px;")
        layout.addWidget(icon_label)
        
        # Content
        content_layout = QVBoxLayout()
        content_layout.setSpacing(2)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("color: #666; font-size: 11px;")
        
        value_label = QLabel(f"{value}{unit}")
        value_label.setStyleSheet(f"color: {color}; font-size: 18px; font-weight: bold;")
        
        content_layout.addWidget(title_label)
        content_layout.addWidget(value_label)
        
        layout.addLayout(content_layout)
        layout.addStretch()
        
        self.setLayout(layout)
        
    def get_icon(self, title):
        icons = {
            "Max Temp": "🌡️",
            "Thermal Index": "⊙",
            "Confidence Score": "✓",
            "Add Metric": "+"
        }
        return icons.get(title, "•")

class MediThermApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MediTherm")
        self.setGeometry(100, 100, 1200, 800)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        
        # Sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        
        # Main content area
        content_area = self.create_content_area()
        main_layout.addWidget(content_area, 1)
        
        # Apply styles
        # Apply styles
        self.setStyleSheet(ModernDarkTheme.get_stylesheet())
        
        # Additional custom styles if needed, or rely on global
        # self.setStyleSheet(...)
        
    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setMaximumWidth(200)
        sidebar.setStyleSheet(f"background-color: {ModernDarkTheme.SURFACE}; border-right: 1px solid {ModernDarkTheme.BORDER};")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Logo
        logo_label = QLabel("📊 MediTherm")
        logo_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 20px;")
        layout.addWidget(logo_label)
        
        # Menu items
        menu_items = ["Dashboard", "Analysis", "Cases", "Settings"]
        for i, item in enumerate(menu_items):
            btn = QPushButton(item)
            if item == "Analysis":
                btn.setStyleSheet(f"""
                    QPushButton {{
                        background-color: #E3F2FD;
                        color: {ModernDarkTheme.PRIMARY};
                        text-align: left;
                        padding: 12px 20px;
                        border: none;
                        border-radius: 0;
                    }}
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        color: #666;
                        text-align: left;
                        padding: 12px 20px;
                        border: none;
                        border-radius: 0;
                    }
                    QPushButton:hover {
                        background-color: #f5f5f5;
                    }
                """)
            layout.addWidget(btn)
        
        layout.addStretch()
        sidebar.setLayout(layout)
        return sidebar
        
    def create_content_area(self):
        content = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        header_layout = QHBoxLayout()
        
        title_label = QLabel("Case Analysis #492-AC")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        print_btn = QPushButton("🖨️ Print")
        print_btn.setStyleSheet("background-color: white; color: #333; border: 1px solid #ddd;")
        export_btn = QPushButton("⬇ Export Report")
        
        header_layout.addWidget(print_btn)
        header_layout.addWidget(export_btn)
        
        layout.addLayout(header_layout)
        
        # Subtitle
        subtitle = QLabel("Detailed thermal analysis results for Liver region scan")
        subtitle.setStyleSheet("color: #666; margin-bottom: 10px;")
        layout.addWidget(subtitle)
        
        # Info cards
        info_layout = QHBoxLayout()
        info_items = [
            ("CASE NUMBER", "#492-AC"),
            ("ORGAN NAME", "Liver"),
            ("FILE NAME", "seq_2023.10.04.seq"),
            ("PROCESSED", "Oct 24, 14:30")
        ]
        
        for label, value in info_items:
            card = QFrame()
            card.setStyleSheet("background-color: white; border-radius: 4px; padding: 10px;")
            card_layout = QVBoxLayout()
            
            label_widget = QLabel(label)
            label_widget.setStyleSheet("color: #999; font-size: 10px;")
            value_widget = QLabel(value)
            value_widget.setStyleSheet("color: #333; font-weight: bold;")
            
            card_layout.addWidget(label_widget)
            card_layout.addWidget(value_widget)
            card.setLayout(card_layout)
            
            info_layout.addWidget(card)
        
        layout.addLayout(info_layout)
        layout.addSpacing(20)
        
        # Main content grid
        content_grid = QHBoxLayout()
        
        # Left side - Thermal images
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        
        section_label = QLabel("Final Visual Image")
        section_label.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        left_layout.addWidget(section_label)
        
        # Thermal images grid
        thermal_grid = QGridLayout()
        thermal_grid.setSpacing(10)
        
        image_titles = [
            "Total Heat Acquired: 3.2",
            "Total Heat Acquired: 2.8",
            "Cold Spots Acquired: 1.4",
            "Cold Spots Acquired: 1.8"
        ]
        
        for i, title in enumerate(image_titles):
            img_widget = ThermalImageWidget(title)
            thermal_grid.addWidget(img_widget, i // 2, i % 2)
        
        left_layout.addLayout(thermal_grid)
        
        note_label = QLabel("Analysis Note: Automated anomaly detection identified a region of elevated temperature (+1.2°C baseline).")
        note_label.setStyleSheet("color: #666; font-size: 11px; margin-top: 10px;")
        note_label.setWordWrap(True)
        left_layout.addWidget(note_label)
        
        left_panel.setLayout(left_layout)
        content_grid.addWidget(left_panel, 2)
        
        # Right side - Charts and metrics
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setSpacing(15)
        
        # Bar chart
        chart_widget = BarChartWidget()
        chart_frame = QFrame()
        chart_frame.setStyleSheet(f"{ModernDarkTheme.card_style()} padding: 10px;")
        chart_frame_layout = QVBoxLayout()
        chart_frame_layout.addWidget(chart_widget)
        chart_frame.setLayout(chart_frame_layout)
        right_layout.addWidget(chart_frame)
        
        # Line chart
        line_chart_widget = LineChartWidget()
        line_chart_frame = QFrame()
        line_chart_frame.setStyleSheet(f"{ModernDarkTheme.card_style()} padding: 10px;")
        line_chart_frame_layout = QVBoxLayout()
        line_chart_frame_layout.addWidget(line_chart_widget)
        line_chart_frame.setLayout(line_chart_frame_layout)
        right_layout.addWidget(line_chart_frame)
        
        # Stage 1 Derived Images
        stage_label = QLabel("Stage 1 Derived Images")
        stage_label.setStyleSheet("font-weight: bold; font-size: 12px;")
        right_layout.addWidget(stage_label)
        
        # Circular progress in derived_frame or nearby
        derived_frame = QFrame()
        derived_frame.setStyleSheet(f"{ModernDarkTheme.card_style()} padding: 10px;")
        derived_frame_layout = QHBoxLayout()
        
        prog1 = CircularProgressWidget(92, "Anomaly Conf.", "#e74c3c")
        prog2 = CircularProgressWidget(85, "Scan Quality", "#3498db")
        
        derived_frame_layout.addWidget(prog1)
        derived_frame_layout.addWidget(prog2)
        derived_frame.setLayout(derived_frame_layout)
        right_layout.addWidget(derived_frame)
        
        right_layout.addStretch()
        right_panel.setLayout(right_layout)
        content_grid.addWidget(right_panel, 1)
        
        layout.addLayout(content_grid)
        layout.addSpacing(20)
        
        # Bottom metrics
        metrics_layout = QHBoxLayout()
        metrics = [
            ("Max Temp", "38.4", "°C", "#e74c3c"),
            ("Thermal Index", "0.85", "", "#3498db"),
            ("Confidence Score", "92", "%", "#2ecc71"),
            ("Add Metric", "", "", "#95a5a6")
        ]
        
        for title, value, unit, color in metrics:
            if title == "Add Metric":
                card = QFrame()
                card.setStyleSheet("background-color: white; border: 2px dashed #ddd; border-radius: 8px;")
                card_layout = QVBoxLayout()
                card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                add_label = QLabel("⊕ Add Metric")
                add_label.setStyleSheet("color: #999;")
                card_layout.addWidget(add_label)
                card.setLayout(card_layout)
                metrics_layout.addWidget(card)
            else:
                card = MetricCard(title, value, unit, color)
                metrics_layout.addWidget(card)
        
        layout.addLayout(metrics_layout)
        
        content.setLayout(layout)
        return content

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModernDarkTheme.setup_theme(app)
    window = MediThermApp()
    window.show()
    sys.exit(app.exec())