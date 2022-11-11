def party():
    while True:
        print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
        action = input('Гость пришёл или ушёл? ')
        if action == 'Пора спать':
            return
        elif action != 'пришёл' and action != 'ушёл':
            party()
        guest_name = input('Имя гостя: ')
        if action == 'пришёл' and len(guests) != 6:
            print(f'Привет, {guest_name}!')
            guests.append(guest_name)
        elif action == 'пришёл' and len(guests) == 6:
            print(f'Прости, {guest_name}, но мест нет.')
        elif action == 'ушёл':
            print(f'Пока, {guest_name}!')
            guests.remove(guest_name)


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

party()

print('\nВечеринка закончилась, все легли спать.')
