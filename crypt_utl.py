import hashlib
import os
from passwd_utl import generate_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from colorama import Fore, Style


def encrypt_file(input_file: str, password: str):
    password_bytes = password.encode()  # Convertir la contraseña a bytes

    key_with_salt = generate_key(input_file, password_bytes)  # Generar la clave utilizando bytes
    if key_with_salt is None:
        print(Fore.RED + "No se pudo generar la clave." + Style.RESET_ALL)
        return

    key = key_with_salt[16:]  # Obtener la clave sin la sal

    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_file, "rb") as file_in:
        data = file_in.read()

    padded_data = data + b'\x00' * (-len(data) % 16)
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    output_file = input_file + ".gie"
    with open(output_file, "wb") as file_out:
        file_out.write(iv)
        file_out.write(encrypted_data)

    print(Fore.LIGHTMAGENTA_EX + f"Archivo ENCRIPTADO guardado como: {output_file}" + Style.RESET_ALL)
    os.remove(input_file)


def decrypt_file(input_file: str, password: bytes):
    base_file = os.path.splitext(os.path.basename(input_file))[0]  # Remove all extensions
    while "." in base_file:
        base_file = os.path.splitext(base_file)[0]  # Remove all extensions
    # Add the .key extension to the base file name
    key_file = os.path.join(os.path.dirname(input_file), base_file + ".GKY")
    key_file = os.path.normpath(key_file)  # Normalize the path

    print(f"Buscando el archivo de la clave: {key_file}")  # Print the name of the key file we are looking for
    if os.path.exists(key_file):
        with open(key_file, "rb") as f:
            key_with_salt = f.read()
            salt = key_with_salt[:16]  # Get the stored salt
            derived_key = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, 32)

        with open(input_file, "rb") as file_in:
            iv = file_in.read(16)
            encrypted_data = file_in.read()

        cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadded_data = decrypted_data.rstrip(b'\\x00')

        output_file = os.path.splitext(input_file)[0]
        with open(output_file, "wb") as file_out:
            file_out.write(unpadded_data)

        print(Fore.LIGHTCYAN_EX + f"Archivo DESENCRIPTADO guardado como: {output_file}" + Style.RESET_ALL)
        os.remove(input_file)

        # Delete the key file after successful decryption
        os.remove(key_file)

    else:
        print(Fore.LIGHTRED_EX + "No se encontró la clave." + Style.RESET_ALL)


def encrypt_directory(directory: str, password: str):
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            encrypt_file(filepath, password)


def decrypt_directory(directory: str, password: str):
    if not os.path.exists(directory):
        print(Fore.LIGHTRED_EX + "La carpeta especificada no existe." + Style.RESET_ALL)
        return

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".gie"):  # Solo desencriptar archivos .gie
                filepath = os.path.join(root, file)
                decrypt_file(filepath, password)
