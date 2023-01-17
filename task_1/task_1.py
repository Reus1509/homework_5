# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
os.system('cls')

with open("task_1/text_task_1.txt", "r", encoding="utf-8") as data:
    txt = data.read()
print()
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')
with open("task_1/result_task_1.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(lst))