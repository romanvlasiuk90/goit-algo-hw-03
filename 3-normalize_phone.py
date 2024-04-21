import re

def normalize_phone(phone_number):
    # Pattern \D - видаляємо всі символи, крім цифр [^0-9]
    pattern = r"\D"
    cleaned_number = re.sub(pattern, "", phone_number)
    # Додаємо міжнародний код, якщо він відсутній
    if cleaned_number.startswith("0"):
        cleaned_number = "+38" + cleaned_number
    else:
        # Додаємо "+" на початок
        cleaned_number = cleaned_number.replace("380", "+380")
    return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)