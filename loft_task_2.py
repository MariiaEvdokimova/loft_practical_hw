"""
Сформировать файл с выбором чисел участниками лотереи.
**Техническое задание:**
1. Задан файл со списком фамилий участников [surnames.txt](https://drive.google.com/file/d/1fz3G7pdJ6iyGrgXT_B9Mh_wGQBZrlSbV/view?usp=share_link) (файл так же можно взять из задания 9.1).
2. Каждый из них случайным образом выбирает 10 чисел в диапазоне от 1 до 99.
   Генерацию случайных чисел сделать с помощью пакета random.
3. Для всех участников: фамилию участника и выбранные им числа записать в другой файл в формате csv с разделителем #.
**Пример:**
Сформировать файл с выбором чисел участниками лотереи.
Новиков#72#2#6#11#38#3#28#55#27#10
Федоров#67#32#61#34#90#13#9#90#87#96
Морозов#96#23#44#26#61#81#47#21#15#13"""


from pathlib import Path
from random import randrange

current_dir = Path(__file__).parent
data_dir = current_dir / 'data_task_01'
with open(data_dir / 'surnames.txt', mode='rt', encoding='utf-8') as file_read:
   with open(data_dir / 'result2.txt', mode='wt', encoding='utf-8') as file_write:
      for line in file_read:
         surname = line.strip()
         choices = [str(randrange(1, 99)) for _ in range(10)]
         str_choices = "#".join(choices)
         file_write.write(f"{surname}#{str_choices}\n")