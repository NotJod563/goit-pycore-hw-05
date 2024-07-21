def caching_fibonacci():    # Створення основної функції
    cache = {}

    def fibonacci(n):   # Створення фун
        if n <= 0:  # Перевірка індексу числа фібоначчі на 0
            return 0
        elif n == 1: # Перевірка на 1, так як ми вже знаємо що перше число буде 1 і це дозволяє уникнути виходу за межі цілих додатніх індексів
            return 1 
        elif n in cache: # Вихід з підрахунку якщо число вже кешоване
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Рекурсивне проходження по числах Фібоначчі
        return cache[n]

    return fibonacci

fib = caching_fibonacci() # Присвоєння аргументу функції


# Приклад використання
# print(fib(10))  # Виведе 55
# print(fib(15))  # Виведе 610