# Напишите программу, удаляющую из текста все слова, содержащие ""абв""


full_str = "Первое абв задание абв абв домашней работы абв."
full_str = full_str.split(" ")
key_str = ["абв", ".абв", "абв."]
res_str = " ".join(filter(lambda s: s not in key_str, full_str))
print(res_str)