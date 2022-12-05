def is_number_russian(text):
    if text.startswith('8-916'):
        print('Этот номер российский')
        return
    print('Этот номер не российский')


phone_number = '8-916-123-45-67'

is_number_russian(phone_number)
