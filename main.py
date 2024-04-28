import messagebox
import os
import tkinter.filedialog
import customtkinter
from PIL import Image
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkFrame, CTkImage
from crypt_utl import encrypt_file, decrypt_file, encrypt_directory, decrypt_directory
from version import VERSION, NAME, AUTHOR, DESCRIPTION

print(f"Name: {NAME}")
print(f"Version: {VERSION}")
print(f"Autor: {AUTHOR}")
print(f"Description: {DESCRIPTION}")

# Init the customtkinter app
app = CTk()
app.geometry("900x330")
app.title(" ")
app.resizable(0, 0)
customtkinter.set_appearance_mode("system")
customtkinter.deactivate_automatic_dpi_awareness()

# Obtain the route for the script
current_directory = os.path.dirname(os.path.abspath(__file__))

image1_path = os.path.join(current_directory, "img", "1.png")
side_img_data1 = Image.open(image1_path)

image2_path = os.path.join(current_directory, "img", "1d.png")
side_img_data2 = Image.open(image2_path)

image1_path = os.path.join(current_directory, "img", "ps1.jpeg")
side_img_data3 = Image.open(image1_path)

image1_path = os.path.join(current_directory, "img", "ps2.jpeg")
side_img_data4 = Image.open(image1_path)

side_img = CTkImage(dark_image=side_img_data2, light_image=side_img_data1, size=(135, 330))
faq_img = CTkImage(dark_image=side_img_data4, light_image=side_img_data3, size=(900, 320))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

CTkLabel(master=app, text="GIE", font=("Impact", 22), compound="left").pack(anchor="w", pady=(10, 0), padx=(360, 0))
CTkLabel(master=app, text="Encrypt and Decrypt Your Files Easily", text_color="#A7ABBC", font=("Helvetica", 16),
         compound="left").pack(anchor="w", pady=(0, 0), padx=(250, 0))

CTkLabel(master=app, text="📂 File or folder path (Required):", text_color="#A7ABBC", font=("Arial", 16),
         compound="left").pack(anchor="w", pady=(5, 0), padx=(10, 0))

frame = CTkFrame(master=app, fg_color="transparent")
frame.pack(pady=(5, 0), padx=(0, 0))

file_entry = CTkEntry(master=frame, font=("Consolas", 12), width=550, fg_color="#EEEEEE", border_color="#601E88",
                      border_width=1, text_color="#000000",
                      placeholder_text="Example: C:/image.jpg or C:/image.jpg.gie")
file_entry.pack(side="left", pady=(5, 0), padx=(0, 50))


def browse_path():
    paths = tkinter.filedialog.askopenfilenames()
    file_entry.delete(0, 'end')
    file_entry.insert('end', ';'.join(paths))


CTkButton(master=frame, text="Browse", command=browse_path, fg_color="#601E88", hover_color="#E44982",
          font=("Arial Bold", 12), text_color="#ffffff", width=100).pack(side="left")

CTkLabel(master=app, text="🔑 Password (Required):", text_color="#A7ABBC", font=("Arial", 16), compound="left").pack(
    anchor="w", pady=(5, 0), padx=(10, 0))

password_entry = CTkEntry(master=app, width=280, show="*", font=("Consolas", 12), fg_color="#EEEEEE",
                          border_color="#601E88", border_width=1, text_color="#000000",
                          placeholder_text='Cannot contain the characters $ and "')
password_entry.pack(anchor="w", pady=(5, 0), padx=(30, 0))


def encrypt(file_entry, password_entry):
    answer = messagebox.askyesno("Confirmation", "Do you want to encrypt?")
    if answer:
        paths = file_entry.get().split(';')
        password = password_entry.get()
        if not paths or not password:
            messagebox.showerror("Error", "Please enter a valid path and password.")
            return
        for path in paths:
            if os.path.exists(path):
                if os.path.isdir(path):
                    encrypt_directory(path, password)
                else:
                    encrypt_file(path, password)
            else:
                messagebox.showerror("Error", "The specified path does not exist.")
        messagebox.showinfo("Success", "Successfully encrypted!")


def decrypt(file_entry, password_entry):
    paths = file_entry.get().split(';')
    password = password_entry.get()
    if not paths or not password:
        messagebox.showerror("Error", "Please enter a valid path and password.")
        return
    for path in paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                decrypt_directory(path, password.encode())
            else:
                decrypt_file(path, password.encode())
        else:
            messagebox.showerror("Error", "The route does not exist.")
    messagebox.showinfo("Success", "Successfully decrypted!")


def faq(toplevel_window=None):
    if toplevel_window is None or not toplevel_window.winfo_exists():
        toplevel_window = ToplevelWindow()  # create window if its None or destroyed
    else:
        toplevel_window.focus()


