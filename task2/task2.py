import argparse

#Объявление парсера для аргументов командной строки
parser = argparse.ArgumentParser()

#Добавление аргументов
parser.add_argument("circle")
parser.add_argument("dots")

#Парсинг аргументов командной строки
args = parser.parse_args()

#Открытие файла circle
circle = open(args.circle)
#Считывание координат центра окружности в int
x, y = (float(i) for i in circle.readline().split())
#Считывание радиуса окружности в int
r = float(circle.readline())
#Закрытие файла circle
circle.close()

#Открытие файла dots
dots = open(args.dots)

#Пока не конец файла
while(line := dots.readline()):
    #Считывание координат точки
    a, b = (float(i) for i in line.split())
    #Определение положения точки относительно окружности
    if pow(x-a,2) + pow(y-b,2) < pow(r,2):
        print(1)
    elif pow(x-a,2) + pow(y-b,2) == pow(r,2):
        print(0)
    else:
        print(2)

#Закрытие файла dots
dots.close()