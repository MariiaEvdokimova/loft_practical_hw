""""- **Задача 2.**
    - Написать функцию, которая будет собирать информацию по городам.
        **Техническое задание:**
     Функция:
    – принимает аргумент - список списков (городов) (см.[LSpt5_t1_data.py](https://drive.google.com/file/d/1oZF7nDl46cBNOUPWXf9VJHwSO2Y6XGUR/view?usp=share_link))
    [LSpt5_t1_data.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/573163a6-a8c4-474c-8463-8d74f091177c/LSpt5_t1_data.py)
    – возвращает словарь вида: Ключ - Страна, Значение - список словарей
    – Для извлечения данных о конкретном городе используйте функцию, созданную в задании 1: скопируйте ее код в код программы.
    – Корректно обрабатывайте исключения ValueError, которое она будет поднимать, в этом случае в итоговый словарь город не включается.
    – При определении функции использовать Аннотации и проверки типов(type hinting).
    – Список из [LSpt5_t1_data.py](https://drive.google.com/file/d/1oZF7nDl46cBNOUPWXf9VJHwSO2Y6XGUR/view?usp=share_link) скопируйте себе в код программы.
      [LSpt5_t1_data.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f2c668f7-a1b6-48c3-8f42-348e88b1c840/LSpt5_t1_data.py)
    **Пример:**
    {"Страна", [{"town1": xxxx, "population": xxxx, "square": xxxx}
              {"town1": xxxx, "population": xxxx, "square": xxxx}
              {"town1": xxxx, "population": xxxx, "square": xxxx}]}
    **Примеры/Тесты:**
    <function_name>(data) -> словарь
    Проверьте: Для Японии
    [{'town': 'Токио', 'population': 38505000, 'square': 8223},
    {'town': 'Осака', 'population': 19281000, 'square': 3004},
    {'town': 'Нагоя', 'population': 10240000, 'square': 3704},
    {'town': 'Фукуока', 'population': 5551000, 'square': 505}]
    Для России [{'town': 'Москва', 'population': 16555000, 'square': 5698}]
    Полностью результат работы приведен в файле [LSpt-5-2-result_level1.txt](https://drive.google.com/file/d/1RNIqHSsK_zoeIyqijwW0NW68MCmBmikB/view?usp=share_link)
    [LSpt-5-2-result_level1.txt](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3a16e7b-bf6f-426c-9f01-4b154b19cbc7/LSpt-5-2-result_level1.txt)
    *Усложнение #1 для Задания #5.2 [*]**
   В возвращаемом словаре создать еще один уровень вложенности - Первая буква названия страны.
   Создавать этот уровень или не надо определяется дополнительным аргументом функции, например title типа boolean
    **Примеры/Тесты:**
    Полностью результат работы приведен в файле [LSpt-5-2-result_level2.txt](https://drive.google.com/file/d/1SqNAQlvoaThGQOvQN3NxjkXiAYr7lnhq/view?usp=share_link)"""
import pprint

