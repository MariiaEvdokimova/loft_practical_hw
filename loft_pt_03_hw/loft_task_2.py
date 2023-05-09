""""
- Реализовать обработку структуры данных товары.
Она представляет собой список списков. Пример структуры в конце условия.
- Каждый товар - список из трех элементов вида название, цена на 1 шт, кол-во штук на складе.
Например:
['принтер', 7100, 1]

- Данные завести прямо в код, не надо вводить их с клавиатуры.
**Техническое задание:**
Необходимо собрать аналитику о товарах.
1. Вывести общее кол-во единиц товара на складе.
2. Вывести общую стоимость всех товаров на складе
3. Вывести список всех наименований товаров, без повторов.

**Примеры/Тесты:**
Общее количество единиц товара: 164 шт.
Общая цена товаров на складе : 730180р.
На складе есть следующие наименования: ['принтер', 'компьютер', 'клавиатура', 'веб-камера', 'монитор', 'сканер', 'мышь']
Для приведенной в условии структуры вывод на экран должен быть следующим:

**Усложнение #1 для задания 3.2 [*]** Дополнительно вывести общее количество и общую стоимость раздельно по наименованиям товаров
**Примеры/Тесты:**
принтер  :  238600р. 51 шт.
компьютер  :  253000р. 15 шт.
клавиатура :  4150р. 31 шт.
веб-камера :  1730р. 17 шт.
монитор  :  207000р. 20 шт.
сканер : 24100р. 25 шт.
мышь :  1600р.  5 шт.
```
**Пример структуры данных:
**data = [['принтер', 7100, 1], ['компьютер', 75000, 1], ['принтер', 3500, 8], ['клавиатура', 950, 15], ['веб-камера', 920, 8],
['монитор', 30000, 9], ['сканер', 7900, 15], ['веб-камера', 810, 9], ['компьютер', 57000, 5], ['компьютер', 46000, 1],
['мышь', 870, 1], ['монитор', 56000, 5], ['монитор', 47000, 3], ['сканер', 7800, 5], ['мышь', 730, 4], ['принтер', 43000, 10],
['клавиатура', 600, 2], ['сканер', 8400, 5], ['монитор', 74000, 3], ['принтер', 59000, 8], ['принтер', 30000, 15], ['клавиатура', 1200, 10], ['клавиатура', 1400, 4], ['компьютер', 75000, 8], ['принтер', 96000, 9],]"""

data = [['принтер', 7100, 1], ['компьютер', 75000, 1], ['принтер', 3500, 8], ['клавиатура', 950, 15], ['веб-камера', 920, 8],
['монитор', 30000, 9], ['сканер', 7900, 15], ['веб-камера', 810, 9], ['компьютер', 57000, 5], ['компьютер', 46000, 1],
['мышь', 870, 1], ['монитор', 56000, 5], ['монитор', 47000, 3], ['сканер', 7800, 5], ['мышь', 730, 4], ['принтер', 43000, 10],
['клавиатура', 600, 2], ['сканер', 8400, 5], ['монитор', 74000, 3], ['принтер', 59000, 8], ['принтер', 30000, 15], ['клавиатура', 1200, 10], ['клавиатура', 1400, 4], ['компьютер', 75000, 8], ['принтер', 96000, 9],]

price_total = 0
quantity_total = 0
name_total = []
for name, price, quantity in data:
    quantity_total += quantity
    price_total += price
    if name not in name_total:
        name_total.append(name)
print(f"Общее количество единиц товара: {quantity_total} шт.")
print(f"Общая цена товаров на складе: {price_total} р.")
print(f"На складе есть следующие наименования: {name_total} ")

#Усложнение #1 для задания 3.2

s = {}
for i in data:
    if i[0] not in s:
        s[i[0]] = [i[1], i[2]]
    else:
       s[i[0]][0] += i[1]
       s[i[0]][1] += i[2]

for key, values in s.items():
    print(f"{key} : {values[0]}р. {values[1]} шт.")