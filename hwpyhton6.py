'''
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
'''

result = float(input("Введите результат пробежки за 1 день >>> "))
resultmax = float(input("Введите максимальный результат пробежки >>> "))
day = 1

while True:
    print(day, "-й день", "%.2f" % (result), "km")
    result = result * 1.1
    if resultmax < result:
        resultmax = result
        print("на ", day, "-й день спортсмен достиг результата — не менее ", "%.2f" % (result), "км.day")
        break
    day += 1