data = [["Токио","Япония",37400068,38505000,8223,],["Дели","Индия",28514000,28125000,2240,],
["Шанхай","Китай",25582000,22125000,4015,],["Сан-Паулу","Бразилия",21650000,20935000,3043,],
["Мехико","Мексика",21581000,20395000,2370,],["Каир","Египет",20076000,16925000,1917,],
["Мумбаи","Индия",19980000,23645000,881, ],["Пекин", "Китай", 19618000, 19430000, 4144, ],
["Дакка", "Бангладеш", 19578000, 18595000, 453, ],["Осака", "Япония", 19281000, 17150000, 3004, ],
["Нью-Йорк", "США", 18819000, 21045000, 11875, ],["Карачи", "Пакистан", 15400000, 16900000, 1036, ],
["Буэнос-Айрес", "Аргентина", 14967000, 15130000, 3212, ],["Чунцин", "Китай", 14838000, 8300000, 1489, ],
["Стамбул", "Турция", 14751000, 13860000, 1360, ],["Калькутта", "Индия", 14681000, 15215000, 1347, ],
["Манила", "Филиппины", 13482000, 25065000, 1813, ],["Лагос", "Нигерия", 13463000, 14630000, 1943, ],
["Рио-де-Жанейро", "Бразилия", 13293000, 12070000, 1917, ],["Тяньцзинь", "Китай", 13215000, 13035000, 2771, ],
["Киншаса", "ДР Конго", 13171000, 12960000, 583, ],["Гуанчжоу", "Китай", 12638000, 20130000, 3885, ],
["Лос-Анджелес", "США", 12458000, 15440000, 6299, ],["Москва", "Россия", 12410000, 16555000, 5698, ],
["Шэньчжэнь", "Китай", 11908000, 13195000, 1748, ],["Лахор", "Пакистан", 11738000, 11545000, 896, ],
["Бангалор", "Индия", 11440000, 11250000, 1166, ],["Париж", "Франция", 10901000, 10960000, 2845, ],
["Богота", "Колумбия", 10574000, 10705000, 585, ],["Джакарта", "Индонезия", 10517000, 34365000, 3367, ],
["Ченнай", "Индия", 10456000, 10560000, 1049, ],["Лима", "Перу", 10391000, 11460000, 894, ],["Бангкок", "Таиланд", 10156000, 16045000, 3043, ],
["Сеул", "Южная Корея", 9963000, 24315000, 2745, ],["Нагоя", "Япония", 9507000, 10240000, 3704, ],
["Хайдарабад", "Индия", 9482000, 9580000, 1230, ],["Лондон", "Великобритания", 9046000, 10840000, 1738, ],
["Тегеран", "Иран", 8896000, 14630000, 1943, ],["Чикаго", "США", 8864000, 9275000, 6856, ],
["Чэнду", "Китай", 8813000, 12160000, 1813, ],["Нанкин", "Китай", 8245000, 6125000, 1489, ],
["Ухань", "Китай", 8176000, 8470000, 1619, ],["Хошимин", "Вьетнам", 8145000, 10955000, 1645, ],
["Луанда", "Ангола", 7774000, 7645000, 984, ],["Ахмедабад", "Индия", 7681000, 7715000, 350, ],
["Куала Лумпур", "Малайзия", 7564000, 7860000, 2163, ],["Сиань", "Китай", 7444000, 7135000, 1088, ],
["Гонконг", "Китай", 7429000, 7435000, 285, ],["Дунгуань", "Китай", 7360000, 8410000, 1748, ],
["Ханчжоу", "Китай", 7236000, 6960000, 1334, ],["Фошань", "Китай", 7236000,],
["Шэньян", "Китай", 6921000, 7055000, 1502, ],["Эр-Рияд", "Сауд.Аравия", 6907000, 6050000, 1658, ],
["Багдад", "Ирак", 6812000, 7315000, 673, ],["Сантьяго", "Чили", 6680000, 6410000, 1140, ],
["Сурат", "Индия", 6564000, 6385000, 233, ],["Мадрид", "Испания", 6497000, 6345000, 1360, ],
["Сучжоу", "Китай", 6339000, 5250000, 1373, ],["Пуна", "Индия", 6276000, 6265000, 583, ],
["Харбин", "Китай", 6115000,],["Хьюстон", "США", 6115000, 6315000, 4841, ],["Даллас", "США", 6099000, 6550000, 5175, ],
["Торонто", "Канада", 6082000, 6630000, 2300, ],["Дар-эс-Салам", "Танзания", 6048000, ],
["Майами", "США", 6036000, ],["Белу-Оризонти", "Бразилия", 5972000, ],
["Сингапур", "Сингапур", 5792000, ],["Филадельфия", "США", 5695000, ],
["Атланта", "США", 5572000, 5580000, 7296, ],["Фукуока", "Япония", 5551000, 2480000, 505, ],
["Хартум", "Судан", 5534000, 5685000, 1010, ],["Барселона", "Испания", 5494000, 4810000, 1075, ],
["Йоханнесбург", "Южная Африка", 5486000, 9335000, 2590, ],["Санкт-Петербург", "Россия", 5383000, ],
["Циндао", "Китай", 5381000, ],["Далянь", "Китай", 5300000, ],["Вашингтон", "США", 5207000, 7515000, 5281, ],
["Янгон", "Мьянма", 5157000, ],["Александрия", "Египет", 5086000, ],
["Цзинань", "Китай", 5052000, ],["Гвадалахара", "Мексика", 5023000, ], ]

