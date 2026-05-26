# Задание 1: чётное или нечётное
number = int(input("Введите число: "))
if number % 2 == 0:
    print("чётное")
else:
    print("нечётное")

# Задание 2: проверка возраста
age = int(input("Введите возраст: "))
if age < 18:
    print("Доступ запрещён")
else:
    print("Добро пожаловать!")

# Задание 3: максимум из двух
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
if num1 > num2:
    print("Наибольшее:", num1)
elif num1 < num2:
    print("Наибольшее:", num2)
else:
    print("Числа равны")

# Задание 4: калькулятор
a = float(input("Число 1: "))
b = float(input("Число 2: "))
op = input("Операция (+, -, *, /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Неизвестная операция")

# Задание 5: високосный год
year = int(input("Год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Високосный")
else:
    print("Не високосный")