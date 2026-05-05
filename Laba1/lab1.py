#Словарь
words   = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
odd = {'1','3','5','7','9'}

text = ""
with open("input.txt", "rb") as f:
    while kusok := f.read(64):
        text += kusok.decode()

for slovo in text.split():
    if slovo.isdigit() and slovo != '0' and '7777' not in slovo and slovo.count('777') <= 1:
        odd_digits = sorted(set(c for c in slovo if c in odd))
        print(f"{slovo}  →  {' '.join(words[d] for d in odd_digits)}")
