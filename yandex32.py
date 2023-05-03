# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# for letter in vowels:
#     print(letter)
#
# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# letters = set("коллекция")
# print(letters.intersection(vowels))
#
# print(", ".join(letters & vowels))

# s = {1, 2, 3}
# s.discard(7)
# print(s)

# s = {1, 2, 3}
# s.clear()
# print(s)

# countries_and_capitals = {"Россия": "Москва",
#                           "США": "Вашингтон",
#                           "Франция": "Париж"}
# print(countries_and_capitals["Франция"])

# countries_and_capitals = {"Россия": "Москва",
#                           "США": "Вашингтон",
#                           "Франция": "Париж"}
# countries_and_capitals["Сербия"] = "Белград"
# print(countries_and_capitals)

# d = {"key": "old_value"}
# d["key"] = "new_value"
# print(d["key"])
# print(d)

# countries_and_capitals = {"Россия": "Москва",
#                           "США": "Вашингтон",
#                           "Франция": "Париж"}
# print(countries_and_capitals["Сербия"])

# countries_and_capitals = {"Россия": "Москва",
#                           "США": "Вашингтон",
#                           "Франция": "Париж"}
# if "США" in countries_and_capitals:
#     print(countries_and_capitals["США"])
# else:
#     print("Страна пока не добавлена в словарь")

# d = {"a": 1, "b": 2, "c": 3}
# for key, value in d.items():
#     print(key, value)

# d = {"a": 1, "b": 2, "c": 3}
# x = d.pop("a")
# print(x)
# print(d)

# countries = dict()
# country = input()
# str_number = 0
# while country != "СТОП":
#     countries[country] = countries.get(country, []) + [str_number]
#     str_number += 1
#     country = input()
# for country in countries:
#     print(f"{country}: {countries[country]}")

# A - Символическая выжимка
# text = input()
# set_text = set(text)
# print("".join(set_text))
