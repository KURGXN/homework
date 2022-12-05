import random
print('Задача 3 - Squades')

first_squad = [random.randint(50, 80) for _ in range(10)]
second_squad = [random.randint(50, 80) for _ in range(10)]
third_squad = [(1 if first_squad[i_damage] > second_squad[i_damage]
                else 2)
               for i_damage in range(10)]

print('\nУрон первого отряда:', first_squad)
print('Урон второго отряда:', second_squad)
print(third_squad)
