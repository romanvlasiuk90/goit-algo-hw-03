import datetime

def get_upcoming_birthdays(users):
    # Визначте поточну дату системи за допомогою datetime.today().date().
    today = datetime.datetime.today().date()
    # Список для зберігання інформації про привітання
    upcoming_birthdays = []
    # Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
    for user in users:
        # Конвертуйте дату народження із рядка у datetime об'єкт - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). 
        # Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Визначення дати наступного дня народження
        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        # Перевірка, чи день народження припадає на вихідний
        while next_birthday.weekday() >= 5:  # 5 і 6 - субота і неділя
            next_birthday += datetime.timedelta(days=1)  # Переносимо наступний день на понеділок
        # Якщо наступне день народження у поточному тижні, додаємо до списку привітань
        if (next_birthday - today).days <= 7 and (next_birthday - today).days >= 1 :
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": next_birthday.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.04.23"},
    {"name": "Jane Smith", "birthday": "1990.04.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)