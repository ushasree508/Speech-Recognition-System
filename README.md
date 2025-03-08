
# Speech Recognition System

## Company Details
- **Company:** CODTECH IT SOLUTIONS  
- **Intern Name:** ORSU USHA SREE  
- **Intern ID:** CT08TMH  
- **Domain:** ARTIFICIAL INTELLIGENCE  
- **Duration:** 4 WEEKS  
- **Mentor:** NEELA SANTOSH  

## Overview
This project is a **Speech Recognition System** that converts spoken language into text using pre-trained models and libraries such as `SpeechRecognition` and `Wav2Vec`. It is capable of transcribing short audio clips efficiently.

## Features
- Converts speech into text
- Supports multiple audio formats
- Uses pre-trained models for high accuracy
- Simple and easy-to-use interface

## Requirements
Ensure you have the following installed before running the project:
- Python (>= 3.7)
- `SpeechRecognition` library
- `pyaudio` (for microphone input)
- `wav2vec2` (for advanced recognition, optional)

## Installation
Run the following commands to set up the environment:
```bash
pip install SpeechRecognition pyaudio torchaudio transformers
```

## Usage
### 1. Transcribe from Microphone
Run the script to capture and transcribe speech:
```bash
python speech_recognition.py
```

### 2. Transcribe from an Audio File
Modify the script to load an audio file instead:
```python
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile('audio.wav') as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)
    print("Transcription:", text)
```



