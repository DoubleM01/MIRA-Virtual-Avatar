import tkinter as tk
from tkinter import ttk
import subprocess, threading, time, os
import cv2
from PIL import Image, ImageTk

# Define pre-defined sentences and expressions
sentences = ["Hello, how can I assist you?", "What's the weather like?", "Tell me a joke!", "Goodbye!"]
expressions = ["Anger", "Disgust", "Fear", "Joy", "Neutral", "Sadness", "Surprise"]

# Dark mode colors
BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
BTN_COLOR = "#2d2d2d"
HIGHLIGHT_COLOR = "#3a3a3a"
FONT = ("Segoe UI", 10)

# GUI setup
root = tk.Tk()
root.title("MIRA - Virtual Avatar Interface")
root.geometry("800x600")
root.configure(bg=BG_COLOR)

# Frame for selections
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(pady=20)

# Sentence selection
sentence_label = tk.Label(main_frame, text="Select a Sentence:", bg=BG_COLOR, fg=FG_COLOR, font=FONT)
sentence_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
sentence_var = tk.StringVar(value=sentences[0])
sentence_menu = ttk.Combobox(main_frame, textvariable=sentence_var, values=sentences, width=40)
sentence_menu.grid(row=0, column=1, pady=5)

# Custom input
custom_label = tk.Label(main_frame, text="Or Enter a Custom Sentence:", bg=BG_COLOR, fg=FG_COLOR, font=FONT)
custom_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
custom_entry = tk.Entry(main_frame, width=43)
custom_entry.grid(row=1, column=1, pady=5)

# Expression selection
expression_label = tk.Label(main_frame, text="Select Facial Expression:", bg=BG_COLOR, fg=FG_COLOR, font=FONT)
expression_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
expression_var = tk.StringVar(value=expressions[0])
expression_menu = ttk.Combobox(main_frame, textvariable=expression_var, values=expressions, width=40)
expression_menu.grid(row=2, column=1, pady=5)

# Auto/manual radio buttons
mode_label = tk.Label(main_frame, text="Expression Mode:", bg=BG_COLOR, fg=FG_COLOR, font=FONT)
mode_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
mode_var = tk.StringVar(value="Auto")
auto_radio = tk.Radiobutton(main_frame, text="Auto", variable=mode_var, value="Auto", bg=BG_COLOR, fg=FG_COLOR, font=FONT, selectcolor=HIGHLIGHT_COLOR)
auto_radio.grid(row=3, column=1, sticky="w")
manual_radio = tk.Radiobutton(main_frame, text="Manual", variable=mode_var, value="Manual", bg=BG_COLOR, fg=FG_COLOR, font=FONT, selectcolor=HIGHLIGHT_COLOR)
manual_radio.grid(row=3, column=1, sticky="e")

# Output label
output_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=("Segoe UI", 10, "italic"))
output_label.pack(pady=10)

# Progress bar for loading
progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
progress.pack(pady=10)

# Function to play video with audio using VLC
def play_video_with_audio():
    subprocess.Popen(["python", "video_player.py"])


# Run the TTS script and avatar generation script
def run_utils_script(sentence, expression):
    video_path = "output/results.mp4"
    os.remove(video_path) if os.path.exists(video_path) else None  # Remove old video file if exists
    progress.start()
    try:
        output_label.config(text="Generating Audio...")
        subprocess.run(["python", "tts_model.py", "--text", sentence])
    finally:
        output_label.config(text="Audio output completed.")
        time.sleep(1)
    try:
        output_label.config(text="Generating Avatar...")
        os.chdir("SadTalker")
        subprocess.run([
            "python", "inference.py", "--driven_audio", "../files/output.wav",
            "--source_image", f"../files/new/{expression.lower()}.png",
            "--still", "--preprocess", "full", "--result_dir", "../output/", "--enhancer", "gfpgan"
        ])
        os.chdir("..")
        play_video_with_audio()
    finally:
        progress.stop()
        output_label.config(text="Avatar output completed.")

def display_selection():
    selected_sentence = custom_entry.get() if custom_entry.get() else sentence_var.get()
    selected_expression = expression_var.get() if mode_var.get() == "Manual" else "Neutral"
    thread = threading.Thread(target=run_utils_script, args=(selected_sentence, selected_expression))
    thread.start()
    output_text = f"MIRA will say: '{selected_sentence}' with '{selected_expression}' expression."
    output_label.config(text=output_text)

# Display button
display_button = tk.Button(root, text="Display Avatar Output", command=display_selection, bg=BTN_COLOR, fg=FG_COLOR, font=("Segoe UI", 11, "bold"), padx=20, pady=10)
display_button.pack(pady=15)
root.mainloop()
