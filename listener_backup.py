import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone(device_index=1) as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("I couldn't understand.")
        return ""

    except sr.RequestError:
        print("No internet connection.")
        return ""