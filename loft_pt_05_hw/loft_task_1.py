""""- **Задача 1.**
    - Написать функцию преобразующую список в словарь.
        **Техническое задание:**
    Функция:
    - принимает аргумент - список вида [Город, Страна, Население в 2018 году, Население сейчас, Площадь]
    - возвращает словарь вида {"country":xxxx, "town": xxxx, "population":xxxx, "square":xxxx}
    Где население(population) - максимальное из двух населений города.
    Если данные извлечь невозможно - отсутствует площадь (такое будет в данных) - функция поднимает исключение ValueError
    Проверить работоспособность функции на приведенных данных из файла [LSpt5_t1_data.py](https://drive.google.com/file/d/1oZF7nDl46cBNOUPWXf9VJHwSO2Y6XGUR/view?usp=share_link).
    Для этого импортировать файл LSpt5_t1_data.py под псевдонимом в свой код.
    При определении функции использовать Аннотации и проверки типов(type hinting)
 **Примеры/Тесты:**
<function_name>(["Мумбаи", "Индия", 19980000, 23645000, 881,]) -> {"country":"Индия", "town": "Мумбаи","population":23645000, "square":881}
<function_name>(["Циндао", "Китай", 5381000,]) -> ValueError
**Усложнение #1 для Задания #5.1 [*]**
      - Функция принимает не список, а 5 аргументов, все остальное как в основном задании
        **Примеры/Тесты:**
<function_name>("Мумбаи", "Индия", 19980000, 23645000, 881,) -> {"country":"Индия", "town": "Мумбаи","population":23645000, "square":881}
<function_name>("Циндао", "Китай", 5381000,) -> ValueError"""

def extract(data: list) -> dict:
    #[Город, Страна, Население в 2018 году, Население сейчас, Площадь]
    if len(data) < 5:
        raise ValueError
    result = {"country": data[1], "town": data[0], "population": max(data[2], data[3]), "square": data[4]}
    return result

#def extract2(data: list) -> dict:
#    town, country, pop2018, pop, square = data
#    result = {"country": country, "town": town, "population": max(pop2018, pop), "square": square}
#    return result

print(extract(["Мумбаи", "Индия", 19980000, 23645000, 881, ]))
print(extract(["Циндао", "Китай", 5381000, ]))

#Усложнение #1 для задания 5.1
def extract3(*args: tuple) -> dict:
    if len(args) < 5:
        raise ValueError
    result = {"country": args[1], "town": args[0], "population": max(args[2], args[3]), "square": args[4]}
    return result

print(extract3("Мумбаи", "Индия", 19980000, 23645000, 881, ))