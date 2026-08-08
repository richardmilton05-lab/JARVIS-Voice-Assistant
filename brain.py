from datetime import datetime

from assistant.speech import speak

from assistant.automation import (
    open_app,
    open_website,
    google_search,
    youtube_search,
    search_chatgpt,
    github_search
)


# ==========================================
# BASIC COMMANDS
# ==========================================

def greet():

    speak("Hello Richard.")

    return True


def status():

    speak("I am functioning normally.")

    return True


def tell_name():

    speak("My name is Jarvis.")

    return True


def tell_time():

    now = datetime.now()

    hour = now.strftime("%I").lstrip("0")
    minute = now.strftime("%M")
    period = now.strftime("%p")

    if minute == "00":

        speak(f"It is {hour} o'clock {period}.")

    else:

        speak(f"It is {hour} {minute} {period}.")

    return True


def exit_jarvis():

    speak("Goodbye Richard.")

    return False


# ==========================================
# OPEN APPLICATION
# ==========================================

def open_application(command):

    target = command.replace("open", "", 1).strip()

    if not target:

        speak("What should I open?")

        return True

    if open_app(target):

        speak(f"Opening {target}.")

    else:

        speak(f"Sorry, I couldn't find {target}.")

    return True


# ==========================================
# OPEN WEBSITE
# ==========================================

def open_site(command):

    target = command.replace("open", "", 1).strip()

    if open_website(target):

        speak(f"Opening {target}.")

    else:

        speak(f"Sorry, I don't know the website {target}.")

    return True


# ==========================================
# GOOGLE SEARCH
# ==========================================

def search_google_command(command):

    command = command.strip()

    prefixes = [
        "search google for",
        "search google",
        "google",
        "find on google",
        "look up"
    ]

    query = ""

    for prefix in prefixes:

        if command.startswith(prefix):

            query = command[len(prefix):].strip()

            break

    if query:

        speak(f"Searching Google for {query}.")

        google_search(query)

    else:

        speak("What should I search for?")

    return True


# ==========================================
# YOUTUBE SEARCH
# ==========================================

def search_youtube_command(command):

    command = command.strip()

    prefixes = [
        "search youtube for",
        "search youtube",
        "youtube",
        "find on youtube"
    ]

    query = ""

    for prefix in prefixes:

        if command.startswith(prefix):

            query = command[len(prefix):].strip()

            break

    # Handle:
    # "find STM32 tutorials on youtube"

    if not query and command.endswith("on youtube"):

        query = command[:-10].replace("find", "", 1).strip()

    if query:

        speak(f"Searching YouTube for {query}.")

        youtube_search(query)

    else:

        speak("What should I search for on YouTube?")

    return True


# ==========================================
# CHATGPT SEARCH
# ==========================================

def search_chatgpt_command(command):

    command = command.strip()

    prefixes = [
        "search chatgpt for",
        "search chatgpt",
        "ask chatgpt",
        "chatgpt"
    ]

    query = ""

    for prefix in prefixes:

        if command.startswith(prefix):

            query = command[len(prefix):].strip()

            break

    if query:

        speak(f"Opening ChatGPT for {query}.")

        search_chatgpt(query)

    else:

        speak("What should I ask ChatGPT?")

    return True


# ==========================================
# GITHUB SEARCH
# ==========================================

def search_github_command(command):

    command = command.strip()

    prefixes = [
        "search github for",
        "search github",
        "github",
        "find on github"
    ]

    query = ""

    for prefix in prefixes:

        if command.startswith(prefix):

            query = command[len(prefix):].strip()

            break

    if query:

        speak(f"Searching GitHub for {query}.")

        github_search(query)

    else:

        speak("What should I search for on GitHub?")

    return True


# ==========================================
# PROCESS COMMAND
# ==========================================

def process(command):

    command = command.lower().strip()

    if command == "":

        return True


    # --------------------------------------
    # EXIT
    # --------------------------------------

    if (
        command == "stop"
        or command == "exit"
        or command == "quit"
        or command == "goodbye"
    ):

        return exit_jarvis()


    # --------------------------------------
    # GOOGLE
    # --------------------------------------

    if (
        command.startswith("search google")
        or command.startswith("google ")
        or command.startswith("find on google")
        or command.startswith("look up ")
    ):

        return search_google_command(command)


    # --------------------------------------
    # YOUTUBE
    # --------------------------------------

    if (
        command.startswith("search youtube")
        or command.startswith("youtube ")
        or command.startswith("find on youtube")
        or command.endswith("on youtube")
    ):

        return search_youtube_command(command)


    # --------------------------------------
    # CHATGPT
    # --------------------------------------

    if (
        command.startswith("search chatgpt")
        or command.startswith("ask chatgpt")
        or command.startswith("chatgpt ")
    ):

        return search_chatgpt_command(command)


    # --------------------------------------
    # GITHUB
    # --------------------------------------

    if (
        command.startswith("search github")
        or command.startswith("github ")
        or command.startswith("find on github")
    ):

        return search_github_command(command)


    # --------------------------------------
    # OPEN WEBSITE / APPLICATION
    # --------------------------------------

    if command.startswith("open "):

        target = command.replace("open ", "", 1).strip()

        websites = [
            "google",
            "youtube",
            "github",
            "chatgpt",
            "gmail",
            "linkedin"
        ]

        if target in websites:

            return open_site(command)

        return open_application(command)


    # --------------------------------------
    # GREETINGS
    # --------------------------------------

    if command == "hello" or command.startswith("hello "):

        return greet()


    if command == "hi" or command.startswith("hi "):

        return greet()


    # --------------------------------------
    # STATUS
    # --------------------------------------

    if "how are you" in command:

        return status()


    # --------------------------------------
    # NAME
    # --------------------------------------

    if (
        "what is your name" in command
        or "what's your name" in command
    ):

        return tell_name()


    # --------------------------------------
    # TIME
    # --------------------------------------

    if (
        command == "time"
        or "what time is it" in command
        or "tell me the time" in command
        or "what is the time" in command
    ):

        return tell_time()


    # --------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------

    speak(
        "Sorry, I don't understand that command yet."
    )

    return True