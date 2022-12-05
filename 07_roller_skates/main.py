def satisfied_people_counter():
    satisfied_people = 0
    for people in range(len(foots_sizes)):
        if foots_sizes[0] <= skates_sizes[0]:
            satisfied_people += 1
            foots_sizes.remove(foots_sizes[0])
            skates_sizes.remove(skates_sizes[0])
        else:
            foots_sizes.remove(foots_sizes[0])
    return satisfied_people


def all_skates_sizes():
    skates_count = int(input('\nКол-во коньков: '))
    for pair_number in range(skates_count):
        pair_size = int(input(f'Размер {pair_number + 1}-й пары: '))
        skates_sizes.append(pair_size)
    skates_sizes.sort(reverse=True)


def all_foots_sizes():
    people_count = int(input('\nКол-во людей: '))
    for people_number in range(people_count):
        foot_size = int(input(f'Размер ноги {people_number + 1}-го человека: '))
        foots_sizes.append(foot_size)
    foots_sizes.sort(reverse=True)


skates_sizes = []
foots_sizes = []

all_skates_sizes()
all_foots_sizes()

print('\nНаибольшее кол-во людей, которые могут взять ролики:', satisfied_people_counter())
