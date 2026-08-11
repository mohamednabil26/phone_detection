# phone_detection
# 🛡️ ProctorAI Vision — Automated Exam Security & Behavioral Analytics

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-000000?style=for-the-badge&logo=yolo)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-indigo?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green?style=for-the-badge&logo=opencv)

**ProctorAI Vision** is an enterprise-grade Computer Vision application designed to automate classroom invigilation and maintain academic integrity. Powered by custom-trained **YOLO** deep learning models and a sleek **CustomTkinter** UI, the system monitors video streams in real time to instantly detect unauthorized smartphone usage during exams.

---

## 🌟 Key Features

* **⚡ Real-Time Object Detection Engine:** Processes video streams with low pipeline latency to detect mobile phone usage dynamically.
* **🎯 Target-Lock Forensics (Auto-Snapshot):** Automatically captures a high-context cropped snapshot (student face, hand orientation, and device) whenever a violation is detected.
* **📊 Enterprise Analytics Dashboard:** Live reporting of active incident counts, processing speed (FPS), latency (ms), and detection confidence scores.
* **📐 Aspect Ratio Preserver:** Proprietary scaling logic ensures zero video stretching, cropping, or distortion regardless of window size.
* **🎛️ Interactive Hyperparameter Controls:** Allows live adjustment of confidence threshold sensitivity directly from the interface.

---

## 💡 Business Impact & ROI

1. **Scalability:** Reduces the ratio of human invigilators required for large examination halls.
2. **Definitive Evidence:** Auto-generated incident logs provide undeniable visual and temporal proof for disciplinary committees.
3. **Operational Efficiency:** Frees educational institutions from manual monitoring errors and oversight.

---

## 🛠️ Tech Stack

* **Language:** Python 3.9+
* **Deep Learning Framework:** Ultralytics YOLO
* **Computer Vision:** OpenCV (`cv2`), PIL
* **GUI Engine:** CustomTkinter

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/proctor-ai-vision.git](https://github.com/your-username/proctor-ai-vision.git)
cd proctor-ai-vision
