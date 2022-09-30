print('Задача 3. Контроль')


def employee_finder():
    global employees
    need_id = int(input('\nКакой ID ищем? '))
    for employee in employees:
        if employee == need_id:
            print('Сотрудник на месте!')
            return
    print('Сотрудник не работает!')


employees = []
employees_count = int(input('\nКол-во сотрудников в офисе: '))
if employees_count < 5:
    print('Похоже сегодня день отдыха) Даже пяти не набралось\n')

for _ in range(employees_count):
    ID = int(input('ID сотрудника: '))
    employees.append(ID)

employee_finder()
