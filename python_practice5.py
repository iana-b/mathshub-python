# Задание 1
# class Person:
#     def __init__(self, name, age, hobbies):
#         self.name = name
#         self.age = age
#         self.hobbies = hobbies
#
#     def add_hobby(self, hobby):
#         self.hobbies.append(hobby)
#
#     def remove_hobby(self, hobby):
#         self.hobbies.remove(hobby)
#
#     def introduce(self):
#         print(f"Меня зовут {self.name}, мне {self.age} лет")
#         print(f'Мои хобби: {self.hobbies}')
#
#
# my_person = Person('Iana', 28, 'книги')
# print(my_person)
# my_person.introduce()

# Задание 2
# class BankAccount:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.balance = balance
#         self.account_number = account_number
#         self.account_holder = account_holder
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Внесено: {amount}')
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print('Недостаточно средств')
#         else:
#             self.balance -= amount
#             print(f'Снято: {amount}')
#
#     def get_balance(self):
#         print(f'Текущий баланс: {self.balance}')
#
#     def __str__(self):
#         return f'Имя владельца: {self.account_holder}\nНомер счета: {self.account_number}'
#
#
# account = BankAccount("123456", "Ivan Ivanov")
# account.deposit(1000)  # выведет "Deposited 1000."
# account.get_balance()  # выведет "Current balance is 1000"
# account.withdraw(500)  # выведет "Withdrawn 500"
# account.get_balance()  # выведет "Current balance is 500
# account.withdraw(700)  # выведет "Insufficient funds!"
# print(account)

# Задание 3
# class Person:
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def get_bmi(self):
#         bmi = self.weight / (self.height ** 2)
#         return round(bmi, 2)
#
#     def recommend_diet(self):
#         bmi = self.get_bmi()
#         if bmi < 18.5:
#             return 'Недостаток веса'
#         elif 18.5 <= bmi <= 24.9:
#             return 'Норма'
#         elif 25.0 <= bmi <= 29.9:
#             return 'Избыток веса'
#         else:
#             return 'Угроза для здоровья, рекомендаци обратиться к специалисту'
#
#
# person1 = Person('Iana', 30, 1.74, 75)
# print('Индекс массы тела:', person1.get_bmi())
# print(person1.recommend_diet())

# Задача 4
# import math
#
#
# class Shape:
#     def __init__(self):
#         pass
#
#     def get_area(self):
#         pass
#
#     def get_perimeter(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__()
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#     def get_perimeter(self):
#         return self.width * 2 + self.height * 2
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius
#
#     def get_area(self):
#         return round(math.pi * (self.radius ** 2), 2)
#
#     def get_perimeter(self):
#         return round(2 * math.pi * self.radius, 2)
#
#
# my_rectangle = Rectangle(3, 5)
# my_circle = Circle(5)
# print(f'Площадь прямоугольника: {my_rectangle.get_area()}, Периметр прямоугольника: { my_rectangle.get_perimeter()}')
# print(f'Площадь круга: {my_circle.get_area()}, Периметр круга (длина окружности): {my_circle.get_perimeter()}')

# Базовая практика

# Задача 1
# def max_word_length(lst):
#     maximum = len(lst[0])
#     for i in range(len(lst)):
#         if len(lst[i]) > maximum:
#             maximum = len(lst[i])
#     return maximum
#
#
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# print(f'Длина самого длинного слова в списке: {max_word_length(my_list)}')

# def max_word_length(lst):
#     maximum = len(lst[0])
#     for each in lst:
#         if len(each) > maximum:
#             maximum = len(each)
#     return maximum
#
#
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# print(f'Длина самого длинного слова в списке: {max_word_length(my_list)}')

# Задача 2
# def is_leap_year(year: int) -> bool:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False
#
#
# test_year = 2023
# print(is_leap_year(test_year))

# def is_leap_year(year: int) -> bool:
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# test_year = 2023
# print(is_leap_year(test_year))

# Задача 3
# def is_leap_year(year: int) -> bool:
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# def filter_leap_year(dates: list) -> list:
#     new_dates = []
#     for each in dates:
#         date = each.split('.')
#         if not is_leap_year(int(date[2])):
#             new_dates.append(each)
#     return new_dates
#
#
# test_dates = ["16.02.1998", "21.12.1876", "21.01.1955", "6.11.1228", "31.12.1200", "9.07.2351"]
# print(f'res = {filter_leap_year(test_dates)}')

# def is_leap_year(year: int) -> bool:
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# def filter_leap_year(dates: list) -> list:
#     return list(filter(lambda x: (not is_leap_year(int(x.split('.')[2]))), dates))
#
#
# test_dates = ["16.02.1998", "21.12.1876", "21.01.1955", "6.11.1228", "31.12.1200", "9.07.2351"]
# print(f'res = {filter_leap_year(test_dates)}')

# Задача 4
# def pow_number(x: int, n: int):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1 / pow_number(x, - n)
#     return x * pow_number(x, n - 1)
#
#
# test_x = 2
# test_n = -3
# print(pow_number(test_x, test_n))

# Задача 5
class Contact:
    def __init__(self, name: str, phone_number: str, email: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self) -> str:
        return f'Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}'


class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name: str, phone_number: str, email: str) -> None:
        self.contacts[name] = Contact(name, phone_number, email)
        print(f"Added {name} to the phone book")

    def remove_contact(self, name: str) -> None:
        if name in self.contacts:
            self.contacts.pop(name)
        print(f"Deleted {name} from the phone book")

    def find_contact(self, name: str):
        print(self.contacts.get(name, f'Name {name} doesn\'t exist'))

    def show_all_contacts(self):
        print('Show all contacts')
        for value in self.contacts.values():
            print(value)

    def show_sorted_contacts(self):
        print('Show sorted contacts')
        names = sorted(list(self.contacts.keys()))
        for n in names:
            print(self.contacts.get(n))


phone_book = PhoneBook()
phone_book.add_contact('Vasya', '+77-88', 'vas@gmail.com')
phone_book.add_contact('Sasha', '+55', 'sasha@gmail.com')
phone_book.add_contact('Olya', '+848', 'olyalya@gmail.com')
phone_book.add_contact('Sveta', '+561-55', 'sssss@gmail.com')
phone_book.find_contact('Vasya')
phone_book.find_contact('Vanya')
phone_book.show_all_contacts()
phone_book.show_sorted_contacts()

