import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO
import os

class YoloPhoneDetectorGUI:
    def __init__(self, root, model_path, default_video_path):
        self.root = root
        self.root.title("YOLO Phone Detection System")
        self.root.geometry("900x680")
        self.root.configure(bg="#1e1e2e")

        # Load YOLO Model
        self.model = YOLO(model_path)

        # Video variables initialization
        self.video_path = default_video_path
        self.cap = None
        self.is_playing = False

        # Build GUI Widgets
        self.build_ui()

    def build_ui(self):
        # Header Title
        title_label = tk.Label(
            self.root, 
            text="📱 Phone Detection - Video Player GUI", 
            font=("Arial", 16, "bold"), 
            fg="#ffffff", 
            bg="#1e1e2e"
        )
        title_label.pack(pady=10)

        # Main Video Display Area
        self.video_label = tk.Label(
            self.root, 
            bg="#11111b", 
            text="Click 'Start Detection' to run video", 
            fg="#a6adc8", 
            font=("Arial", 12)
        )
        self.video_label.pack(expand=True, fill="both", padx=20, pady=10)

        # Bottom Control Panel
        control_panel = tk.Frame(self.root, bg="#1e1e2e")
        control_panel.pack(fill="x", pady=10)

        # File path info label
        self.path_label = tk.Label(
            control_panel, 
            text=f"Selected File: {os.path.basename(self.video_path)}", 
            font=("Arial", 9), 
            fg="#bac2de", 
            bg="#1e1e2e"
        )
        self.path_label.pack(pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(control_panel, bg="#1e1e2e")
        btn_frame.pack()

        # Browse Video Button
        self.btn_browse = tk.Button(
            btn_frame, 
            text="📁 Browse Video", 
            font=("Arial", 10, "bold"), 
            bg="#89b4fa", 
            fg="#11111b", 
            command=self.browse_video,
            padx=10, pady=5
        )
        self.btn_browse.grid(row=0, column=0, padx=10)

        # Start Button
        self.btn_start = tk.Button(
            btn_frame, 
            text="▶ Start Detection", 
            font=("Arial", 10, "bold"), 
            bg="#a6e3a1", 
            fg="#11111b", 
            command=self.start_video,
            padx=10, pady=5
        )
        self.btn_start.grid(row=0, column=1, padx=10)

        # Stop Button
        self.btn_stop = tk.Button(
            btn_frame, 
            text="⏹ Stop", 
            font=("Arial", 10, "bold"), 
            bg="#f38ba8", 
            fg="#11111b", 
            command=self.stop_video,
            padx=10, pady=5
        )
        self.btn_stop.grid(row=0, column=2, padx=10)

    def browse_video(self):
        """Open file dialog to choose a custom video file"""
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
        )
        if file_path:
            self.stop_video()
            self.video_path = file_path
            self.path_label.config(text=f"Selected File: {os.path.basename(self.video_path)}")

    def start_video(self):
        """Start or restart the video inference loop"""
        if not self.video_path or not os.path.exists(self.video_path):
            self.video_label.config(text="Error: Video file not found!")
            return

        if not self.is_playing:
            self.cap = cv2.VideoCapture(self.video_path)
            self.is_playing = True
            self.update_frame()

    def stop_video(self):
        """Stop video playback and release resources"""
        self.is_playing = False
        if self.cap:
            self.cap.release()
            self.cap = None
        self.video_label.config(image="", text="Video Stopped. Click Start to Play again.")

    def update_frame(self):
        """Main loop to read, infer, and render each video frame inside GUI"""
        if self.is_playing and self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Run YOLO prediction
                results = self.model.predict(source=frame, conf=0.5, verbose=False)
                annotated_frame = results[0].plot()

                # Convert BGR (OpenCV) to RGB (PIL format)
                rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

                # Resize frame dynamically to fit GUI canvas
                max_w, max_h = 800, 450
                h, w, _ = rgb_frame.shape
                scale = min(max_w / w, max_h / h)
                new_w, new_h = int(w * scale), int(h * scale)
                resized_frame = cv2.resize(rgb_frame, (new_w, new_h))

                # Convert array to Image and then to PhotoImage
                img = Image.fromarray(resized_frame)
                imgtk = ImageTk.PhotoImage(image=img)

                # Update Tkinter Label
                self.video_label.imgtk = imgtk
                self.video_label.config(image=imgtk, text="")

                # Schedule next frame update (~30 fps)
                self.root.after(30, self.update_frame)
            else:
                # End of video file reached
                self.stop_video()
                self.video_label.config(text="Video Finished Successfully!")

    def on_closing(self):
        """Clean shutdown when closing window"""
        self.stop_video()
        self.root.destroy()

if __name__ == "__main__":
    # Absolute paths
    MODEL_PATH = r"D:\Downloads\exp.pt"
    VIDEO_PATH = r"D:\Desktop\WhatsApp Video 2026-08-12 at 12.14.30 AM.mp4"

    # Run GUI Application
    root = tk.Tk()
    app = YoloPhoneDetectorGUI(root, MODEL_PATH, VIDEO_PATH)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()