def extract (data:list) -> dict:
    #[Город, Страна, Население в 2018 году, Население сейчас, Площадь]
    if len(data)<5:
        raise ValueError
    result = {"country":data[1], "town": data[0], "population":max(data[2],data[3]), "square":data[4]}
    return result

def towns_inf(data: list) -> dict:
    result = {}
    for cell in data:
        try:
            town = extract(cell)
        except ValueError:
            continue
        country = town.pop('country')
        if country not in result:
            result[country] = [town]
        else:
            result[country].append(town)
    return result

rez = towns_inf(data)
print(rez)
print(rez['Япония'])


#Усложнение #1 для задания 5.2

def extract_town_info (lst:list) -> dict:
    #[Город, Страна, Население в 2018 году, Население сейчас, Площадь]
    if len(lst)<5:
        raise ValueError
    result = {"country":lst[1], "town": lst[0], "population":max(lst[2],lst[3]), "square":lst[4]}
    return result

def group_towns_info_by_country(lst: list) -> dict:
    result = {}
    for cell in data:
        try:
            town = extract_town_info(cell)
        except ValueError:
            continue
        country = town.pop('country')
        if country not in result:
            result[country] = [town]
        else:
            result[country].append(town)
    return result

def group_countries_by_first_letter(dct: dict) -> dict:
    new_dict = {}

    for key, value in dct.items():
        first_letter = key[0].upper()
        if first_letter not in new_dict:
            new_dict[first_letter] = {}
        for item in value:
            country = key
            town = item['town']
            population = item['population']
            square = item['square']
            if country not in new_dict[first_letter]:
                new_dict[first_letter][country] = {}
            new_dict[first_letter][country][town] = {"population": population, "square": square}

    return new_dict

