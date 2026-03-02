# SPIDR Frontend

## Overview

**SPIDR Frontend** is the graphical user interface layer of the SPIDR (Smart Processing Interface for Diagnostic Radiology) system. It provides an interactive desktop interface for radiologists and researchers to upload MRI scans, visualize segmentation outputs, and generate AI-assisted diagnostic reports.

The frontend integrates with:

* MONAI-based BRATS MRI segmentation backend
* LLM-powered medical report generation module
* Local or API-based inference services

The application is built using **PyQt6** and follows a modular UI architecture for scalability and maintainability.

---

## Core Features

* MRI image upload (NIfTI / DICOM support)
* Multi-panel scan visualization
* Tumor segmentation overlay
* Model inference status tracking
* AI-generated structured radiology reports
* Export reports (PDF / text)
* Modular stacked widget UI navigation

---

## Architecture

```
SPIDR/
│
├── ui/
│   ├── main_window.py
│   ├── stacked_views/
│   ├── components/
│
├── services/
│   ├── inference_client.py
│   ├── report_generator.py
│
├── assets/
│
└── main.py
```

### Design Principles

* Separation of UI and inference logic
* Service-based backend communication
* Expandable widget-based layout
* Clean signal-slot architecture (Qt event model)

---

## Tech Stack

* Python 3.10+
* PyQt6
* MONAI (backend integration)
* Hugging Face Transformers (LLM integration)
* SQLite (local metadata storage, optional)

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/SPIDR-Frontend.git
cd SPIDR-Frontend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python main.py
```

---

## Build Standalone Executable

Using PyInstaller:

```bash
pyinstaller --onefile --windowed --collect-all PyQt6 main.py
```

Output will be available in:

```
dist/
```

---

## Workflow

1. Launch application
2. Upload MRI scan
3. Trigger segmentation inference
4. Visualize tumor mask overlay
5. Generate structured AI-assisted report
6. Export report for clinical review

---

## Backend Integration

The frontend communicates with the inference backend via:

* Local Python service calls
* REST API endpoints (optional deployment)
* Model-in-memory execution (development mode)

Ensure backend is running before triggering inference.

---

## Future Improvements

* 3D volumetric viewer
* Model confidence visualization
* Multi-model comparison
* PACS integration
* Cloud inference deployment
* User authentication system

---

## Intended Users

* Radiologists
* Medical imaging researchers
* AI healthcare developers
* Academic researchers working on BRATS dataset

---

## Project Status

Active development
Research + Deployment hybrid system

---

## License

MIT License

Copyright (c) 2026 Misbahur Rahman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---

## Author

Misbahur Rahman
B.Tech | AI/ML & Intelligent Systems
Focused on medical AI deployment and scalable model integration

---
