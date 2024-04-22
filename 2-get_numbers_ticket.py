import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка валідності вхідних даних
    if min >= 1 and max <= 1000 and max > min and quantity > 0 and quantity <= (max-min+1):
        # Оголошуємо множину і наповнюємо по к-сті чисел лотереї
        numbers_set = set()
        while len(numbers_set) < quantity:
            # Додаємо рандомні числа у множину
            numbers_set.add(random.randint(min, max))
        # Відсортовуємо + вивід
        return print(f"Ваші лотерейні числа: {sorted(numbers_set)}")
    else:
        return print(f"Помилка вводу умови лотереї")

# Умова Лотереії - Min , Max, Quantity
lottery_numbers = get_numbers_ticket(1, 36, 5)