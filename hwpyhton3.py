# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

usnumber = int(input("Введите число от 1 до 9 >>> "))
print("Сумма чисел n + nn + nnn >>> ", f"{usnumber} + {usnumber * 11} + {usnumber * 111} = {usnumber * 123}")