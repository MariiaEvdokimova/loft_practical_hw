""""- Изменить предыдущую задачу
**Техническое задание**
- Функция должна теперь быть функцией-генератором
- Вместо генераторного выражения использовать в теле функции ключевое слово yield
- Остальные условия остаются прежними
- Вызвать функцию для некоторых аргументов.
    - Проверить тип возвращаемого объекта.
    - Исчерпать итератор в цикле for. Например вывести все значения через запятую.
- Вызвать функцию для некоторых аргументов.
    - Исчерпать итератор в цикле while с помощью функции next(), дойти до исключения StopIteration
    <function_name>(1,10) -> <generator object...>
    <function_name>(1,-10) -> ValueError"""

def main(begin: int, end : int) -> list:
    if begin > end:
        raise ValueError
    for num in range(begin, end+1):
        if num %2 == 0:
            yield num

print(main(1,10))
for item in main(1,10):
     print(item, end = ", ")

print("\n", "*" * 30)
gen2 = main(2,14)
while True:
    print(next(gen2), end = ", ")