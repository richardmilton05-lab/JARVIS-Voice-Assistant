from assistant.listener import listen
from assistant.speech import speak
from assistant.brain import process
from assistant.automation import create_desktop_folder


# ==========================================
# CREATE DESKTOP FOLDER
# ==========================================

create_desktop_folder("JARVIS")


# ==========================================
# JARVIS SETTINGS
# ==========================================

WAKE_PHRASES = [
    "launch"
]

LOCK_PHRASES = [
    "lock jarvis",
    "go to sleep",
    "sleep jarvis"
]


# ==========================================
# Check Wake Phrase
# ==========================================

def is_wake_command(command):

    command = command.lower().strip()

    for phrase in WAKE_PHRASES:

        if phrase in command:

            return True

    return False


# ==========================================
# Check Lock Phrase
# ==========================================

def is_lock_command(command):

    command = command.lower().strip()

    for phrase in LOCK_PHRASES:

        if phrase in command:

            return True

    return False


# ==========================================
# JARVIS
# ==========================================

print()
print("========================================")
print("             JARVIS AI")
print("========================================")
print()

speak("Jarvis is online.")

print()
print("🔒 Jarvis is locked.")
print("Say 'Launch jarvis' to activate.")
print()


# ==========================================
# Main Loop
# ==========================================

running = True

unlocked = False


while running:

    # ======================================
    # LOCKED MODE
    # ======================================

    if not unlocked:

        command = listen()

        if command == "":
            continue

        if is_wake_command(command):

            unlocked = True

            speak("I'm listening.")

            print()
            print("🔓 Jarvis unlocked.")
            print()

        continue


    # ======================================
    # UNLOCKED MODE
    # ======================================

    command = listen()

    if command == "":
        continue


    # ======================================
    # LOCK COMMAND
    # ======================================

    if is_lock_command(command):

        speak("Locking Jarvis.")

        unlocked = False

        print()
        print("🔒 Jarvis locked.")
        print("Say 'Launch jarvis' to activate.")
        print()

        continue


    # ======================================
    # NORMAL COMMAND
    # ======================================

    running = process(command)


print()
print("Jarvis has shut down.")