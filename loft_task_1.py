"""**Написать скрипт, создающий структуру директорий для типового проекта**
Написать функцию, которая создает структуру директорий для "типового проекта" по следующей схеме:

|--<project_name>

|-- backup

|-- documents

|-- music

|-- others

|-- pictures

|--videos

**Пример:**

![pt08_task01.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/03c4ce0c-207c-409a-9ab8-38008b05354e/pt08_task01.jpg)

**Техническое задание:**

- Функция принимает один аргумент - имя директории проекта.
- Функция возвращает объект путь, указывающий на директорию проекта(через os.path или pathlib).
- Директория проекта создается в директории запуска скрипта.
- Необходимо выбрать удобную структуру данных для хранения имен поддиректорий, учесть, что их может быть значительно больше.
- Необходимо проверять корректность(валидность) имени директории проекта:
    - Имя директории проекта не должно иметь пробелов и спецсимволов, только цифры, буквы и символы подчеркивания.
    - Если имя проекта не валидно - функция поднимает исключение TypeError.
- Если директория с таким именем проекта уже существует - функция поднимает исключение ValueError.
- В основной программе вызвать эту функцию несколько раз для различных имен проекта:
    - валидное имя проекта;
    - не валидное имя проекта;
    - имя проекта, которое уже существует.
- Корректно обработать исключения и выдать в консоль соответствующее диагностическое сообщение.

*Примечание - поищите какой метод строки подходит для проверки корректности имени директории*"""

from pathlib import Path

def create_project_dir(project_name: str) -> Path:
    if not project_name.isidentifier():
        raise TypeError
    current_path = Path(__file__).parent
    project_path = current_path / project_name
    if project_path.exists():
        raise ValueError
    project_path.mkdir()
    subdirs =  ['backup', 'documents', 'music', 'others', 'pictures', 'videos']
    for subdir in subdirs:
        path = project_path / subdir
        path.mkdir()
    return project_path

test_name = ['prj2', 'prj 10', 'prj1']

for name in test_name:
    try:
        create_project_dir(name)
    except TypeError:
        print(f"Не валидное имя проекта: {name}")
    except ValueError:
        print(f"Такая директория уже есть: {name}")
