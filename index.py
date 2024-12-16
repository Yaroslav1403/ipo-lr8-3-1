#Импортируем библиотеку json 
import json

#Определяем имя файла, где будет храниться информация о звёздах
file = 'stars.json'

#Создаём список с данными о звёздах и сохраняем его в переменную data_about_stars_1
data_about_stars_1 = [
    {"id": 1, "name": "Сириус", "constellation": "Большой Пес", "is_visible": True, "radius": 1.71},
    {"id": 2, "name": "Канопус", "constellation": "Корма", "is_visible": True, "radius": 0.73},
    {"id": 3, "name": "Арктур", "constellation": "Богатырь", "is_visible": True, "radius": 1.5},
    {"id": 4, "name": "Вега", "constellation": "Лира", "is_visible": True, "radius": 2.13},
    {"id": 5, "name": "Полиус", "constellation": "Центавр", "is_visible": False, "radius": 1.3}
]
#Открываем файл для записи и сохраняем данные о звёздах в формате json
with open(file, 'w') as f:
    json.dump(data_about_stars_1, f) 

#Создаём переменную count_of_operations, которая будет использоваться для подсчета количества выполненных операций с записями о звёздах
count_of_operations = 0

#Функция для отображения всех звёзд
def display_all_stars():
    #Открываем файл для чтения
    with open(file, 'r') as f:
        #Загружаем данные о звёздах из файла
        stars = json.load(f)
        print("\nВсе записи:")
        #Проходим по каждому объекту звезды и выводим его в формате json
        for star in stars:
            print(json.dumps(star, ensure_ascii = False, indent = 4))

#Функция для поиска звезды по ID
def find_star_by_id(ID):
    #Открываем файл для чтения
    with open(file, 'r') as f:
        #Загружаем данные о звёздах из файла
        stars = json.load(f)
        #Проходим по списку звёзд и ищем нужную по ID
        for index, star in enumerate(stars):
            #Если ID совпадает
            if star['id'] == ID:
                print(f"\nЗапись найдена (позиция {index + 1}):")
                #Выводим информацию о звезде
                print(json.dumps(star, ensure_ascii = False, indent = 4))
                return True
        #Если запись не найдена
        print("Запись не найдена.")
        return False

#Функция для добавления новой звезды
def add_star():
    #Создаем пустой словарь для новой звезды
    new_star = {}
    
    while True:
        try:
            #Просим пользователя ввести ID новой звезды
            new_star['id'] = int(input("Введите ID записи: "))
            break
        except ValueError:
            #Сообщаем о неверном вводе
            print("Пожалуйста, введите корректный числовой ID.")
    
    #Просим пользователя ввести название звезды
    new_star['name'] = input("Введите название звезды: ")
    #Просим пользователя ввести название созвездия
    new_star['constellation'] = input("Введите название созвездия: ")
    
    while True:
        #Просим пользователя ввести информацию о видимости звезды без телескопа
        is_visible_input = input("Можно ли увидеть звезду без телескопа (True/False): ")
        if is_visible_input in ['True', 'False']:
            new_star['is_visible'] = is_visible_input == 'True'
            break
        else:
            #Сообщаем о неверном вводе
            print("Пожалуйста, введите 'True' или 'False'.")
    
    while True:
        try:
            #Просим пользователя ввести солнечный радиус звезды
            new_star['radius'] = float(input("Введите солнечный радиус звезды: "))
            break
        except ValueError:
            #Сообщаем о неверном вводе
            print("Пожалуйста, введите корректное число для радиуса.")
    
    #Открываем файл для чтения и загружаем существующие записи о звёздах
    with open(file, 'r') as f:
        stars = json.load(f)
    
    if any(star['id'] == new_star['id'] for star in stars):
        print("Запись с таким ID уже существует.")
        return
    
    #Добавляем новую звезду в список
    stars.append(new_star)

    #Открываем файл для записи и сохраняем обновленный список звёзд
    with open(file, 'w') as f:
        json.dump(stars, f)

    #Подтверждение добавления записи
    print("Запись добавлена.")

#Функция для удаления звезды по ID
def remove_star(ID_remove):
    #Открываем файл для чтения и загружаем существующие записи о звёздах
    with open(file, 'r') as f:
        stars = json.load(f)
    
    #Переменная для отслеживания нахождения записи
    found = False
    # Проходим по списку звёзд и ищем нужную по ID
    for index, star in enumerate(stars):
        #Если ID совпадает
        if star['id'] == ID_remove:
            #Удаляем запись из списка
            del stars[index]
            #Устанавливаем флаг нахождения записи
            found = True
            break

    if found:
        #Открываем файл для записи и сохраняем обновленный список звёзд
        with open(file, 'w') as f:
            json.dump(stars, f)
        #Подтверждение удаления записи
        print("Запись удалена.")
    else:
        #Если запись не найдена
        print("Запись не найдена.")

#Создаём бесконечный цикл, который будет работать до того момента, пока пользователь не захочет выйти
while True:
    #Выводим меню с пятью вариантами действий
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по ID")
    print("3. Добавить запись")
    print("4. Удалить запись по ID")
    print("5. Выйти из программы")

    #Создаём переменную user_choice, в которой происходит обработка того варианта действия, который выбрал пользователь
    user_choice = input("Выберите пункт меню: ")

    #Если пользователь выбрал 1-ый вариант действия
    if user_choice == '1':
        #Вызываем функцию для отображения всех звёзд
        display_all_stars()
        #Счётчик операций увеличивается на 1
        count_of_operations += 1

    #Если пользователь выбрал 2-ой вариант действия
    elif user_choice == '2':
        while True:
            try:
                #Просим пользователя ввести ID записи для поиска
                ID = int(input("Введите ID записи для поиска: "))
                #Вызываем функцию для поиска звезды по ID
                find_star_by_id(ID)
                #Счётчик операций увеличивается на 1
                count_of_operations += 1
                break  
            except ValueError:
                #Сообщаем о неверном вводе
                print("Пожалуйста, введите корректный числовой ID.")

    #Если пользователь выбрал 3-ий вариант действия
    elif user_choice == '3':
        #Вызываем функцию для добавления новой звезды
        add_star()
        #Счётчик операций увеличивается на 1
        count_of_operations += 1

    #Если пользователь выбрал 4-ый вариант действия
    elif user_choice == '4':
        while True:
            try:
                #Просим пользователя ввести ID звезды, которую он хочет удалить
                ID_remove = int(input("Введите ID записи для удаления: "))
                #Вызываем функцию для удаления звезды по ID
                remove_star(ID_remove)
                #Счётчик операций увеличивается на 1
                count_of_operations += 1
                break  
            except ValueError:
                #Сообщаем о неверном вводе
                print("Пожалуйста, введите корректный числовой ID.")

    #Если пользователь выбрал 5-ый вариант действия
    elif user_choice == '5':
        #Программа выводит количество выполненных операций
        print(f"Количество выполненных операций: {count_of_operations}")
        #Выход из цикла и завершение программы
        break  

    #Если пользователь ввёл неверное значение
    else:
        #Сообщаем о неверном вводе
        print("Неверный ввод. Пожалуйста, выберите пункт меню от 1 до 5.")
