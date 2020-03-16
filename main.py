# Список алгоритма действий
# Положить в массив 2 значения
#  Начат цикл игры:
#  Ждать от пользователя команды
#  Когда получим команду - обработать массив
#  Найти пустые клетки
#  Если есть пустые клетки - выбрать случайно одну из них
#  И положить туда либо 2, либо 4
#  Если пустыъ клеток нет и нельзя двигать массив - игра окончена


# Создаем приятный вывод массива, проходимся по всем строкам массива и выводим его
# Чтобы убрать скобочки квадратные и запятые - ставим * он распоковывает файл
def prety_print(mas):
    print('-' * 10)  # Распечатывает тире 10 раз
    for row in mas:
        print(*row)
    print('-' * 10)  # Если поставить это свойство прямо под print(row), то отделения будет прямо под каждой строкой, что не надо


# Создаем функцию получение номера с индекса принимает параметры i, j
def get_number_from_index(i, j):
    return i * 4 + j + 1  # Возвращаем результат этой формулы


# Напишем функцию, которая в рандомном порядке будет ставить значения либо 2, либо 4
def get_empty_list(mas):
    empty = [] # Переменная empty, которая является списком, когда найдем пустой элемент, мы в empty будем добавлять его номер
    for i in range(4):  # В пределах от 1 до 3 (строки)
        for j in range(4):  # Тоже самое для колонок
            if mas[i][j] == 0:  # Если элементы этих массивов равны 0, то печатайте эти индексы
                 num = get_number_from_index(i,j)  # сохраняем в переменную num
                 empty.append(num)
    return empty # По окончанию возвращаем этот список

# Создаем 2х мерный массив, будет 2 индекса у каждого элемента (Номер строки, Номер столбца)
mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
# Вставляем значения в наш массив и выводим его с помощью Print
mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))  # Вызываем функцию
prety_print(mas)  # Вызываем функцию

# Номер строки i*4 + j + 1, чтобы с нуля не считать прибавляем 1  номер столбца, тогда мы получим разницу значений в массиве 2*4+1=9
