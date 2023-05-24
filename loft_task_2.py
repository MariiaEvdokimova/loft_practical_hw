"""**Техническое задание:**
- Написать функцию, которая удаляет пустые поддиректории в заданной директории.
- Функция принимает аргумент: имя директории.
- Функция возвращает список имен поддиректорий, которые были удалены – только непосредственно имя директорий, не весь путь.

**Техническое задание:**
Используйте приведенный архив с поддиректориями [data](https://drive.google.com/drive/folders/1UWpyB25hhW1lGM6xdLqHa6ySFP4JnmMD?usp=share_link), только директории 002, 003, 005, 008 не пустые и должны остаться.
**Архив для скачивания:**
[data-20230512T115603Z-001.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90bb9540-fe3d-403f-a848-d9d6572a38f1/data-20230512T115603Z-001.zip)
Проверьте работоспособность своего кода.
```python
<function_name>("data") -> ['001', '004', '006', '007', '009']
```
*Примечание. Вспомните или проверьте можно ли удалить не пустую директорию и что случится, если попытаться это сделать. Подумайте как использовать “ответ” Python.*"""

from pathlib import Path

def remove_empty_dir(name: str) -> list:
    current_path = Path(__file__).parent
    data_path = current_path / name
    remove_names = []
    for item in data_path.iterdir():
        name = item.name
        try:
           item.rmdir()
        except OSError:
          continue
        remove_names.append(name)
    return remove_names

print(remove_empty_dir("data"""))

