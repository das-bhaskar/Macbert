# 🎙️ Macbert

**Macbert** is a minimalist voice-controlled transcription tool for macOS. It records a short voice clip using your microphone, transcribes it using OpenAI’s Whisper model, and (optionally) executes matched shell commands — all locally, no internet required after setup.

> 🛠️ Built in Python. Runs fully offline. Packaged into a single-file app if needed.

---

## ✨ Features

- 🎧 Records voice from your Mac’s microphone  
- 🧠 Transcribes locally using Whisper  
- ⚡ Works offline after install  
- 🚀 Can be compiled into a one-click Mac app using PyInstaller  
- 🔐 Does not send your audio to any server  

---

## 📦 Setup Instructions

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/yourusername/macbert.git
cd macbert
```

### 🧪 2. Create and Activate a Virtual Environment (Recommended)

```bash
python3 -m venv macbert-env
source macbert-env/bin/activate
```

### 📥 3. Install Required Packages

```bash
pip install git+https://github.com/openai/whisper
pip install sounddevice
pip install rapidfuzz
```

> If you're using Whisper for the first time, it may also download model weights the first time you run it.

---

## ▶️ How to Run

From inside the project directory:

```bash
python macbert.py
```

This will:

1. Record 5 seconds of audio via your mic  
2. Save it to `temp.wav`  
3. Transcribe the spoken text using the Whisper model  
4. Attempt to match the phrase to a shell command (e.g., "open Chrome")  
5. Execute the matched command without asking  

---

## 🧠 Example Commands You Can Say

| Phrase              | What It Does                         |
|---------------------|--------------------------------------|
| `open chrome`       | Launches Google Chrome               |
| `open vscode`       | Opens Visual Studio Code             |
| `open terminal`     | Opens Terminal                       |
| `shutdown computer` | Shuts down your Mac (⚠️ Be careful!) |

Commands are stored in the `COMMANDS` dictionary inside the script. You can add your own!

---

## 🧊 Building a One-Click App (Optional)

You can turn `macbert.py` into a standalone executable using **PyInstaller**.

### 🔧 1. Install PyInstaller

```bash
pip install pyinstaller
```

### ⚙️ 2. Build the Executable

```bash
pyinstaller --onefile \
--add-data "/path/to/mel_filters.npz:whisper/assets" \
--add-data "/path/to/multilingual.tiktoken:whisper/assets" \
macbert.py
```

> Replace the paths above with the correct locations on your system.

The output app will be found in `dist/macbert`.

Double-click it to run like a native app.

---

## 🤝 Credits

- [Whisper](https://github.com/openai/whisper) by OpenAI  
- [`sounddevice`](https://pypi.org/project/sounddevice/)  
- [`rapidfuzz`](https://github.com/maxbachmann/RapidFuzz)
