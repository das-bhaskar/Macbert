import os
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"  # or "/usr/local/bin" for Intel Macs

import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from rapidfuzz import process
import subprocess

COMMANDS = {
    # Browsers
    "open browser": "open -a Safari",
    "open safari": "open -a Safari",
    "open chrome": "open -a 'Google Chrome'",
    "open google chrome": "open -a 'Google Chrome'",
    "open firefox": "open -a Firefox",
    "open brave": "open -a Brave Browser",
    
    # Editors / IDEs
    "open vscode": "code",  # VSCode CLI
    "open visual studio code": "code",
    "open sublime": "open -a 'Sublime Text'",
    "open atom": "open -a Atom",

    # System apps
    "open terminal": "open -a Terminal",
    "open finder": "open -a Finder",
    "open notes": "open -a Notes",
    "open mail": "open -a Mail",
    "open calendar": "open -a Calendar",
    "open messages": "open -a Messages",
    "open music": "open -a Music",
    "open photos": "open -a Photos",
    
    # System controls
    "shutdown computer": "sudo shutdown -h now",
    "restart computer": "sudo shutdown -r now",
    "sleep computer": "pmset sleepnow",

    # Utilities
    "open activity monitor": "open -a 'Activity Monitor'",
    "open system preferences": "open -a 'System Preferences'",
    "open disk utility": "open -a 'Disk Utility'",
}

def record_audio(filename="temp.wav", duration=5, fs=16000):
    print("Recording started...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print(f"Recording saved as {filename}")

def transcribe_audio(filename="temp.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result['text']

def find_best_command(text):
    # Check exact match first
    if text in COMMANDS:
        return COMMANDS[text], text
    
    # Otherwise fuzzy match
    commands = COMMANDS.keys()
    best_match, score, _ = process.extractOne(text, commands)
    if score > 85:
        return COMMANDS[best_match], best_match
    return None, None

def execute_command(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"Executed: {cmd}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute {cmd}: {e}")

def main():
    record_audio()
    text = transcribe_audio()
    print(f"You said: {text}")

    cmd, phrase = find_best_command(text.lower())
    if cmd:
        print(f"Executing command: {cmd}")
        execute_command(cmd)
    else:
        print("Sorry, no matching command found.")

if __name__ == "__main__":
    main()
