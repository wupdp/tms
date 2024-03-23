import os
from jinja2 import Template

# 1. Функция умножения чисел
def multiply_numbers(a, b):
    return a * b

# Вызов функции и вывод результата
result = multiply_numbers(2, 3)
print("Результат умножения:", result)

# 2. Работа с файлами
# Создание и запись в файл
with open("test.txt", "w") as file:
    file.write("Это тестовый файл для домашнего задания по программированию")

# Чтение файла и вывод содержимого
with open("test.txt", "r") as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)

# 3. Работа с директориями
# Создание директории
os.makedirs("mydir", exist_ok=True)

# Переход в директорию
os.chdir("mydir")

# Создание файлов
for i in range(1, 4):
    with open(f"file{i}.txt", "w"):
        pass

# Вывод списка файлов в директории
print("Список файлов в директории mydir:")
print(os.listdir())

# Возвращаемся обратно в исходную директорию
os.chdir("..")

# 4. Работа с шаблонизатором Jinja2
# Создание шаблона
template_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User List</title>
</head>
<body>
    <h1>User List</h1>
    <ul>
    {% for user in users %}
        <li>{{ user.name }} - {{ user.email }}</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

# Создание списка пользователей
users = [
    {"name": "Иван", "email": "ivan@example.com"},
    {"name": "Мария", "email": "maria@example.com"},
    {"name": "Петр", "email": "petr@example.com"},
]

# Использование шаблона и вывод результата
template = Template(template_string)
rendered_template = template.render(users=users)
print("HTML код для списка пользователей:")
print(rendered_template)
