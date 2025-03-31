import torch
from TTS.api import TTS
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--text", type=str,  default="Hello, World!", help="Text to convert to speech")
args = parser.parse_args()
text = args.text

device = "cuda" if torch.cuda.is_available() else "cpu"

print(TTS().list_models())
# voice(model) selection
tts = TTS("tts_models/en/jenny/jenny").to(device)

# Text to speech to a file
tts.tts_to_file(text=text,  file_path="files/output.wav")

# Text to speech to a file with different tone (pitch and speed)
# uncomment the next line to use a different tone --|---|--
#                                                   v   v
#tts.tts_to_file(text=text,  file_path="files/output.wav", speed=1.2, pitch=1.5)