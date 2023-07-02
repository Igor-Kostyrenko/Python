import random
import string

def generate_password(length):
    # Створюємо набір символів для генерації пароля
    password_characters = string.ascii_letters + string.digits + string.punctuation

    # Перевіряємо, чи містить пароль потрібні символи
    while True:
        password = random.choices(password_characters, k=length)
        if (
            any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)
        ):
            return ''.join(password)

def main():
    print("Ласкаво просимо до генератора паролів користувачів Linux!\n")
    length = int(input("Будь ласка, введіть бажану довжину пароля: "))

    password = generate_password(length)
    print("\nЗгенерований пароль:", password)

if __name__ == "__main__":
    main()