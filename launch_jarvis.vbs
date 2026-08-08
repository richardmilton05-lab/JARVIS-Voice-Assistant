Set shell = CreateObject("WScript.Shell")

shell.CurrentDirectory = "C:\Jarvis"

shell.Run """C:\Espressif\tools\python\python.exe"" ""C:\Jarvis\main.py""", 0, False