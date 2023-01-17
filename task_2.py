from random import randint
game_type = ''
new_game = 'да'

def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, value):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

def bot_calc(value):
    k = randint(1, 29)
    while value-k <= 28 and value > 29:
        k = randint(1, 29)
    return k

def main(game_type, new_game, input_dat, p_print, bot_calc):
    while new_game == 'да':
        print("Добро пожаловать в игру с конфетами!!!\n Выберите режим игры:\n   '2 игрока'\n   'бот'\n   'сложный бот'")
        game_type = input("Введите ваш выбор: ")

        if game_type == '2 игрока':
            player1 = input("Введите имя первого игрока: ")
            player2 = input("Введите имя второго игрока: ")
            value = int(input("Введите количество конфет на столе: "))
            flag = randint(0, 2)  # флаг очередности
            if flag:
                print(f"Первый ходит {player1}")
            else:
                print(f"Первый ходит {player2}")

            counter1 = 0
            counter2 = 0

            while value > 28:
                if flag:
                    k = input_dat(player1)
                    counter1 += k
                    value -= k
                    flag = False
                    p_print(player1, k, counter1, value)
                else:
                    k = input_dat(player2)
                    counter2 += k
                    value -= k
                    flag = True
                    p_print(player2, k, counter2, value)

            if flag:
                print(f"Выиграл {player1}")
            else:
                print(f"Выиграл {player2}")

        if game_type == "бот":
            player1 = input("Введите имя игрока: ")
            player2 = "Бот"
            value = int(input("Введите количество конфет на столе: "))
            flag = randint(0, 2)  # флаг очередности
            if flag:
                print(f"Первый ходит {player1}")
            else:
                print(f"Первый ходит {player2}")

            counter1 = 0
            counter2 = 0

            while value > 28:
                if flag:
                    k = input_dat(player1)
                    counter1 += k
                    value -= k
                    flag = False
                    p_print(player1, k, counter1, value)
                else:
                    k = randint(1, 29)
                    counter2 += k
                    value -= k
                    flag = True
                    p_print(player2, k, counter2, value)

            if flag:
                print(f"Выиграл {player1}")
            else:
                print(f"Выиграл {player2}")

        if game_type == "сложный бот":
            player1 = input("Введите имя игрока: ")
            player2 = "Бот"
            value = int(input("Введите количество конфет на столе: "))
            flag = randint(0, 2)  # флаг очередности
            if flag:
                print(f"Первый ходит {player1}")
            else:
                print(f"Первый ходит {player2}")

            counter1 = 0
            counter2 = 0

            while value > 28:
                if flag:
                    k = input_dat(player1)
                    counter1 += k
                    value -= k
                    flag = False
                    p_print(player1, k, counter1, value)
                else:
                    k = bot_calc(value)
                    counter2 += k
                    value -= k
                    flag = True
                    p_print(player2, k, counter2, value)

            if flag:
                print(f"Выиграл {player1}")
            else:
                print(f"Выиграл {player2}")
        print("Хотите сыграть еще раз? да/нет: ")
        new_game = input()
        if new_game == 'нет':
            if player2 == 'Бот':
                print(f"{player1}, всего доброго!")
            elif player2 != 'Бот':
                print(f"{player1}, {player2}, всего вам доброго!")

if __name__ == '__main__':
    main(game_type, new_game, input_dat, p_print, bot_calc)