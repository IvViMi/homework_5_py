# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".

import os
os.system('cls||clear')
text = 'абв - 1, ааа - 2'
print(text)
def format_text(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = format_text(text)
print(text)