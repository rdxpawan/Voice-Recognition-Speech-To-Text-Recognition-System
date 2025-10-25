# 🎤 Voice Recognition and Speech-to-Text App (Tkinter + Vosk)

This is a simple **Speech-to-Text desktop application** built using **Python**, **Tkinter**, and **Vosk**.  
It allows you to select your microphone, start live voice recognition, and display the recognized text in real-time.

---

## 🧠 Features

✅ Real-time speech-to-text conversion  
✅ Supports multiple microphones  
✅ Lightweight Vosk offline recognition model (works without internet)  
✅ User-friendly GUI built with Tkinter  
✅ Start/Stop recognition with a single click  

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** (GUI)
- **Vosk** (Speech recognition)
- **PyAudio** (Audio stream)
- **Threading** (Background processing)
- **JSON** (For parsing recognition results)

---

## 📦 Installation

### 1️⃣ Clone or Download the Repository
```bash
git clone https://github.com/yourusername/voice-recognition-tkinter.git
cd voice-recognition-tkinter
````

### 2️⃣ Install Dependencies

Make sure you have Python installed. Then install the required packages:

```bash
pip install vosk pyaudio
```

> ⚠️ If `pyaudio` fails to install on Windows, run:
>
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🗣️ Download the Vosk Model

You’ll need an offline model for speech recognition.

### English (India)

Download from: [vosk-model-small-en-in-0.4](https://alphacephei.com/vosk/models)

### Hindi (Optional)

[vosk-model-small-hi-0.22](https://alphacephei.com/vosk/models)

After downloading, extract the model and place it in a folder (e.g.):

```
C:/Users/pawan/PythonProjects/Vosk/vosk-model-small-en-in-0.4
```

Then update the path in your code:

```python
model = Model("C:/Users/pawan/PythonProjects/Vosk/vosk-model-small-en-in-0.4")
```

---

## 🚀 Run the Application

Run the app using:

```bash
python app.py
```

### GUI Overview:

* **Select Microphone** → Choose input device
* **Start Button** → Begin recognition
* **Stop Button** → End recognition
* **Text Area** → Displays live transcribed text

---

## 🧩 Project Structure

```
📁 VoiceRecognitionApp
│
├── app.py                 # Main application code
├── README.md              # Project documentation
└── vosk-model-small-en-in-0.4/   # Speech recognition model folder
```

---

## 💡 Notes

* Works fully offline — no internet required after model download.
* You can switch to other Vosk models for different languages.
* Keep microphone permissions enabled for Python.

---

## 📸 Example Output

```
Recognized: hello world
Recognized: how are you today
Recognized: this is working great
```

---

## 👨‍💻 Author

**Pawan Kumar**
🎓 MCA Student at Graphic Era University, Dehradun
💻 Passionate about coding and AI-driven applications

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

```

---

Would you like me to make this README **GitHub-ready** (with clickable links, emoji headers, and badges like “Made with ❤️ in Python”)? I can prettify it for direct upload.
```
