# bank.py

from data_handler import read_users, write_users
from logs import log_event, log_error

def get_balance(username):
    """
    Verilmiş istifadəçinin balansını qaytarır.
    """
    users = read_users()
    for user in users:
        if user[0] == username:
            return float(user[2])
    log_error(f"Balans oxunmadı: {username}")
    return None

def deposit(username, amount):
    """
    Verilmiş istifadəçiyə pul əlavə edir.
    """
    if amount <= 0:
        log_error(f"Yalnış məbləğlə yatırma cəhdi: {amount}")
        return False

    users = read_users()
    for user in users:
        if user[0] == username:
            user[2] = str(float(user[2]) + amount)
            write_users(users)
            log_event(f"{username} istifadəçisi {amount} AZN yatırdı")
            return True

    log_error(f"Yatırma zamanı istifadəçi tapılmadı: {username}")
    return False

def withdraw(username, amount):
    """
    Verilmiş istifadəçidən balans kifayətdirsə, pul çıxarır.
    """
    if amount <= 0:
        log_error(f"Yalnış məbləğlə çıxarma cəhdi: {amount}")
        return False

    users = read_users()
    for user in users:
        if user[0] == username:
            current_balance = float(user[2])
            if current_balance >= amount:
                user[2] = str(current_balance - amount)
                write_users(users)
                log_event(f"{username} istifadəçisi {amount} AZN çıxartdı")
                return True
            else:
                log_error(f"{username} kifayət qədər balans yoxdur ({current_balance} < {amount})")
                return False

    log_error(f"Çıxarma zamanı istifadəçi tapılmadı: {username}")
    return False
