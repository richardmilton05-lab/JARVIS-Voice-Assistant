import os
import subprocess
import webbrowser
from urllib.parse import quote_plus


# ==========================================
# Windows Applications
# ==========================================

APPS = {
    "calculator": "calc.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",

    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    "vs code": r"C:\Users\Richard\AppData\Local\Programs\Microsoft VS Code\Code.exe",

    "whatsapp": "shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"
}


# ==========================================
# Open Windows Application
# ==========================================

def open_app(app_name):

    app_name = app_name.lower().strip()

    if app_name not in APPS:
        return False

    app = APPS[app_name]

    try:

        if app.startswith("shell:"):

            os.system(f'start "" "{app}"')

        else:

            subprocess.Popen(app)

        return True

    except Exception as e:

        print(f"Application error: {e}")

        return False


# ==========================================
# Websites
# ==========================================

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "gmail": "https://mail.google.com",
    "linkedin": "https://www.linkedin.com"
}


# ==========================================
# Open Website
# ==========================================

def open_website(name):

    name = name.lower().strip()

    if name not in WEBSITES:
        return False

    try:

        webbrowser.open(WEBSITES[name])

        return True

    except Exception as e:

        print(f"Website error: {e}")

        return False


# ==========================================
# Google Search
# ==========================================

def google_search(query):

    query = query.strip()

    if not query:
        return False

    url = (
        "https://www.google.com/search?q="
        + quote_plus(query)
    )

    webbrowser.open(url)

    return True


# ==========================================
# YouTube Search
# ==========================================

def youtube_search(query):

    query = query.strip()

    if not query:
        return False

    url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(query)
    )

    webbrowser.open(url)

    return True


# ==========================================
# ChatGPT Search
# ==========================================

def search_chatgpt(query):

    query = query.strip()

    if not query:
        return False

    url = (
        "https://chatgpt.com/?q="
        + quote_plus(query)
    )

    webbrowser.open(url)

    return True


# ==========================================
# GitHub Search
# ==========================================

def github_search(query):

    query = query.strip()

    if not query:
        return False

    url = (
        "https://github.com/search?q="
        + quote_plus(query)
    )

    webbrowser.open(url)

    return True


# ==========================================
# Create JARVIS Desktop Folder
# ==========================================

def create_desktop_folder(folder_name="JARVIS"):

    desktop = os.path.join(
        os.path.expanduser("~"),
        "Desktop"
    )

    folder_path = os.path.join(
        desktop,
        folder_name
    )

    try:

        os.makedirs(
            folder_path,
            exist_ok=True
        )

        return folder_path

    except Exception as e:

        print(f"Folder creation error: {e}")

        return None