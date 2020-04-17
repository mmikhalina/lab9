import numpy as np
from random import randint
import timeit

def bubble1(a):  #создание сортировки bubble в порядке роста
    obmen = 0
    sravnenie = 0
    elo = len(a)
    for i in range(1, elo):
        for j in range(elo - 1, i - 1, -1):
            sravnenie += 1
            if (a[j - 1] > a[j]):
                a[j], a[j - 1] = a[j - 1], a[j]
                obmen += 1
    return sravnenie,obmen
def bubble2(a):  #создание сортировки bubble в порядке спадания
    obmen = 0
    sravnenie = 0
    elo = len(a)
    for i in range(1, elo):
        for j in range(elo - 1, i - 1, -1):
            sravnenie += 1
            if (a[j - 1] < a[j]):
                a[j], a[j - 1] = a[j - 1], a[j]
                obmen += 1
    return sravnenie, obmen
def selection1(a):  #создание сортировки selection в порядке роста
    obmen = 0
    sravnenie = 0
    elo = len(a)
    for i in range(elo - 1):
        min = i
        for j in range(i + 1, elo):
            sravnenie += 1
            if a[j] < a[min]:
                min = j
        obmen += 1
        a[i], a[min] = a[min], a[i]
    return sravnenie, obmen
def selection2(a):  #создание сортировки selection в порядке спадания
    obmen = 0
    sravnenie = 0
    elo = len(a)
    for i in range(elo - 1):
        min = i
        for j in range(i + 1, elo):
            sravnenie += 1
            if a[j] < a[min]:
                min = j
        obmen += 1
        a[i], a[min] = a[min], a[i]
    return sravnenie, obmen
def insertion(a):  #создание сортировки insertion в порядке роста
    obmen = 0
    sravnenie = 0
    elo = len(a)
    for i in range(1, elo):
        j = i - 1
        key = a[i]
        sravnenie += 1
        while j >= 0 and a[j] > key:
            obmen += 1
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return sravnenie, obmen
def insertion2(a):  #создание сортировки insertion в порядке спадания
    obmen = 0
    sravnenie = 0
    elo = len(a)
    for i in range(1, elo):
        sravnenie += 1
        j = i - 1
        key = a[i]
        while j >= 0 and a[j] < key:
            obmen += 1
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return sravnenie, obmen

while True:
    while True:  #создание масива и выбор
        try:
            flag = input("Если вы хотите использовать рандомные значения - нажмите 1")
            if flag == '1':
                a = np.random.randint(-10000, 10000, 100000)
            else:
                n = int(input('Если длинна массива от 1 до 30, то программа не запустится: '))
                a = np.zeros(0, dtype = int)
                if n <= 30:
                    a = np.zeros(n, dtype = int)
                    for i in range(n):
                        a[i] = randint(-100, 100)
                    print(f'Ваш масив{a}')

                else:
                    print('Вы превысили лимит')
                    break
            break

        except ValueError:
            print("Введите целое число!")
    len_arr = len(a)
    if 1 <= len_arr <= 30 or len_arr == 100000:
        check = int(input('Выберите вид сортировки:\n1)Buble\n2)Selection\n3)Insertion'))  # вибір яке сортування застосувати
        if check == 1:
            order = int(input('Выберите порядок \n1)Порядок роста\n2)Порядок спадания'))
            if order == 1:
                sravnenie, obmen = bubble1(a)
                type = 'Buble.Increasing'
            elif order == 2:
                sravnenie, obmen = bubble2(a)
                type = 'Buble decreasing'
        elif check == 2:
            order = int(input('Выберите вид сортировки \n1)Increasing\n2)Decreasing'))
            if order == 1:
                sravnenie, obmen = selection1(a)
                type = 'Selection increasing'
            elif order == 2:
                sravnenie, obmen = selection2(a)
                type = 'Selection decreasing'
        elif check == 3:
            order = int(input('Выберите вид сортировки \n1)Increasing\n2)Decreasing'))
            if order == 1:
                sravnenie, obmen = insertion(a)
                type = 'Insertion increasing'
            elif order == 2:
                sravnenie, obmen = insertion2(a)
                type = 'Insertion decreasing'

        print(f'Отсортированный масив: \n {a}')  #вывод всех данных
        print(type)
        print(f'Сравнения были выполнены {sravnenie} раз')
        print(f'Обменов было совершено {obmen}')
        t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
        print(f'Программа проработала {t} секунд')
        result = input('Если вы хотите перезапустить программу - нажмите 1, если нет, нажмите любую другую кнопку.')
        if result == '1':
            continue
        else:
            break