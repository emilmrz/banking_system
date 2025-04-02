# utils.py

import hashlib

def hash_password(password):
    """
    Verilən şifrəni SHA-256 ilə hash-ləyir və string şəklində qaytarır.
    """
    return hashlib.sha256(password.encode()).hexdigest()
