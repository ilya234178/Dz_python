# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1 , 1.2, 3.1 , 5, 10.01]
list2 = []
for i in range(len(list1)):
    list2.append(round((list1[i] - int(list1[i])), 3))

print(max(list2) - min(list2))
