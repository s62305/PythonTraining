#coding=utf-8

import requests

HOST = 'http://sputnik.ru'

# Использование параметров по умолчанию
def is_connected(host, t=0.02):
    try:
        r = requests.get(host, timeout=t)
    	if r.status_code == 200:
        	return True
    except:
        return False

# Вызываем функцию с использованием параметра по умолчанию
print is_connected(HOST)
# Вызываем функцию, передавая параметр явно
print is_connected(HOST, 10)

# Именованные параметры идут всегда после неименованных
def func1(a, b, c, d=10, e=14):
    return float(a + b + c + d)/e

# Примеры вызова функции
print(func1(1, 1, 3))
print(func1(1, 1, 3, e=86, d=10))


v = range(37)

# Обработка произвольного числа неименованных аргументов в функцию
def print_every(*a):
    print type(a)
    for element in a:
        print element


print_every(1, 2, 3, 4, 5, 6)
# Вызов функции с распаковкой
print_every(*v)

# Передача произвольного числа именованных аргументов в функцию
def func2(**kw):
    print type(kw)
    for k, v in kw.items():
        print "{}:{}".format(k, v)

# Вызов функции, принимающей произвольное число именованных аргументов
func2(a=1, b=3, c=20)

d = dict(a=1, b=3, c=20)
# Вызов с распаковкой
func2(**d)


# Обычно функцию определяют как-то так
def feefnsdf(par1, par2, *args, **kwargs):
    pass


# Лямбда-функция
f = lambda x: x * x

print f
print type(f)
print f(3, 3)

a = [(1, 2), (2, 30), (5, 18), (45, 0), (-1, 0.3)]


# Пример применения лямбда функции
print sorted(a)
print sorted(a, key=lambda x: x[1])

list = [10, 4, 2, -1, 6]

y = 5
print filter(lambda x: x < y, list)

list_of_word = ['1', '2', '3', '4']

print map(int, list_of_word)

new_list = [int(x) for x in list_of_word]


# Глобальные переменные

b = 10

def func(a):
    b = a + 1

func(3)
print b


def func(a):
	# Объявляем глобальную переменную внутри функции
	global b
	b = a + 1


func(3)
print b