import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import pyaudio
import threading
import json
from vosk import Model, KaldiRecognizer

# Load model (change path if needed)
# vosk-model-small-hi-0.22 and vosk-model-small-en-in-0.4
model = Model("C:/Users/pawan/PythonProjects/Vosk/vosk-model-small-en-in-0.4")

# Global variables
stream = None
mic = None
rec = None
recognizing = False

# Get available input devices
def get_input_devices():
    p = pyaudio.PyAudio()
    devices = []
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if dev['maxInputChannels'] > 0:
            devices.append((i, dev['name']))
    p.terminate()
    return devices

# Recognition function (runs in background)
def recognize(device_index, text_widget):
    global stream, mic, rec, recognizing
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
                      input_device_index=device_index, frames_per_buffer=8192)
    rec = KaldiRecognizer(model, 16000)
    stream.start_stream()

    try:
        while recognizing:
            data = stream.read(4096, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text_widget.insert(tk.END, result['text'] + "\n")
                text_widget.see(tk.END)
            else:
                partial = json.loads(rec.PartialResult())
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        stream.stop_stream()
        stream.close()
        mic.terminate()

# Start/Stop Button Handler
def toggle_recognition(text_widget, device_box, btn):
    global recognizing
    if not recognizing:
        try:
            device_index = int(device_box.get().split(" - ")[0])
            recognizing = True
            btn.config(text="Stop")
            thread = threading.Thread(target=recognize, args=(device_index, text_widget))
            thread.start()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        recognizing = False
        btn.config(text="Start")

# GUI setup
def main():
    root = tk.Tk()
    root.title("Voice Recognition And Speech To Text")
    root.geometry("600x400")

    # Mic Selection
    tk.Label(root, text="Select Microphone:").pack(pady=5)
    devices = get_input_devices()
    device_box = ttk.Combobox(root, values=[f"{i} - {name}" for i, name in devices], state="readonly")
    device_box.pack(pady=5)
    if devices:
        device_box.current(0)

    # Start/Stop Button
    btn = tk.Button(root, text="Start", command=lambda: toggle_recognition(output, device_box, btn))
    btn.pack(pady=10)

    # Output Text Area
    output = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
    output.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
