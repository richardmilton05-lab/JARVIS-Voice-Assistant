# JARVIS Voice Assistant

A Python-based desktop voice assistant developed as a Phase 1 personal project.

JARVIS can recognize voice commands, respond using text-to-speech, launch Windows applications, open websites, perform web searches, and use a voice activation system.

## Table of Contents

- [Phase 1 Features](#phase-1-features)
- [How It Works](#how-it-works)
- [Voice Activation](#voice-activation)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Example Commands](#example-commands)
- [Requirements](#requirements)
- [Running JARVIS](#running-jarvis)
- [Project Status](#project-status)
- [Known Limitations](#known-limitations)
- [Future Development](#future-development)
- [License](#license)
- [Author](#author)

## Phase 1 Features

- Voice command recognition
- Text-to-speech responses
- Voice activation using the wake word "Launch"
- Lock and unlock listening mode
- Windows application control
- Website launching
- Google search
- YouTube search
- GitHub search
- ChatGPT search
- Voice-controlled time
- Desktop JARVIS folder creation
- Windows launcher

## How It Works

```
Voice
  |
  v
Speech Recognition
  |
  v
JARVIS Listener
  |
  v
Brain / Command Processing
  |
  v
Automation
  |
  +------ Windows Applications
  |
  +------ Websites
  |
  +------ Search
  |
  v
JARVIS Response
```

## Voice Activation

JARVIS starts in a locked state.

```
Locked
   |
   v
"Launch"
   |
   v
Activated
   |
   v
Voice Commands
   |
   v
"Lock Jarvis"
   |
   v
Locked
```

## Project Structure

```
JARVIS/
|
├── main.py
├── start_jarvis.bat
├── launch_jarvis.vbs
├── README.md
├── .gitignore
|
└── assistant/
    ├── brain.py
    ├── listener.py
    ├── speech.py
    ├── automation.py
    └── config.py
```

## Technologies

- Python
- SpeechRecognition
- pyttsx3
- Pygame
- Windows automation
- Web browser automation

## Example Commands

```
"Launch"
"Open Chrome"
"Open VS Code"
"Open WhatsApp"
"Open Calculator"
"Open Notepad"
"Open Paint"
"What is the time?"
"Search Google for embedded systems"
"Search YouTube for Python tutorials"
"Search GitHub for ESP32 projects"
"Search ChatGPT for how PWM works"
"Lock Jarvis"
"Exit"
```

## Requirements

- Windows 10 or Windows 11
- Python 3.x
- Working microphone
- Internet connection for online search features

## Running JARVIS

Run:

```
python main.py
```

or use:

```
start_jarvis.bat
```

## Project Status

Phase 1 - Completed

The core voice assistant, speech recognition, text-to-speech, application launching, web searching, and voice activation system are working.

## Known Limitations

This is a personal Phase 1 learning project, not a finished commercial assistant. Current limitations include:

- Commands are matched using fixed phrases rather than full natural language understanding
- Application paths (e.g. VS Code) are currently hardcoded and may need adjusting for other machines
- No persistent memory between sessions yet
- Search features require an internet connection

## Future Development

Planned future phases include:

- Natural language command understanding
- More Windows automation
- File and folder management
- Browser automation
- JARVIS memory
- Plugin system
- Improved wake-word detection
- Voice identification
- Desktop GUI
- More advanced assistant capabilities


## Author

Richard Milton

This project was created as a personal learning and development project.
