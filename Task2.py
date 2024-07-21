import re
from typing import Callable

def generator_numbers(text: str):
    numbers = r'\b\d+(\.\d+)?\b'    # Регулярний вираз для пошуку дійсних чисел у тексті
    results = re.finditer(numbers, text)     # Знаходження всіх чисел у тексті за допомогою регулярного виразу
    for result in results:
        yield float(result.group()) # Перетворення знайденого числа на float і повернення його як частини генератора

def sum_profit(text: str, func: Callable):
    return sum(func(text))  # Виклик функції, яка повертає генератор чисел, і підсумовування всіх чисел

# Приклад використання:
# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")