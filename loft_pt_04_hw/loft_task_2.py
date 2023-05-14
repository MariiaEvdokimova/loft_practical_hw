""""- Заданы три списка строк: имена, действия и цели
**Пример:**
names_all = ['Иван', 'Федор', 'Катерина', 'Марина', 'Илья', 'Ольга', 'Анастасия', ]
actions_all = ['гулять', 'в школу', 'на дачу', 'в магазин', 'на спортплощадку', 'на тренировку', ]
targets_all = ['идет', 'едет', 'спешит', 'бежит', 'не торопится', ]
```
- Реализовать функцию, возвращающую список строк, каждая из которых состоит из случайно выбранных элементов, по одному из каждого списка.
- Функция принимает аргументы: количество строк в результирующем списке и три списка со строками.
**Примеры/Тесты:**
<function_name>(2, names_all, actions_all, targets_all)
       -> ['Катерина бежит на тренировку ', 'Федор спешит гулять ']
<function_name>(3, names_all, actions_all, targets_all)
      -> ['Анастасия спешит на дачу ', 'Федор спешит гулять ', 'Илья идет на тренировку ']
```
- Учесть чистоту функции и возможные side-effects
**Усложнение #1 для задания #4.2 [*]**
- Добавить в функцию еще параметр, разрешающий или запрещающий повторное использование строк в списке.
- Т.е. при запрете повторов каждая строка в списке(любом) может только один раз попасть в результирующую строку.
<function_name>(8, names_all, actions_all, targets_all, False)
      -> ['Ольга идет на тренировку ', 'Иван не торопится в школу ', 'Иван идет в магазин ',
      'Иван бежит на тренировку ', 'Илья идет на дачу ', 'Ольга не торопится на спортплощадку ',  'Федор спешит на дачу ', 'Катерина едет в школу ']
<function_name>(8, names_all, actions_all, targets_all, True)
      -> ['Илья на тренировку бежит', 'Марина в школу идет', 'Иван на спортплощадку спешит', 'Анастасия гулять не торопится', 'Ольга в магазин едет']"""

names_all = ['Иван', 'Федор', 'Катерина', 'Марина', 'Илья', 'Ольга', 'Анастасия']
actions_all = ['гулять', 'в школу', 'на дачу', 'в магазин', 'на спортплощадку', 'на тренировку', ]
targets_all = ['идет', 'едет', 'спешит', 'бежит', 'не торопится', ]

from random import choice
def mix(number, names, actions, targets):
    result = list()
    for i in range(number):
        result.append(f"{choice(names)} {choice(actions)} {choice(targets)}")
    return result

mix(12, names_all, actions_all, targets_all)

print(mix(2, names_all, actions_all, targets_all))
print(mix(3, names_all, actions_all, targets_all))

#Усложнение #1 для Задания #4.2
def mix(number, names, actions, targets, repeat):
    if not repeat:
        result = [f"{choice(names)} {choice(actions)} {choice(targets)}" for _ in range(number)]
    else:
        used_names = set()
        used_actions = set()
        used_targets = set()

        result = []
        min_len = min(len(names_all), len(actions_all), len(targets_all))

        for _ in range(min_len):
            name = choice([i for i in names_all if i not in used_names])
            action = choice([i for i in actions_all if i not in used_actions])
            target = choice([i for i in targets_all if i not in used_targets])

            used_names.add(name)
            used_actions.add(action)
            used_targets.add(target)

            result.append(f'{name} {action} {target}')

    return result

if __name__ == '__main__':
    print(mix(8, names_all, actions_all, targets_all, False))
    print(mix(8, names_all, actions_all, targets_all, True))