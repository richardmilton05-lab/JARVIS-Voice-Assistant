import speech_recognition as sr


# ==========================================
# Microphone Configuration
# ==========================================

MICROPHONE_INDEX = 1

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

recognizer.pause_threshold = 0.8
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5


# ==========================================
# Listen
# ==========================================

def listen():

    with sr.Microphone(
        device_index=MICROPHONE_INDEX
    ) as source:

        print("Listening...")

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:

            return ""

    try:

        command = recognizer.recognize_google(
            audio
        )

        command = command.lower().strip()

        print(f"You: {command}")

        return command

    except sr.UnknownValueError:

        return ""

    except sr.RequestError as e:

        print(f"Speech recognition error: {e}")

        return ""