"""- Изменить предыдущую задачу
**Техническое задание**
- Теперь функция должна возвращать не список, а генератор целых четных чисел в заданном диапазоне.
- Использовать генераторное выражение
- Остальные условия остаются прежними
- Вызвать функцию для некоторых аргументов.
- Проверить тип возвращаемого объекта.
- Вызвать функцию для некоторых аргументов.
- Исчерпать итератор в цикле while с помощь функции next(), дойти до исключения StopIteration
**Пример:**
<function_name>(1,10) -> <generator object...>
<function_name>(1,-10) -> ValueError"""

def main(begin: int, end : int) -> list:
    if begin > end:
        raise ValueError
    return (num for num in range(begin, end+1) if num %2 == 0)

print(main(1,10))
for item in main(1,10):
     print(item, end = ", ")

print("\n", "*" * 30)
gen2 = main(2,14)
while True:
    print(next(gen2), end = ", ")