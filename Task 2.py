# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random

candy_count = 202


def take_input(player_name: str) -> int:
    value = 0
    while value == 0:
        value = int(input(f"Сколько конфет берет {player_name}?: "))
        if not (value in range(1, 29)):
            print("Количество конфет должно быть от 1 до 28! Повторите!")
            value = 0
            continue
        return value
        break


def bot_move(player_name: str):
    if candy_count - 28 > 57:
        value = random.randint(1, 28)
    else:
        value = random.randint(1, (candy_count - 28))
    print(f"Компьютер берет {value} конфет.")
    return value


def winner(player_name: str, player_moves: list):
    print(f"Победил игрок {player_name}")
    print(f"Победная серия: {player_moves}")


player1_name = input("Введите имя первого игрока (если ввести bot - будет играть компьютер!): ")
player2_name = input("Введите имя второго игрока (если ввести bot - будет играть компьютер!): ")
player1 = 0
player2 = 0
player1_moves_log = list()
player2_moves_log = list()
whose_move = random.randint(0, 1)
candy_taken = 0
print("Начинаем игру!")

while candy_count > 28:
    if whose_move == 0:
        if player1_name.find('bot') > -1:
            candy_taken = bot_move(player1_name)
            player1_moves_log.append(candy_taken)
            candy_count -= candy_taken
            print(f"Осталось {candy_count} конфет.")
            whose_move = 1
        else:
            candy_taken = take_input(player1_name)
            player1_moves_log.append(candy_taken)
            candy_count -= candy_taken
            print(f"Осталось {candy_count} конфет.")
            whose_move = 1
    else:
        if player2_name.find('bot') > -1:
            candy_taken = bot_move(player2_name)
            player2_moves_log.append(candy_taken)
            candy_count -= candy_taken
            print(f"Осталось {candy_count} конфет.")
            whose_move = 0
        else:
            candy_taken = take_input(player2_name)
            player2_moves_log.append(candy_taken)
            candy_count -= candy_taken
            print(f"Осталось {candy_count} конфет.")
            whose_move = 0
else:
    if whose_move == 0:
        winner(player1_name, player1_moves_log)
    else:
        winner(player2_name, player2_moves_log)
