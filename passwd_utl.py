import os
import hashlib
from colorama import Fore, Style

KEY_FILE = ".GKY"


def is_valid_password(password: str) -> bool:
    min_length = 8
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special_char = any(c in "!@#%^&*/()-¡?^[a-z][-a-z0-9._]*$" for c in password)
    return len(password) >= min_length and has_uppercase and has_lowercase and has_digit and has_special_char


def generate_key(input_file: str, password: bytes) -> bytes:
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, 32)
    key_with_salt = salt + key

    base_file = os.path.splitext(input_file)[0]  # Remove the .gie extension
    key_file_path = base_file + KEY_FILE
    with open(key_file_path, "wb") as key_file:
        key_file.write(key_with_salt)

    print(".GKY generated successfully.")

    return key_with_salt


def get_key(input_file: str, password: bytes) -> bytes:
    base_file = os.path.splitext(os.path.basename(input_file))[0]  # Remove all extensions
    key_file = os.path.join(os.path.dirname(input_file), base_file + KEY_FILE)
    print(f"Buscando el archivo de la clave: {key_file}")  # Print the name of the key file we are looking for
    if os.path.exists(key_file):
        with open(key_file, "rb") as f:
            key_with_salt = f.read()
            salt = key_with_salt[:16]  # Get the stored salt
            derived_key = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, 32)
            return derived_key  # Return the full key
    print(Fore.RED + "No se encontró la clave." + Style.RESET_ALL)
    return b''


def verify_password(input_file: str, password: bytes) -> bool:
    base_file = os.path.splitext(os.path.basename(input_file))[0]
    key_file = os.path.join(os.path.dirname(input_file), base_file + KEY_FILE)
    print("Ruta del archivo de clave:", key_file)
    if not os.path.exists(key_file):
        print("¡El archivo de clave no existe!")
        return False
    with open(key_file, "rb") as f:
        key_with_salt = f.read()
        salt = key_with_salt[:16]
        stored_key = key_with_salt[16:]
        derived_key = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, 32)
        print("Contraseña almacenada:", stored_key)
        print("Contraseña derivada:", derived_key)
        return stored_key == derived_key

