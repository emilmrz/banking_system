from constants import USERS_FILE

def read_users():
    """
    users.txt faylını oxuyur və istifadəçi məlumatlarını siyahı şəklində qaytarır.
    """
    try:
        with open(USERS_FILE, "r") as f:
            lines = f.readlines()
        return [line.strip().split(",") for line in lines]
    except FileNotFoundError:
        return []

def write_users(users):
    """
    Verilmiş istifadəçi məlumatlarını users.txt faylına yazır.
    users: [['ali', 'hashed_password', '100.0'], ...]
    """
    with open(USERS_FILE, "w") as f:
        for user in users:
            f.write(",".join(user) + "\n")
