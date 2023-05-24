    """
**Техническое задание:**
1. В файле хранятся данные о ФИО людей в виде строк. Пример файла [surnames.txt](https://drive.google.com/file/d/1fz3G7pdJ6iyGrgXT_B9Mh_wGQBZrlSbV/view?usp=share_link) Пример данных: Иванов,Иван,Иванович.
[surnames.txt](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aa1a982d-48cb-4da9-bb1b-cb8cc1cfa08b/surnames.txt)
1. Преобразовать эти данные к виду Иванов И.И. и записать в результирующий файл.
2. Нельзя считывать все данные из файла в память компьютера – только построчная обработка."""

from pathlib import Path

current_dir = Path(__file__).parent
data_dir = current_dir / 'data_task_01'
with open(data_dir / 'surnames.txt', mode = 'rt', ecoding = 'utf-8') as file_read:
    for line in file_read:
        line.strip()