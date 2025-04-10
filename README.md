# MIRA Virtual Avatar

A comprehensive project for generating realistic text-to-speech (TTS), emotion-based avatars, and synchronized video outputs. This project integrates multiple services to create a seamless pipeline for generating expressive avatars with synchronized audio and video.

---

## Features

- **Text-to-Speech (TTS):** Generate realistic speech from text using advanced TTS models.
- **Emotion-Based Avatars:** Create avatars that reflect specific emotions based on input parameters.
- **Video Generation:** Produce synchronized video outputs with audio and avatar animations.
- **Customizable Pipelines:** Modular design for integrating additional features or models.

---

## Directory Structure

```plaintext
📂 TTS/          # Text-to-Speech service
📂 SadTalker/    # Emotion-based avatar generation
📂 files/       # Avatar assets and configurations
📂 output/       # Generated outputs (audio, video, etc.)
📂 scripts/      # Utility scripts for automation
```

---

## Requirements

- **Python:** 3.8 or later
- **TTS** 
- **SadTalker:** with some source modifications 
- **CUDA** recommeneded but not required 
- **Other Dependencies:** Listed in the respective `requirements.txt` files for each service.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DoubleM01/MIRA-Virtual-Avatar.git
   cd MIRA-Virtual-Avatar
   ```

2. Install dependencies for each service:
   ```bash
   cd TTS
   pip install -r requirements.txt
   cd ../SadTalker
   pip install -r requirements.txt
   ```

---

## Usage

1. Start the GUI local version:
   ```python
   python main.py
   ```

2. Start gradio version:
   ```python
   python app.py
   ```

3. Use the gradio server for avatar generation "local host" at `http://127.0.0.1:7860`.

4. Preview available for both of GUI and gradio.
5. Generated outputs will be saved as a file  `output/results.mp4`.

---


## Results


https://github.com/user-attachments/assets/7a075ce5-d119-430a-a600-f041ca52f921


## Notes

- Ensure all required models are downloaded and placed in the appropriate directories.
- script for downloading automation at 📂 scripts/ 
---

## Acknowledgments

This project leverages the following open-source tools and libraries:

- [TTS](https://github.com/coqui-ai/TTS) for text-to-speech generation.
- [SadTalker](https://github.com/Winfredy/SadTalker) for emotion-based avatar generation.
- [GFPGAN](https://github.com/TencentARC/GFPGAN) for face enhancement.

---

## License

This project is None-licensed.

---

## Contact

For questions or support, please open an issue on the [GitHub repository](https://github.com/DoubleM01/MIRA-Virtual-Avatar) or contact me at `mahmoud_2001m@outlook.com`.

---
