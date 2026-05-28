#Задание 1

students = ["Анна", "Борис", "Вика"]
print(students[0])
print(students[-1])
print(len(students))
students[1] = "Пётр"
print(students)

#Задание 2

shopping_list = []
shopping_list.append("молоко")
shopping_list.append("хлеб")
shopping_list.append("яйца")
shopping_list.insert(1, "масло")
shopping_list.remove("хлеб")
removed_item = shopping_list.pop()
print("Удалён:", removed_item)
print("Итоговый список:", shopping_list)

#Задание 3

numbers = [5, 2, 8, 1, 9, 3]
print("Изначальный список", numbers)
numbers.sort()
print("Отсортированный список", numbers)
numbers.reverse()
print("Перевёрнутый список", numbers)
numbers2 = [10, 20, 30, 40, 50]
print("Новый список", numbers2)
first_three = numbers2[:3]
print("Первые три элемента из нового списка", first_three)

#Задание 4

grades = [4, 5, 3, 5, 4, 4, 5, 2, 5, 4]
print("Журнал оценок", grades)
count_5 = grades.count(5)
print("Количество пятёрок:", count_5)
index_2 = grades.index(2)
print("Индекс первой двойки:", index_2)
has_one = 1 in grades
print("Есть ли оценка 1?", has_one)

#Задание 5 

numbers = [3, 7, 2, 9, 5]
print("Список", numbers)
total = 0
for num in numbers:
    total = total + num   
print("Сумма:", total)
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print("Максимальное число:", max_value)

#Задание 6

days = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
print("Кортеж дней:", days)
print("Первый день:", days[0])
print("Последний день:", days[-1])
# days[0] = "понедельник"   # TypeError: 'tuple' object does not support item assignment
days_list = list(days)          # теперь список
print("Список после преобразования:", days_list)
days_list[0] = "понедельник"
print("Изменённый список:", days_list)
days_tuple = tuple(days_list)
print("Новый кортеж:", days_tuple)