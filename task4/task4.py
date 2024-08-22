import argparse

#Объявление парсера для аргументов командной строки
parser = argparse.ArgumentParser()

#Добавление аргументов
parser.add_argument("nums")

#Парсинг аргументов командной строки
args = parser.parse_args()

#Открытие файла numbers
file = open(args.nums)

#Инициализация массива
nums = []

#Пока не конец файла
while(line := file.readline()):
    #Добавление числа в массив
    nums.append(int(line))

#Закрытие файла numbers
file.close()

#Сортировка массива
sortedArray = sorted(nums)

#Вычисление оптимального числа для приведения - медианы
target = nums[len(nums)//2]

#Инициализация числа шагов
result = 0
#Для каждого числа
for num in nums:
    #Вычисляем модуль разницы между целевым числом и текущим
    #И прибавляем эту разницу к кол-ву шагов
    result += abs(target-num)

#Вывод результата на консоль
print(result)