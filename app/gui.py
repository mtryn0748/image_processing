import tkinter as tk

from tkinter import filedialog
from tkinter import ttk

from app.video_processor import VideoProcessor


class CounterGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title(
            "Vehicle & Human Counter"
        )

        self.root.geometry("800x800")

        self.root.configure(bg="#f4f6f9")

        self.root.resizable(False, False)

        self.video_path = ""

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Vehicle & Human Counter",
            font=("Arial", 24, "bold"),
            bg="#f4f6f9",
            fg="#1e3a5f"
        )

        title.pack(pady=25)

        subtitle = tk.Label(
            self.root,
            text="YOLOv8 + ByteTrack Based Counting System",
            font=("Arial", 11),
            bg="#f4f6f9",
            fg="gray"
        )

        subtitle.pack(pady=5)

        card_frame = tk.Frame(
            self.root,
            bg="white",
            bd=1,
            relief="solid"
        )

        card_frame.pack(
            padx=40,
            pady=25,
            fill="both",
            expand=False
        )

        path_title = tk.Label(
            card_frame,
            text="Selected Video",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#1e3a5f"
        )

        path_title.pack(pady=(20, 5))

        self.path_label = tk.Label(
            card_frame,
            text="No video selected",
            wraplength=500,
            bg="white",
            fg="black",
            font=("Arial", 10)
        )

        self.path_label.pack(pady=10)

        self.status_label = tk.Label(
            card_frame,
            text="System Ready",
            fg="green",
            bg="white",
            font=("Arial", 10, "bold")
        )

        self.status_label.pack(pady=5)

        select_button = tk.Button(
            card_frame,
            text="Select Video",
            command=self.select_video,
            width=22,
            height=2,
            bg="#2563eb",
            fg="white",
            font=("Arial", 11, "bold"),
            bd=0,
            cursor="hand2"
        )

        select_button.pack(pady=20)

        mode_label = tk.Label(
            card_frame,
            text="Detection Mode",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#1e3a5f"
        )

        mode_label.pack(pady=10)

        self.mode_var = tk.StringVar()

        self.mode_var.set("Tümü")

        style = ttk.Style()

        style.theme_use("clam")

        mode_menu = ttk.Combobox(
            card_frame,
            textvariable=self.mode_var,
            values=[
                "İnsan",
                "Araç",
                "Tümü"
            ],
            state="readonly",
            font=("Arial", 11),
            width=20
        )

        mode_menu.pack(pady=10)

        start_button = tk.Button(
            card_frame,
            text="Start Detection",
            command=self.start_detection,
            width=22,
            height=2,
            bg="#16a34a",
            fg="white",
            font=("Arial", 12, "bold"),
            bd=0,
            cursor="hand2"
        )

        start_button.pack(pady=30)

        footer = tk.Label(
            self.root,
            text="Computer Vision Project - YOLOv8n CPU Optimized",
            font=("Arial", 9),
            bg="#f4f6f9",
            fg="gray"
        )

        footer.pack(side="bottom", pady=15)

    def select_video(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                (
                    "Video Files",
                    "*.mp4 *.avi *.mov"
                )
            ]
        )

        if file_path:
            self.video_path = file_path

            self.path_label.config(
                text=file_path
            )

            self.status_label.config(
                text="Video Selected",
                fg="#2563eb"
            )

    def start_detection(self):
        if not self.video_path:
            self.status_label.config(
                text="Please Select a Video",
                fg="red"
            )
            return

        self.status_label.config(
            text="Detection Running...",
            fg="#dc2626"
        )

        self.root.withdraw()

        processor = VideoProcessor(
            video_path=self.video_path,
            mode=self.mode_var.get()
        )

        processor.process()

        self.root.deiconify()

        self.status_label.config(
            text="System Ready",
            fg="green"
        )

    def run(self):
        self.root.mainloop()

