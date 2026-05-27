# Задание 1
N = int(input("Введите N:"))
total = 0 
for i in range(1, N+1):
    total = total + i
print("Сумма от 1 до", N, "=", total)
# Задание 2
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
# Задание 3
x = 1 
while x <= 10:
    print(f"{x} идём дальше")
    x += 1
# Задание 4
secret = 7
guess = None
while guess != secret:
    guess = int(input("Угадай число (от 1 до 10): "))
    if guess != secret:
        print("Не угадал, попробуй ещё")
    else:
        print("Поздравляю!")
# Задание 5
for i in range(0,21,2):
    print(i)
# Задание 6
for i in range(1,6):
    print("*" * i)