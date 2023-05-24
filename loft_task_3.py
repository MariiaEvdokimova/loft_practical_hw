"""
Продолжить выполнение предыдущего задания - 9.2: Лотерея
**Техническое задание:**
1. В программе случайным образом генерируется три “счастливых” числа в диапазоне от 1 до 99.
2. Считать данные об участниках и их выборе чисел из файла предыдущего задания.
3. Вывести на экран фамилии тех участников, которые угадали хотя бы одно “счастливое” число."""


from pathlib import Path
from random import randrange

current_dir = Path(__file__).parent
data_dir = current_dir / 'data_task_01'
win = [str(randrange(1, 99)) for _ in range(3)]

with open(data_dir / 'result2.txt', mode='rt', encoding='utf-8') as file_read:
   for line in file_read:
       surname, *choices = line.strip().split("#")
       lenght = len(set(choices).intersection(win))
       if lenght == 1:
            print(f"{surname} угадал одно “счастливое” число.")
       elif lenght == 2:
            print(f"{surname} угадал два “счастливых” числа.")