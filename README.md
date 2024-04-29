![imageTitle](img/title.png)

[![Static Badge](https://img.shields.io/badge/%20build-MIT-brightgreen?logo=github&label=LICENSE)]([https://github.com/Rawierdt/GIE-UI/LICENSE](https://github.com/Rawierdt/GIE-UI/blob/main/LICENSE))
![Static Badge](https://img.shields.io/badge/APRIL%202024-red?label=RELEASE%20DATE)
![Static Badge](https://img.shields.io/badge/LANGUAGE-Python-yellow?logo=python)
# GIE-UI

## Encrypt and Decrypt
An Encrypt and Decrypt your files easily and folders, and send it secure, written in Python with UI.


> [!CAUTION]
> Disclaimer: This tool was created for educational purposes only. I do not take any responsibility for the misuse of this tool.


![Screenshott](https://i.imgur.com/NC2A0HT.jpeg)


## Version
**GIE V1.40.1.2**

### Features
Encrypt and decrypt your files and folders with AES, for any file, jpg, png, mp4, mp3, docx, pdf, etc... 

**¡¡IMPORTANT TO READ ALL!!**

## 📦 Requirements

- **Windows 10+ (64-bit) or macOS Monterey+**

- **30 MB disk space**

- **[Python](https://www.python.org/downloads/)**

### 🦠 Antivirus advertisement
GIE has the ability to encrypt vital paths and files on your system, so it is considered a risk by the operating system. If you still decide to use it, you should create an exception to the GIE program.

- Matches rule PyInstaller from ruleset PyInstaller at [Yara-rules](https://github.com/bartblaze/Yara-rules) by @bartblaze

[Virustotal scan](https://www.virustotal.com/gui/file/49a6c879bb46ad0f357a545f6f6577bb418c7f210cac60556f45051a9473851b/detection)

[Triage](https://tria.ge/240428-bnst8acg68)

## 💻 Installation
Execute the commands according to your case

Clone or Download this Repository

```
git clone git@github.com:Rawierdt/GIE-UI.git
```

Change Directory

```
cd GIE-UI
```

Run the project

```
python main.py
```

---

## For Encrypt

To **Encrypt** a folder or file

For folders (_you must type the path as it appears in your file browser_)

![PATH](https://i.imgur.com/Lah8Ri8.png)

For only files (_one or more files_)

Only select the files to encrypt.

supports = jpg, png, mp3, mp4, docx, xlsx, sql, py, zip, etc...

**Enter a password:**

> [!IMPORTANT]  
> The password cannot contain the characters $ or "" and ''
> The password will not be visible while you type it.

When you click the Encrypt button, the operation will begin., it will start encrypting the files with the extension **".gie"** and will generate a **".GKY"** file, which is very important to decrypt your original file.

*"GKY" is the extension of the file containing the key for decryption, along with the password provided.*

! *If you want to share the file with your colleague, you will need to provide him/her with three files, the .gie, the .GKY and the password.*

**EXAMPLE**

![FileEn](https://i.imgur.com/pGLWaxL.jpeg)


## For Decrypt

To **Decrypt** a folder or file 

> [!IMPORTANT]  
> The password must be the same as the one used to encrypt the file, otherwise you will lose your file forever.

The program will search if the .GKY file exists in the path provided and will try to decrypt the file with the password, if the password does not match the file will not decrypt or will decrypt corruptly, if the GKY does not exist, the program will throw an error message and will not be able to decrypt.

It is very important to save the .GKY and the PASSWORD very well.

---

### [⬇️ Download ⬇️](https://rawierdt.github.io/GIE-UI/)

### 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to check issues page.

### ❤️ Show your support

Give a ⭐️ if this _project helped you!_ 

### 📝 License

Copyright © 2024 [Rawier](https://rawier.vercel.app). This project is [MIT](/LICENSE) licensed.

---
