# 1. Класс "Круг"
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
        return 3.14 * self.radius**2

    def circumference(self):
        return 2 * 3.14 * self.radius

# Создание объектов класса Circle и вызов методов
circle1 = Circle(5, "красный")
print("Площадь круга 1:", circle1.area())
print("Длина окружности круга 1:", circle1.circumference())

circle2 = Circle(3, "синий")
print("Площадь круга 2:", circle2.area())
print("Длина окружности круга 2:", circle2.circumference())

# 2. Класс "Банковский счет"
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств на счете")

# Создание объектов класса BankAccount и вызов методов
account1 = BankAccount("1234567890", "Иванов Иван")
print("Баланс счета 1:", account1.balance)
account1.deposit(1000)
print("Баланс счета 1 после пополнения:", account1.balance)
account1.withdraw(500)
print("Баланс счета 1 после снятия:", account1.balance)

account2 = BankAccount("0987654321", "Петров Петр", 500)
print("Баланс счета 2:", account2.balance)
account2.withdraw(700)
print("Баланс счета 2 после снятия:", account2.balance)

# 3. Класс "Студент"
class Student:
    def __init__(self, name, age, average_score):
        self.name = name
        self.age = age
        self.average_score = average_score

    def calculate_status(self):
        if self.average_score >= 4.5:
            return "отличник"
        elif self.average_score >= 3.5:
            return "хорошист"
        else:
            return "троечник"

# Создание объектов класса Student и вызов методов
student1 = Student("Иванов", 20, 4.8)
print("Статус студента 1:", student1.calculate_status())

student2 = Student("Петров", 21, 3.2)
print("Статус студента 2:", student2.calculate_status())

# 4. Класс "Книга"
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}"

    def set_title(self, new_title):
        self.title = new_title

# Создание объектов класса Book и вызов методов
book1 = Book("Война и мир", "Лев Толстой", 1869)
print("Информация о книге 1:", book1.get_info())
book1.set_title("Война и мир (новое издание)")
print("Новое название книги 1:", book1.title)

book2 = Book("Преступление и наказание", "Федор Достоевский", 1866)
print("Информация о книге 2:", book2.get_info())

# 5. Класс "Автомобиль"
class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Цвет: {self.color}, Год выпуска: {self.year}"

    def set_color(self, new_color):
        self.color = new_color

# Создание объектов класса Car и вызов методов
car1 = Car("Toyota", "Corolla", "серебристый", 2015)
print("Информация об автомобиле 1:", car1.get_info())
car1.set_color("белый")
print("Новый цвет автомобиля 1:", car1.color)

car2 = Car("BMW", "X5", "черный", 2019)
print("Информация об автомобиле 2:", car2.get_info())
