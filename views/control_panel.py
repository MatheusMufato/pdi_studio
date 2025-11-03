import tkinter as tk
from tkinter import scrolledtext, Scale, Frame, Label, Button

class ControlPanel:
    def __init__(self, root, controller):
        self.controller = controller

        self.frame = tk.Frame(root, bg="#333", width=300) # Largura aumentada
        self.frame.pack_propagate(False)

        controls_frame = Frame(self.frame, bg="#333")
        controls_frame.pack(pady=10, padx=10, fill="x")

        Label(controls_frame, text="Brilho", fg="white", bg="#333").pack()
        self.brightness_slider = Scale(controls_frame, from_=-127, to=127, orient=tk.HORIZONTAL, bg="#555", fg="white", troughcolor="#444")
        self.brightness_slider.set(0)
        self.brightness_slider.pack(fill="x", pady=2)

        Label(controls_frame, text="Contraste (x10)", fg="white", bg="#333").pack()
        self.contrast_slider = Scale(controls_frame, from_=1, to=30, orient=tk.HORIZONTAL, bg="#555", fg="white", troughcolor="#444")
        self.contrast_slider.set(10)
        self.contrast_slider.pack(fill="x", pady=2)

        Button(controls_frame, text="Aplicar Brilho/Contraste", command=self.on_apply_brightness_contrast).pack(pady=5)

        Label(controls_frame, text="Limiar Global", fg="white", bg="#333").pack()
        self.threshold_slider = Scale(controls_frame, from_=0, to=255, orient=tk.HORIZONTAL, bg="#555", fg="white", troughcolor="#444")
        self.threshold_slider.set(127)
        self.threshold_slider.pack(fill="x", pady=2)

        Button(controls_frame, text="Aplicar Limiar Global", command=self.on_apply_threshold).pack(pady=5)

        Frame(self.frame, height=2, bg="#555").pack(fill="x", padx=5, pady=10)

        tk.Label(self.frame, text="Histórico de Ações", fg="white", bg="#333").pack(pady=5)
        self.log_area = scrolledtext.ScrolledText(self.frame, width=35, height=20, bg="#111", fg="white") # Altura ajustada
        self.log_area.pack(padx=10, pady=10, fill="both", expand=True)

    def on_apply_brightness_contrast(self):
        brightness = self.brightness_slider.get()
        contrast = self.contrast_slider.get() / 10.0

        self.controller.apply_brightness_contrast(brightness, contrast)

    def on_apply_threshold(self):
        threshold_value = self.threshold_slider.get()
        self.controller.apply_global_threshold(threshold_value)


    def add_log(self, text):
        self.log_area.insert(tk.END, f"> {text}\n")
        self.log_area.see(tk.END)
