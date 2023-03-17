# jelly_count = 5
# while jelly_count != 0:
#     jelly_count = jelly_count - 1
#     print("Я беру еще мармеладки")
# print("Мармеладки закончились")

# a = int(input("Введите число: "))
# while a % 2 == 0:
#     a = int(input("Введите число: "))
# print("Ошибка ! Нечетное число !")

# a = input("Назовите пароль: ")
# password = "пароль"
# while a != password:
#     a = input("Назовите пароль еще раз: ")
# print("Добро пожаловать, друг !")

# a = int(input("Угадай число: "))
# number = 11
# while a != number:
#     if a > number:
#         print("Твое число больше загаданного")
#         a = int(input("Угадай число еще раз: "))
#     elif a < number:
#         print("Твое число меньше загаданного")
#         a = int(input("Угадай число еще раз: "))
# print("Вы Победили !")

# for i in range(10, 20, 2):
#     print(i)

# for i in range(6, 37, 3):
#     print(i)

# buying_list = ["хлеб", "сыр", "хлебосыр", "сырохлеб"]
# for each in buying_list:
#     print(each)

# buying_list = ["хлеб", "сыр", "хлебосыр", "киви", "сырохлеб"]
# empty_list = []
# for each in buying_list:
#     print(each)
#     if each != "киви":
#         empty_list.append(each)
#     else:
#         break
# print(empty_list)
# index = 0
# each = buying_list[index]
# while each != "киви":
#     print(each)
#     empty_list.append(each)
#     index = index + 1
#     each = buying_list[index]
# print(empty_list)

# buying_list = ["хлеб", "сыр", "хлебосыр", "сырохлеб"]
# buying_list.append("мандарины")
# print(buying_list)

# buying_list = []
# word = input("Введите продукт: ")
# while word != "киви":
#     buying_list.append(word)
#     word = input("Введите еще продукт: ")
# print(buying_list)


# number = int(input("Введите число: "))
# num_list = []
# while number >= 0:
#     if number % 2 == 0:
#         num_list.append(number)
#         print(num_list)
#     number = int(input("Введите еще число: "))
# print(num_list)

# number = [1, 24, 400, 303, 23, 33, 44, 4]
# summa = 0
# for n in number:
#     summa = summa + n

# for i in range(len(number)):
#     summa = summa + number[i]

# i = 0
# while i < len(number):
#     summa = summa + number[i]
#     i = i + 1
# print(summa)

# guest_list = ["jedi", "jedi", "jedi", "sith", "jedi"]
# index = 0
# while guest_list[index] != "sith":
#     print("все ок")
#     index = index + 1
# print("Тревога, враг найден")
# summa = 0
# for guest in guest_list:
#     if guest == "jedi":
#         summa = summa + 1
# print(summa)


# sword = input("Какой меч ? ")
# a = "красный"
# b = "голубой"
# c = "без меча"
# sum_a = 0
# sum_b = 0
# sum_c = 0
# while sword != "стоп":
#     if sword == a:
#         sum_a = sum_a + 1
#     elif sword == b:
#         sum_b = sum_b + 1
#     elif sword == c:
#         sum_c = sum_c + 1
#     sword = input("Какой меч? ")
# print(f"{sum_a} с красным мечом, {sum_b} с голубым мечом, {sum_c} без меча")

# sword = input("Какой меч ? ")
# red = 0
# blue = 0
# basic = 0
# while sword != "стоп":
#     if sword == "красный":
#         red = red + 1
#     elif sword == "голубой":
#         blue = blue + 1
#     elif sword == "без меча":
#         basic = basic + 1
#     sword = input("Какой меч? ")
# print(f"{red} с красным мечом, {blue} с голубым мечом, {basic} без меча")
