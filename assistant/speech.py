import subprocess


def speak(text):
    """
    Speak text using the built-in Windows Speech API.
    """

    print(f"Jarvis: {text}")

    # Escape single quotes for PowerShell
    text = str(text).replace("'", "''")

    command = f"""
    Add-Type -AssemblyName System.Speech;
    $speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer;
    $speaker.Rate = 0;
    $speaker.Volume = 100;
    $speaker.Speak('{text}');
    """

    subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-Command",
            command
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )