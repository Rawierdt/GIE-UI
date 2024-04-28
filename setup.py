import os
import platform
import sys

try:
    if platform.system() == "Windows":
        os.system("python -m pip install colorama")
        os.system("python -m pip install customtkinter")
        os.system("python -m pip install --upgrade --force-reinstall cryptography")
        os.system("python -m pip install pillow")
        os.system("python -m pip install tkinter")
        os.system("cls")
    else:  # Linux, macOS, etc.
        os.system("python3 -m pip install colorama")
        os.system("python3 -m pip install customtkinter")
        os.system("python3 -m pip pip install --upgrade --force-reinstall cryptography")
        os.system("python3 -m pip install pillow")
        os.system("python3 -m pip install tkinter")
        os.system("clear")

    print("Installed Successfully !!!")
    python_command = "python3" if sys.platform != "win32" else "python"
    os.system(f"{python_command} anayansi.py")
except Exception as error:
    print(f"\n{error}\nError Encountered...")
