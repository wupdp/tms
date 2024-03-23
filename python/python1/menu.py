def display_menu():
    print("Меню:")
    print("1. Вычислить произведение двух чисел")
    print("2. Вывести первую букву слова")
    print("3. Привет мир")
    print("4. Привет [имя]")
    print("5. Вывести массив")
    print("6. 2+2")
    print("7. Ваш возраст")
    print("0. Выйти из программы")

while True:
    display_menu()
    choice = input("Выберите программу (введите номер): ")

    if choice == "1":
        exec(open("composition.py").read())
    elif choice == "2":
        exec(open("first_letter.py").read())
    elif choice == "3":
        exec(open("hello.py").read())
    elif choice == "4":
        exec(open("helloname.py").read())
    elif choice == "5":
        exec(open("output_range.py").read())
    elif choice == "6":
        exec(open("2+2.py").read())
    elif choice == "7":
        exec(open("how_old.py").read())
    elif choice == "0":
        print("Выход из программы...")
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите номер программы из меню.")