def change_theme():
    if customtkinter.get_appearance_mode() == "light":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")


def clear_fields():
    file_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


frame2 = CTkFrame(master=app, fg_color="transparent")
frame2.pack(pady=(5, 0), padx=(0, 0))


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(appfaq, *args, **kwargs):
        super().__init__(*args, **kwargs)
        appfaq.geometry("900x800")
        appfaq.title("How to use GIE")
        appfaq.resizable(0, 0)
        appfaq.state('normal')

        textbox = customtkinter.CTkTextbox(master=appfaq, width=600, height=500, corner_radius=0, fg_color="transparent",
                                           font=("Consolas", 16))
        textbox.grid(row=0, column=0, sticky="nsew")
        textbox.insert("0.0", " --------------------------- HOW TO ENCRYPT? --------------------------- \n")
        textbox.insert("2.10", "⚫ To encrypt files or directory just search for it or type the full path and then "
                               "click the 'Encrypt' button.\n")
        textbox.insert("3.0", "⚪ Administrator privileges are required to encrypt certain files properly.\n")
        textbox.insert("4.0", "⚫ You can encrypt any type of file (jpg, webp, mp4, docx, "
                              "txt, zip...), including (dll, sql, iso, and more).\n")
        textbox.insert("5.0", "⚪ If you want to encrypt a path you must write it as it appears in the file explorer. "
                              "for example 'D:/File And A'.\n")
        textbox.insert("6.0", "⚫ When encrypting, two files will be generated, one with the "
                              "extension '.gie' and the other '.GKY'.\n")
        textbox.insert("7.0", "⚪ The file with the '.gie' extension is the encrypted file and the '.GKY' is the key.\n")
        textbox.insert("8.0", "⚫ The GKY key is very important, if it is not found when "
                              "decrypting, your file will be corrupted.\n")
        textbox.insert("9.0", "⚪ The password cannot contain the characters $, ´ or ' ‘, avoid using them.\n")
        textbox.insert("10.0", "⚫ Save the GKY file and the password very well otherwise you will lose your file "
                               "forever.\n")
        textbox.insert("12.0", "⚪ GIE uses the AES-128 algorithm in CBC mode and sha256 for the password.\n")
        textbox.insert("13.0", "⚫ Use of this tool is at your own risk.\n")
        textbox.insert("14.0", " \n")
        textbox.insert("15.0", " --------------------------- HOW TO DECRYPT? --------------------------- \n")
        textbox.insert("16.0", "⚫ To decrypt you will search for the encrypted file with the extension '.gie' or the "
                               "full path.\n")
        textbox.insert("17.0", "⚪ You must enter the exact password you used to encrypt the file.\n")
        textbox.insert("18.0", "⚫ The program will look for the GKY keys associated with each file, if they are not "
                               "found it will not decrypt.\n")
        textbox.insert("19.0", "⚪ If the password is incorrect or the key is not found you may lose your file "
                               "forever.\n")
        textbox.insert("19.0", "⚫ If you have any further questions, don't forget to visit the documentation: "
                               "https://rawier.vercel.app/blog/gieui\n")
        textbox.configure(state="disabled")
        CTkLabel(master=appfaq, text="", image=faq_img).grid(row=1, column=0, sticky="wens")  # Use grid instead of pack


CTkButton(master=frame2, text="FAQ", command=faq, fg_color="#E61609", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=120).pack(side="left", pady=(40, 0), padx=(25, 10))

CTkButton(master=frame2, text="Theme", command=change_theme, fg_color="#09E60D", hover_color="#E44982",
          font=("Arial Bold", 12), text_color="#ffffff", width=120).pack(side="left", pady=(40, 0), padx=(25, 10))

CTkButton(master=frame2, text="Encrypt", command=lambda: encrypt(file_entry, password_entry), fg_color="#6801E8",
          hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=120).pack(side="left",
                                                                                                pady=(40, 0),
                                                                                                padx=(25, 10))

CTkButton(master=frame2, text="Decrypt", command=lambda: decrypt(file_entry, password_entry), fg_color="#0C36E1",
          hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=120).pack(side="left",
                                                                                                pady=(40, 0),
                                                                                                padx=(10, 10))

CTkButton(master=frame2, text="Clear", command=clear_fields, fg_color="#601E88", hover_color="#E44982",
          font=("Arial Bold", 12), text_color="#ffffff", width=120).pack(side="left", pady=(40, 0), padx=(10, 25))

CTkLabel(master=app, text="GIE V1.40.1.3 Copyright © 2024 Rawier.", text_color="#A7ABBC", font=("Arial", 12),
         compound="left").pack(anchor="w", pady=(20, 0), padx=(250, 0))


def main():
    app.mainloop()


if __name__ == "__main__":
    main()
