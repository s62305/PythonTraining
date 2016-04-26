# coding=utf-8

"""
Написать программу, которая будет обрабатывает файл, содержащего спискок сотрудников предприятия
Файл содержит следующие поля: id сотрудника, его ФИО, дату рождения, должность, компания
Программа должна добавлять поле с электронной почтой, полученной из имени с добавлением @contora.ru
(например, Ivanov Ivan -> ivanovi@contora.ru)
Программа должна выдавать сводную информацию по сотрудникам: средний возраст, количество человек в каждом департаменте,
которая должна сохраняться в текстовый файл
"""
from pprint import pprint



def read_file(filename):
    with open(filename, 'r') as f:
        f.readline()
        return [tuple(x.strip().split(',')) for x in f.readlines()]


def get_companies(list_of_comp):
    comp_employees = {}
    for id, name, date, comp in list_of_comp:
        if comp in comp_employees:
            comp_employees[comp] += 1
        else:
            comp_employees[comp] = 1
    return comp_employees


companies = read_file('data.csv')
print companies[:10]
# pprint(get_companies(companies))
#c = get_companies(companies)

#pprint(max(c,key=lambda k: c[k]))


def form_email(name):
    splitted = name.split(' ')
    first_name = splitted[0][0]
    second_name = splitted[1]
    return (second_name + first_name + '@sputnik.ru').lower()

def create_new_data(l):
    return [(id, name, date, comp, form_email(name)) for id, name, date, comp in l]

with_email = create_new_data(companies)


def write_to_file(filename, ccc):
    with open(filename, 'w') as f:
        f.writelines('id,name,birthday,comp,email\n')
        for el in ccc:
            f.writelines(",".join(list(el)) + '\n')


write_to_file('new_data.csv', with_email)