import re

words = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре',
         '5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}

with open("input.txt", "r") as f:
    text = f.read()

# Единственная регулярка — находим все натуральные числа
for num in re.findall(r'\b[1-9]\d*\b', text):
    if '7777' not in num and num.count('777') == 1:
        odd_digits = sorted(set(c for c in num if c in '13579'))
        print(f"{num}  →  {' '.join(words[d] for d in odd_digits)}")
