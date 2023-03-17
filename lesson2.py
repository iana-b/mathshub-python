# les2 = "кардиолог"
# print(les2[2] + les2[5] + les2[8] + les2[1] + les2[6] + les2[4] + les2[0])

# number1, number2, nuber3 = input(), input(), input()
# a, b, c = 5, 6, 7
# print(a)

# a = 5
# b = 6
# a, b = b, a
# print(a, b)

# broccoli_lover = input("Любите ли вы мороженое: ")
# if broccoli_lover == "да":
#     user_money = input("Есть деньги? ")
#     if user_money == "да":
#         sdacha = input("Есть сдача? ")
#         if sdacha == "да":
#             print("Вы купили мороженое !")
#         else:
#             print("Sorry")
#     else:
#         print("Вам не хватило денег")
# else:
#     print("Вы не купили мороженое !")

# password = "телефон"
# elite_password = "телевизор"
# user_password = input("Назовите пароль: ")
# if user_password == password:
#     print("Вы прошли")
# elif user_password == elite_password:
#     print("Вы элитно прошли")
# else:
#     print("Пароль неверный")

# password1 = "rabbit"
# password2 = "wolf"
# user_password = input("Назови пароль: ")
# if password1 == user_password or password2 == user_password:
#     print("проходи")
# else:
#     print("проход запрещен")

# password1 = "rabbit"
# password2 = "wolf"
# user_password = input("Назови пароль 1: ")
# user_password2 = input("Назови пароль 2: ")
# if user_password == password1 and user_password2 == password2:
#     print("проходи")
# else:
#     print("не проходи")

# word = input("Введите слово: ")
# if word[0] == "М" or word[-1] == "Г":
#     print("хорошее слово")
# else:
#     print("плохое слово")

# name = "fvhbvheb  hebrhbew  erhfb"
# print(len(name))

# number = int(input("Введите число: "))
# if number % 3 == 0 and len(str(number)) % 3 == 0:
#     print("крутое число")
# else:
#     print("не круто")

# number = input()
# if int(number) % 3 == 0 and len(number) % 3 == 0:
#     print("круто")
# else:
#     print("не круто")

# dz1 = input("Мышонку дали: ")
# type1 = "молоко"
# type2 = "соломинку"
# type3 = "салфетку"
# if dz1 == type1:
#     print(f"Мышонок попросил: {type2}")
# elif dz1 == type2:
#     print(f"Мышонок попросил: {type3}")
# elif dz1 == type3:
#     print(f"Мышонок попросил: {type1}")

# day = input("Введите день недели в виде числа: ")
# if day == "6" or day == "7":
#     print("Это выходной")
# else:
#     print("Это рабочий день")

# vvod = input("Введите число: ")
# if int(vvod) < 10:
#     print("Число меньше 10")
# elif int(vvod) == 10:
#     print("Число равно 10")
# else:
#     print("Число больше 10")

# print("Вы оказываетесь в странном лесу с тропинкой, разветвляющейся в двух направлениях.\nОдин путь ведет к темному замку со зловещей репутацией, а другой ведет к таинственным руинам, которые, как считается, обладают магической силой.")
# dz = input("Какой путь вы бы выбрали: ")
# if dz == "1":
#     print("Вы идете к тёмному замку")
#     zamok = input("Войти в замок ночью или дождаться утра: ")
#     if zamok == "1":
#         print("Вы вошли и безумно напуганы")
#     elif zamok == "2":
#         print("Вы дождались утра и спокойно вошли")
#     else:
#         print("Введите корректный ответ")
# elif dz == "2":
#     print("Вы идете к таинственным руинам")
#     runes = input("Вы умеете читать руны: ")
#     if runes == "1":
#         print("Вы прочли руны и поняли смысл")
#     elif runes == "2":
#         print("Вы не поняли смысл рун")
#     else:
#         print("Введите корректный ответ")
# elif dz == "никакой":
#     print("Вы остаетесь на месте")
# else:
#     print("Выберете корректный путь")

# a = "печенье"
# b = "молоко"
# c = "соломинка"
# d = "салфетка"
# word = input("Мышонку дали: ")
# if word == a:
#     next_word = b
# elif word == b:
#     next_word = c
# elif word == c:
#     next_word = d
# elif word == d:
#     next_word = a
# else:
#     next_word = "Ошибка"
# print(f"Мышонок попросил: {next_word}")
