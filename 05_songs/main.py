violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]]

songs_count = int(input('\nСколько песен выбрать? '))
final_time = 0

for song_number in range(songs_count):
    song_name = input(f'Название {song_number + 1}-й песни: ')
    for number in range(len(violator_songs)):
        if violator_songs[number][0] == song_name:
            final_time += violator_songs[number][1]

print('\nОбщее время звучания песен:', round(final_time, 2), 'минуты')
