print('Задача 4. Видеокарты')

gpu_count = int(input('\nКоличество видеокарт: '))
gpu_list = []
new_gpu_list = []

for place in range(gpu_count):
    gpu = int(input(f'{place + 1} Видеокарта: '))
    gpu_list.append(gpu)

for gpu in gpu_list:
    if gpu != max(gpu_list):
        new_gpu_list.append(gpu)

print('\nСтарый список видеокарт:', gpu_list)
print('Новый список видеокарт:', new_gpu_list)
