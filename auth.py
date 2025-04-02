__all__ = ['create_account', 'login']

# auth.py

from utils import hash_password
from data_handler import read_users, write_users
from logs import log_event, log_error

def create_account(username, password):
    users = read_users()

    for user in users:
        if user[0] == username:
            log_error(f"Qeydiyyat zamanı istifadəçi adı təkrarlandı: {username}")
            return False

    hashed_pw = hash_password(password)
    users.append([username, hashed_pw, "0.0"])
    write_users(users)
    log_event(f"Yeni istifadəçi yaradıldı: {username}")
    return True

def login(username, password):
    users = read_users()
    hashed_pw = hash_password(password)

    for user in users:
        if user[0] == username and user[1] == hashed_pw:
            log_event(f"Uğurlu giriş: {username}")
            return True
    log_error(f"Uğursuz giriş cəhdi: {username}")
    return False
print("auth.py modulu yükləndi")