if __name__ == '__main__':
    data = [["Токио","Япония",37400068,38505000,8223,],["Дели","Индия",28514000,28125000,2240,],
["Шанхай","Китай",25582000,22125000,4015,],["Сан-Паулу","Бразилия",21650000,20935000,3043,],
["Мехико","Мексика",21581000,20395000,2370,],["Каир","Египет",20076000,16925000,1917,],
["Мумбаи","Индия",19980000,23645000,881, ],["Пекин", "Китай", 19618000, 19430000, 4144, ],
["Дакка", "Бангладеш", 19578000, 18595000, 453, ],["Осака", "Япония", 19281000, 17150000, 3004, ],
["Нью-Йорк", "США", 18819000, 21045000, 11875, ],["Карачи", "Пакистан", 15400000, 16900000, 1036, ],
["Буэнос-Айрес", "Аргентина", 14967000, 15130000, 3212, ],["Чунцин", "Китай", 14838000, 8300000, 1489, ],
["Стамбул", "Турция", 14751000, 13860000, 1360, ],["Калькутта", "Индия", 14681000, 15215000, 1347, ],
["Манила", "Филиппины", 13482000, 25065000, 1813, ],["Лагос", "Нигерия", 13463000, 14630000, 1943, ],
["Рио-де-Жанейро", "Бразилия", 13293000, 12070000, 1917, ],["Тяньцзинь", "Китай", 13215000, 13035000, 2771, ],
["Киншаса", "ДР Конго", 13171000, 12960000, 583, ],["Гуанчжоу", "Китай", 12638000, 20130000, 3885, ],
["Лос-Анджелес", "США", 12458000, 15440000, 6299, ],["Москва", "Россия", 12410000, 16555000, 5698, ],
["Шэньчжэнь", "Китай", 11908000, 13195000, 1748, ],["Лахор", "Пакистан", 11738000, 11545000, 896, ],
["Бангалор", "Индия", 11440000, 11250000, 1166, ],["Париж", "Франция", 10901000, 10960000, 2845, ],
["Богота", "Колумбия", 10574000, 10705000, 585, ],["Джакарта", "Индонезия", 10517000, 34365000, 3367, ],
["Ченнай", "Индия", 10456000, 10560000, 1049, ],["Лима", "Перу", 10391000, 11460000, 894, ],["Бангкок", "Таиланд", 10156000, 16045000, 3043, ],
["Сеул", "Южная Корея", 9963000, 24315000, 2745, ],["Нагоя", "Япония", 9507000, 10240000, 3704, ],
["Хайдарабад", "Индия", 9482000, 9580000, 1230, ],["Лондон", "Великобритания", 9046000, 10840000, 1738, ],
["Тегеран", "Иран", 8896000, 14630000, 1943, ],["Чикаго", "США", 8864000, 9275000, 6856, ],
["Чэнду", "Китай", 8813000, 12160000, 1813, ],["Нанкин", "Китай", 8245000, 6125000, 1489, ],
["Ухань", "Китай", 8176000, 8470000, 1619, ],["Хошимин", "Вьетнам", 8145000, 10955000, 1645, ],
["Луанда", "Ангола", 7774000, 7645000, 984, ],["Ахмедабад", "Индия", 7681000, 7715000, 350, ],
["Куала Лумпур", "Малайзия", 7564000, 7860000, 2163, ],["Сиань", "Китай", 7444000, 7135000, 1088, ],
["Гонконг", "Китай", 7429000, 7435000, 285, ],["Дунгуань", "Китай", 7360000, 8410000, 1748, ],
["Ханчжоу", "Китай", 7236000, 6960000, 1334, ],["Фошань", "Китай", 7236000,],
["Шэньян", "Китай", 6921000, 7055000, 1502, ],["Эр-Рияд", "Сауд.Аравия", 6907000, 6050000, 1658, ],
["Багдад", "Ирак", 6812000, 7315000, 673, ],["Сантьяго", "Чили", 6680000, 6410000, 1140, ],
["Сурат", "Индия", 6564000, 6385000, 233, ],["Мадрид", "Испания", 6497000, 6345000, 1360, ],
["Сучжоу", "Китай", 6339000, 5250000, 1373, ],["Пуна", "Индия", 6276000, 6265000, 583, ],
["Харбин", "Китай", 6115000,],["Хьюстон", "США", 6115000, 6315000, 4841, ],["Даллас", "США", 6099000, 6550000, 5175, ],
["Торонто", "Канада", 6082000, 6630000, 2300, ],["Дар-эс-Салам", "Танзания", 6048000, ],
["Майами", "США", 6036000, ],["Белу-Оризонти", "Бразилия", 5972000, ],
["Сингапур", "Сингапур", 5792000, ],["Филадельфия", "США", 5695000, ],
["Атланта", "США", 5572000, 5580000, 7296, ],["Фукуока", "Япония", 5551000, 2480000, 505, ],
["Хартум", "Судан", 5534000, 5685000, 1010, ],["Барселона", "Испания", 5494000, 4810000, 1075, ],
["Йоханнесбург", "Южная Африка", 5486000, 9335000, 2590, ],["Санкт-Петербург", "Россия", 5383000, ],
["Циндао", "Китай", 5381000, ],["Далянь", "Китай", 5300000, ],["Вашингтон", "США", 5207000, 7515000, 5281, ],
["Янгон", "Мьянма", 5157000, ],["Александрия", "Египет", 5086000, ],
["Цзинань", "Китай", 5052000, ],["Гвадалахара", "Мексика", 5023000, ], ]
    towns_by_country = group_towns_info_by_country(data)
    alphabet_info = group_countries_by_first_letter(towns_by_country)
    pprint.pprint(alphabet_info, indent = 4)

