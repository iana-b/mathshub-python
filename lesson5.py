# name = "Констанция"
# print(name[::-1])
import math


# station = "Кутузовская"
# print(station[::-1])
# print(station[::-2])
# print(station[2:9:2])

# class Dog():
#     def bark(self):
#         print("ГАВ" * 5)
#     def walk(self):
#         print("Собака на прогулке")
#     def bite(self):
#         print("Собака атакует")
#     def name_dog(self, new_name):
#         self.name = new_name
#     def print_dog_name(self):
#         print(self.name)
#
#
# Dog1 = Dog()
# Dog1.bark()
# Dog1.walk()
# Dog1.bite()
# Dog1.name_dog("Mikha")
# Dog1.print_dog_name()

# class Dog:
#     def __init__(self, breed, name, color):
#         self.breed = breed
#         self.name = name
#         self.color = color
#
#     def print_dog_info(self):
#         print(f"Эта собака породы {self.breed}, ее зовут {self.name}, цвет ее окраса {self.color}")
#
#
# Barsik = Dog("медведь", "Барсик", "белый")
# Barsik.print_dog_info()

# class Student:
#     def __init__(self, name, age, rating):
#         self.name = name
#         self.age = age
#         self.rating = rating
#
#     def get_average_rating(self):
#         print((sum(self.rating)/len(self.rating)))
#
#
# Ivanov = Student("Ivanov", 20, [5, 5, 5])
# Ivanov.get_average_rating()

# class Worker:
#     def __init__(self, name, salary, post):
#         self.name = name
#         self.salary = salary
#         self.post = post
#
#     def premium_amount(self, percent):
#         print(self.salary * percent)
#
#
# Ivanov = Worker("Ivanov", 80000, "engineer")
# Ivanov.premium_amount(0.4)

# class Triangle:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def get_area(self):
#         p = sum(self.sides) / 2
#         print(math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])))
#
#
# Triangle1 = Triangle([5, 6, 7])
# Triangle1.get_area()

# class Figure:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def get_perimeter(self):
#         print(sum(self.sides))
#
# Figure1 = Figure([5, 15, 10, 50, 6])
# Figure1.get_perimeter()

# class Hero:
#     def __init__(self, name, health, power):
#         self.name = name
#         self.health = health
#         self.power = power
#
#     def get_result(self, enemy_power, damage):
#         health_result = self.health
#         if enemy_power > self.power:
#             health_result = self.health - damage
#         print(f"Здоровье героя в результате: {health_result}")
#
#
# Hero1 = Hero("Shenhe", 33000, 2500)
# Hero1.get_result(2500, 3000)

# class Hero:
#     def __init__(self, name, health, power):
#         self.name = name
#         self.health = health
#         self.power = power
#
#     def fight(self, power, damage):
#         if power > self.power and damage > 0:
#             self.health = self.health - damage
#         if self.health <= 0:
#             print(f"Герой {self.name} проиграла")
#
#
# class Monster:
#     def __init__(self, name, health, power):
#         self.name = name
#         self.health = health
#         self.power = power
#
#     def fight(self, power, damage):
#         if power > self.power and damage > 0:
#             self.health = self.health - damage
#         if self.health <= 0:
#             print(f"Монстр {self.name} проиграла")
#
#
# Shenhe = Hero("Shenhe", 33000, 5500)
# Ayaka = Monster("Ayaka", 35500, 2000)
#
# while Shenhe.health > 0 and Ayaka.health > 0 and Shenhe.power != Ayaka.power:
#     damage_s = Ayaka.power - Shenhe.power
#     Shenhe.fight(Ayaka.power, damage_s)
#     damage_a = Shenhe.power - Ayaka.power
#     Ayaka.fight(Shenhe.power, damage_a)
#     print(Shenhe.health, Ayaka.health)
