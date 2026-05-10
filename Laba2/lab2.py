import re

#Словарь
words = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}

#Открытие файла
with open("input.txt", "r") as f:
    text = f.read()

#Поиск чисел
for slovo in re.findall(r'\b[1-9]\d*\b', text):
    if re.search(r'7{4,}', slovo):  # пропуск, где больше 4ех подряд семерок
        continue
    if len(re.findall(r'777', slovo)) != 1:  # пропуск, где больше одного повторения 777
        continue

    #Поиск нечетных чисел
    odd_digits = sorted(set(re.findall(r'[13579]', slovo)))
    print(f"{slovo}  →  {' '.join(words[d] for d in odd_digits)}")
