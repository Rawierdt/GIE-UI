import os
import random
from playsound import playsound
import customtkinter
from PIL import Image
from crypt_utl import encrypt_file, decrypt_file, encrypt_directory, decrypt_directory
from passwd_utl import verify_password
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkFrame, CTkImage
import tkinter.filedialog, messagebox
from version import VERSION, NAME, AUTHOR, DESCRIPTION


print(f"Name: {NAME}")
print(f"Version: {VERSION}")
print(f"Autor: {AUTHOR}")
print(f"Description: {DESCRIPTION}")


app = CTk()
app.geometry("900x330")
app.title(" ")
app.resizable(0, 0)
customtkinter.set_appearance_mode("system")
customtkinter.deactivate_automatic_dpi_awareness()
import os

# Obtener la ruta del directorio actual del script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo "1.png" dentro del directorio "img"
image1_path = os.path.join(current_directory, "img", "1.png")
side_img_data1 = Image.open(image1_path)

# Construir la ruta al archivo "1d.png" dentro del directorio "img"
image2_path = os.path.join(current_directory, "img", "1d.png")
side_img_data2 = Image.open(image2_path)

# Construir las rutas a los archivos de audio dentro del directorio "audio"
audio_files = [
    os.path.join(current_directory, "audio", "audio1.mp3"),
    os.path.join(current_directory, "audio", "audio2.mp3"),
    os.path.join(current_directory, "audio", "audio3.mp3")
]

# Crear la instancia de CTkImage con ambas imágenes
side_img = CTkImage(dark_image=side_img_data2, light_image=side_img_data1, size=(135, 330))

# Usar la instancia de CTkImage en un CTkLabel
CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

CTkLabel(master=app, text="GIE", text_color="#A7ABBC", font=("Impact", 22), compound="left").pack(anchor="w", pady=(10, 0), padx=(360, 0))
CTkLabel(master=app, text="Encrypt and Decrypt Your Files Easily", text_color="#A7ABBC", font=("Helvetica", 16), compound="left").pack(anchor="w", pady=(0, 0), padx=(250, 0))

# Create CTkEntry instance to interact with
CTkLabel(master=app, text="📂 File or folder path (Required):", text_color="#A7ABBC", font=("Arial", 16), compound="left").pack(anchor="w", pady=(5, 0), padx=(10, 0))

frame = CTkFrame(master=app)
frame.pack(pady=(5, 0), padx=(0, 0))  # Adjust padding as needed

file_entry = CTkEntry(master=frame, font=("Consolas", 12), width=550, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", placeholder_text="Example: C:/image.jpg or C:/image.jpg.gie")
file_entry.pack(side="left", pady=(5, 0), padx=(0, 50))  # Adjust spacing as needed


def browse_path():
    path = tkinter.filedialog.askopenfilename()  # Get selected file path
    file_entry.delete(0, 'end')  # Clear the entry
    file_entry.insert(0, path)  # Insert only the path (3 arguments)


CTkButton(master=frame, text="Browse", command=browse_path, fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=100).pack(side="left")

CTkLabel(master=app, text="🔑 Password (Required):", text_color="#A7ABBC", font=("Arial", 16), compound="left").pack(anchor="w", pady=(5, 0), padx=(10, 0))

password_entry = CTkEntry(master=app, width=280, show="*", font=("Consolas", 12), fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", placeholder_text='Cannot contain the characters $ and "')
password_entry.pack(anchor="w", pady=(5, 0), padx=(30, 0))  # Place it below the password label


def encrypt(file_entry, password_entry):
    path = file_entry.get()
    password = password_entry.get()  # Obtener la contraseña como una cadena
    if not path or not password:
        messagebox.showerror("Error", "Por favor, ingrese una ruta y contraseña válidas.")
        return
    if os.path.exists(path):
        if os.path.isdir(path):
            encrypt_directory(path, password)  # Pasar la contraseña como cadena
        else:
            encrypt_file(path, password)  # Pasar la contraseña como cadena
        messagebox.showinfo("Éxito", "¡Encriptado exitosamente!")
    else:
        messagebox.showerror("Error", "La ruta especificada no existe.")


frame2 = CTkFrame(master=app)
frame2.pack(pady=(5, 0), padx=(0, 0))  # Adjust padding as needed


def change_theme():
    random_audio_file = random.choice(audio_files)
    playsound(random_audio_file)
    if customtkinter.get_appearance_mode() == "light":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")


CTkButton(master=frame2, text="Uwu", command=change_theme, fg_color="#09E60D", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=105).pack(side="left", pady=(40, 0), padx=(25, 10))


CTkButton(master=frame2, text="Encrypt", command=lambda: encrypt(file_entry, password_entry), fg_color="#6801E8", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(side="left", pady=(40, 0), padx=(25, 10))  # Adjust padding as needed


def decrypt(file_entry, password_entry):
    path = file_entry.get()
    password = password_entry.get()  # Get password as a string
    if not path or not password:
        messagebox.showerror("Error", "Por favor, ingrese una ruta y contraseña válidas.")
        return
    if os.path.exists(path):
        if os.path.isdir(path):
            decrypt_directory(path, password.encode())  # Pass password as bytes
        else:
            decrypt_file(path, password.encode())  # Pass password as bytes
        messagebox.showinfo("Éxito", "¡Desencriptado exitosamente!")
    else:
        messagebox.showerror("Error", "La ruta especificada no existe.")


CTkButton(master=frame2, text="Decrypt", command=lambda: decrypt(file_entry, password_entry), fg_color="#0C36E1", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(side="left", pady=(40, 0), padx=(10, 10))


def clear_fields():
    file_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


CTkButton(master=frame2, text="Clear", command=clear_fields, fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=105).pack(side="left", pady=(40, 0), padx=(10, 25))

CTkLabel(master=app, text="V1.40 Copyright © 2024 Rawier 𝕽♕.", text_color="#A7ABBC", font=("Arial", 12), compound="left").pack(anchor="w", pady=(20, 0), padx=(290, 0))


def main():
    app.mainloop()


if __name__ == "__main__":
    main()
