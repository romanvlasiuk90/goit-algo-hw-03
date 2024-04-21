import datetime

def get_days_from_today(date):
    # Обробка вірного формату
    try:
        # Метод strftime представляє введену дату відліку у datetime
        target_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        # Визначаємо дату сьогодні
        today = datetime.datetime.today()
        print(f">>> Сьогодні: ⮕  {today.strftime('%Y-%m-%d')}")
        # Калькулюємо різницю і повертаємо у днях
        delta = today - target_date
        return print(f">>> Різниця днів між {target_date.strftime('%Y-%m-%d')} та Сьогодні: ⮕  {delta.days}")
    # Обробка помилкового формату значення параметру count_date
    except ValueError:
        return print(f"Неправильний формат дати, потрібен: YYYY-MM-DD")

count_date = input(">>> Введіть дату відліку YYYY-MM-DD ⮕  ")

get_days_from_today(count_date)