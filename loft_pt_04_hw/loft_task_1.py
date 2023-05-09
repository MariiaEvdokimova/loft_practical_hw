""""- **Задача 1.**
    - Напишите функцию, которая заменяет числа в переданном ей списке по схеме: все вхождения минимального числа заменить на максимальное число.
    **Техническое задание:**
    1. Функция принимает один аргумент - список целых чисел.
    2. Возвращает новый список с заменой минимального числа(всех вхождений) на максимальное число.
    3. Если ни одна замена не была произведена, функция возвращает None.
    *Примечание:* Обратите внимание на side effects функции.
    **Примеры/Тесты:**"
<function_name>([1, 3, 1, 3, 4, 2, 5, 5, 2]) -> [5, 3, 5, 3, 4, 2, 5, 5, 2]
Т.е. все 1 заменены на 5.
<function_name>([2, 3, 2, 3, 4, 2, 4, 4, 2]) -> [4, 3, 4, 3, 4, 4, 4, 4, 4]
Т.е. все 2 заменены на 4.
<function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None""
**Усложнение #1 для Задания #4.1 [*]**
Добавьте аргумент в функцию, который определит, как будут заменены числа:
"min-max" минимальные на максимальные
"max-min" максимальные на минимальные
**Примеры/Тесты:
**<function_name>([1, 3, 1, 3, 4, 2, 5, 5, 2], "min-max") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
<function_name>([1, 3, 1, 3, 4, 2, 5, 5, 2], "max-min")  -> [1, 3, 3, 3, 4, 2, 1, 1, 2]"""

def replace(lst_data):
    #lst_rez = lst_data.copy()
    # вычисляем каждое значение независимо
    min_val = min(lst_data)
    max_val = max(lst_data)
    if min_val == max_val:
        return
    for idx, el in enumerate(lst_data):
        if el == min_val:
            lst_data[idx] = max_val
    return lst_data

#test1=[1, 3, 1, 3, 4, 2, 5, 5, 2]
#print(test1)
#print(replace(test1))
#print(test1)

print(replace([1, 3, 1, 3, 4, 2, 5, 5, 2]))
print(replace([2, 3, 2, 3, 4, 2, 4, 4, 2]))
print(replace([3, 3, 3, 3, 3, 3, 3, 3, 3]))

#Усложнение #1 для Задания #4.1
def replace_mm(lst_data, replacement_type):
    min_val = min(lst_data)
    max_val = max(lst_data)
    if min_val == max_val:
       return
    for idx, el in enumerate(lst_data):
        if replacement_type == "min-max":
            if el == min_val:
             lst_data[idx] = max_val
        if replacement_type == "max-min":
            if el == max_val:
             lst_data[idx] = min_val
    return lst_data

print(replace_mm([1, 3, 1, 3, 4, 2, 5, 5, 2], "min-max"))
print(replace_mm([1, 3, 1, 3, 4, 2, 5, 5, 2], "max-min"))