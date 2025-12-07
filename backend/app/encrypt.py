from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encryptMessage(message: str, key: bytes) -> tuple[bytes, bytes]:
    """Encrypt a message using AES-256-CBC."""

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv, ciphertext


def decryptMessage(iv: bytes, ciphertext: bytes, key: bytes) -> str:
    """Decrypt a message using AES-256-CBC."""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data.decode()
