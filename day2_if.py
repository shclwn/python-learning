# Запрашиваем число
number = int(input("Введите число: "))

# Проверяем, чётное ли оно
if number % 2 == 0:
    print("чётное")
else:
    print("нечётное")

age = int(input("Введите ваш возраст: "))
if age < 18:
    print("Доступ запрещён")
else:
    print("Добро пожаловать!")

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
if number1 > number2:
    print("Наибольшее число:", number1)
elif number1 < number2:
    print("Наибольшее число:", number2)
else:
    print("Числа равны")

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

if op == "+":
    print("Результат:", a + b)
elif op == "-":
    print("Результат:", a - b)
elif op == "*":
    print("Результат:", a * b)
elif op == "/":
    print("Результат:", a / b)
else:
    print("Ошибка: неизвестная операция")

year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")