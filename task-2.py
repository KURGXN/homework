import random
print('Задача 2 - Магазин')

original_prices = [random.randint(-10, 10) for _ in range(10)]
new_prices = [number for number in original_prices if number > 0]

print(f'\nСписок старых цен: {original_prices}')
print(f'\nСписок актуальных цен: {new_prices}')
