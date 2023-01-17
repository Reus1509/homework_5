import os
os.system('cls')

def rle_encode(data):
    encoding = '' 
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else: 
        encoding += str(count) + prev_char
    return encoding

with open("task_4/task_4.txt", 'r') as data:
    s = data.read()
    result = rle_encode(s)
    with open("task_4/result_task_4.txt", "w") as f:
        f.write(result)

with open("task_4/result_task_4.txt", "r") as s:
    to_console = s.read()

print(f"Готово! Результат: {to_console}")