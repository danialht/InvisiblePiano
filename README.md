# Invisible Piano: Computer Vision, Signal Processing, and Art!

## Introduction
A virtual piano which you can play by showing your hands to the camera and moving you fingers. Your hand movements are going to be detected and depending on your finger poisitions the approprate key will be pressed.
There is also a python notebook included were simple signal processing ideas are discussed and the piano sounds are created using the code in the notebook.

## Libraries
Here a list of some of the libraries used in this project are included and a brief summary of their use:

- MediaPipe: Google's MediaPipe has a hand landmarks detector model which was used in order to detect the position of fingers and hand landmarks
- CV2: mostly for processing the captured video from webcam and drawing landmarks and their connections on it
- librosa: for audio processing and creating different notes
- Pygame: used for playing sound and showing second window which included the keys and the showed if they were pressed or not

## Installation
You could go to Code > Download Zip to download the repository, or alternatively use the following command:
```bash
git clone https://github.com/danialht/InvisiblePiano.git
```
run the main.py file to start.
```bash
python main.py
```
