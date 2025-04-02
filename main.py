# main.py

from auth import create_account, login
from bank import get_balance, deposit, withdraw

print("🔐 Xoş gəlmisiniz - Sadə Bank Sisteminə!")

current_user = None

while True:
    if not current_user:
        print("\n1. Qeydiyyat")
        print("2. Daxil ol")
        print("3. Çıxış")
        secim = input("Seçiminizi daxil edin: ")

        if secim == "1":
            username = input("İstifadəçi adı: ")
            password = input("Şifrə: ")
            if create_account(username, password):
                print("✅ Qeydiyyat uğurludur!")
            else:
                print("❌ Bu istifadəçi artıq mövcuddur.")

        elif secim == "2":
            username = input("İstifadəçi adı: ")
            password = input("Şifrə: ")
            if login(username, password):
                print(f"🔓 Uğurla daxil oldunuz: {username}")
                current_user = username
            else:
                print("❌ İstifadəçi adı və ya şifrə yalnışdır.")

        elif secim == "3":
            print("👋 Çıxış edilir...")
            break

        else:
            print("⚠️ Yanlış seçim!")

    else:
        print(f"\n🏦 {current_user} istifadəçisi üçün əməliyyatlar:")
        print("1. Balansı yoxla")
        print("2. Pul yatır")
        print("3. Pul çıxart")
        print("4. Hesabdan çıxış")

        icra = input("Seçiminizi daxil edin: ")

        if icra == "1":
            balance = get_balance(current_user)
            print(f"💰 Cari balans: {balance:.2f} AZN")

        elif icra == "2":
            try:
                amount = float(input("Yatırılacaq məbləğ: "))
                if deposit(current_user, amount):
                    print("✅ Pul yatırıldı.")
                else:
                    print("❌ Pul yatırmaq mümkün olmadı.")
            except ValueError:
                print("⚠️ Yalnış məbləğ!")

        elif icra == "3":
            try:
                amount = float(input("Çıxarılacaq məbləğ: "))
                if withdraw(current_user, amount):
                    print("✅ Pul çıxarıldı.")
                else:
                    print("❌ Əməliyyat mümkün olmadı.")
            except ValueError:
                print("⚠️ Yalnış məbləğ!")

        elif icra == "4":
            print(f"🔒 {current_user} istifadəçisi çıxış etdi.")
            current_user = None

        else:
            print("⚠️ Yanlış seçim!")
