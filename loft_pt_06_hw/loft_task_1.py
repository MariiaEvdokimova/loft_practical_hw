""""- Сформировать список целых четных чисел в заданном диапазоне
**Техническое задание:**
Написать функцию
- аргументы - границы диапазона. Два целых числа.
- возвращаемое значение - список чисел.
Для формирования списка использовать Comprehensions.
Последовательность чисел должна быть неубывающая, если это сделать невозможно функция поднимает исключение ValueError.
**Примеры/Тесты:**
<function_name>(1,10) -> [2, 4, 6, 8, 10]
<function_name>(1,13) -> [2, 4, 6, 8, 10, 12]
<function_name>(-2,14) -> [-2, 0, 2, 4, 6, 8, 10, 12, 14]
<function_name>(1,-10) -> ValueError

**Усложнение #1 для Задания #6.1 [*]**
Выполнить дополнительное преобразование с элементами по схеме:
Если элемент больше чем середина диапазона - преобразовать его к типу float
**Примеры/Тесты:**
<function_name>(1,10) -> [2, 4, 6.0, 8.0, 10.0]
<function_name>(1,13) -> [2, 4, 6, 8.0, 10.0, 12.0]
<function_name>(-2,14) -> [-2, 0, 2, 4, 6, 8, 10.0, 12.0, 14.0]
<function_name>(1,-10) -> ValueError"""

def main(begin: int, end: int) -> list:
     if begin > end:
         raise ValueError
     result = [num for num in range(begin, end+1) if num % 2 == 0]
     if not result:
          raise ValueError
     return result


print(main(1,10))
print(main(1,13))
print(main(-2,14))
print(main(1,1)) #добавлена проверка
print(main(1,-10))


#Усложнение #1 для Задания #6.1
def main(begin: int, end: int) -> list:
    if begin > end:
        raise ValueError
    rez2 = [float(num) if num > (end - begin) / 2 else num for num in [num for num in range(begin, end+1) if num % 2 == 0]]
    return rez2

print(main(1,10))
print(main(1,13))
print(main(-2,14))
print(main(1,-10))

