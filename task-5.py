def choose_scenario():
    scenario = int(input('1 - Содруженство'
                         '\n2 - Питт'
                         '\n3 - Столичная пустошь'
                         '\nВыберите сценарий: '))


def choose_character():
    character = int(input('\n1. Выходец из убежища'
                          '\n2. Обитель пустоши'
                          '\n3. Мутант'
                          '\n4. Баба с ломом'
                          '\n5. Боец анклава'
                          '\n\nВыберите персонажа: '))


def game_rules():
    print('-' * 84, '~~', '-' * 84)
    print(' ' * 81, 'FALLOUT')
    print(' ' * 73, 'A POST-NUCLEAR BOARD GAME')
    print('-' * 84, '~~', '-' * 84)


def start_parametrs():
    print('СТАРТОВЫЕ ПАРАМЕТРЫ:')
    print('Сценарий:')
    choose_scenario()
    # print(user_character())


game_rules()
start_parametrs()
