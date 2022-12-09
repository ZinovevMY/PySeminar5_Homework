# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random


candy_count = 2021
player1_name = input("Введите имя первого игрока: ")
player2_name = input("Введите имя второго игрока: ")
player1 = 0
player2 = 0
player1_moves_log = list()
player2_moves_log = list()


def take_input(player_name: str):
    while True:
        value = int(input(f"Сколько конфет берет {player_name}?: "))
        if not (value in range(1, 29)):
            print("Количество конфет должно быть от 1 до 28! Повторите!")
            continue
        # if value > candy_count:
        #     print("Нет столько конфет на столе!")
        #     continue
        return value

def check_winner(player_name: str):
    if candy_count < 28:
        print(f"Игрок {player_name} победил!!!")

print("Начинаем игру!")
whose_move = random.randint(1, 3)


