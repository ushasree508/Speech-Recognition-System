
import wave
import json
import vosk
import os
import tkinter as tk
from tkinter import filedialog

def transcribe_audio_vosk():
    # Ask the user to select an audio file
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    audio_path = filedialog.askopenfilename(title="Select a WAV File", filetypes=[("WAV Files", "*.wav")])

    if not audio_path:
        print("⚠️ No file selected. Exiting...")
        return

    model_path = r"C:\Users\pothi\OneDrive\Desktop\Speech Recg\model"

    if not os.path.exists(audio_path):
        raise Exception(f"⚠️ Audio file not found: {audio_path}")

    if not os.path.exists(model_path):
        raise Exception(f"⚠️ Model folder not found: {model_path}")

    model = vosk.Model(model_path)
    wf = wave.open(audio_path, "rb")
    recognizer = vosk.KaldiRecognizer(model, wf.getframerate())

    text = ""

    # Increase read chunk size
    while True:
        data = wf.readframes(8000)  # Increased from 4000 to 8000
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text += result.get("text", "") + " "

    final_result = json.loads(recognizer.FinalResult())
    text += final_result.get("text", "")

    print("\n🔹 Transcribed Text:\n", text.strip())

    # Save transcription to a text file
    transcription_file = "transcription.txt"
    with open(transcription_file, "w") as f:
        f.write(text.strip())

    print(f"✅ Transcription saved to {transcription_file}")

# Call function
transcribe_audio_vosk()
