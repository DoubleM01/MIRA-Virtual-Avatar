import gradio as gr
import subprocess
import os
import time

# Ensure output folder exists
os.makedirs("output", exist_ok=True)
def run_avatar_demo():
        video_path = "output/results.mp4"
        time.sleep(1)
        if os.path.exists(video_path):
                return video_path
        return ""

def run_avatar(text, expression):
    video_path = "output/results.mp4"
    if os.path.exists(video_path):
        os.remove(video_path)

    # Step 1: Run TTS
    subprocess.run(["python3", "tts_model.py", "--text", text])

    # Step 2: Run SadTalker
    os.chdir("SadTalker")
    subprocess.run([
        "python3", "inference.py",
        "--driven_audio", "../files/output.wav",
        "--source_image", f"../files/new/{expression.lower()}.png",
        "--still", "--preprocess", "full",
        "--result_dir", "../output/", 
        # uncomment to enable enhancer 
        # "--enhancer", "gfpgan"
    ])
    os.chdir("..")

    if os.path.exists(video_path):
        return video_path
    return ""

with gr.Blocks() as iface:
    gr.Markdown("# MIRA - Virtual Avatar Generator")
    gr.Markdown("Generate a talking avatar video with your selected emotion and custom sentence.")

    with gr.Row():
        text_input = gr.Textbox(label="Enter a sentence")
        expression_input = gr.Dropdown(["Anger", "Disgust", "Fear", "Joy", "Neutral", "Sadness", "Surprise"], label="Expression")  
    output_video = gr.Video(label="Generated Avatar")

    with gr.Row():
        generate_btn = gr.Button("Generate Avatar")
        demo_btn = gr.Button("Run Demo")

    generate_btn.click(fn=run_avatar, inputs=[text_input, expression_input], outputs=output_video)
    demo_btn.click(fn=run_avatar_demo, inputs=[], outputs=output_video)

iface.launch(server_name="127.0.0.1", server_port=7860)
