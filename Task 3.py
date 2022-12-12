# Создайте программу для игры в ""Крестики-нолики"".


field = list(range(1,10))
win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def draw_field():
    print('-------------')
    for i in range(3):
        print('|', field[0 + i * 3],'|', field[1 + i * 3],'|', field[2 + i * 3],'|')
    print('-------------')


def get_input(player_name):
    while True:
        value = int(input(f"Куда ставим {player_name}: "))
        if value < 0 or value > 9:
            print("Ошибка, введите снова!")
            continue
        if str(field[value - 1]) in 'XO':
            print("Занято!")
            continue
        field[value - 1] = player_name
        break


def check_winner():
    for i in win_combinations:
        if field[i[0] - 1] == field[i[1] - 1] == field[i[2] - 1]:
            return field[i[1] - 1]
    else:
        return False


counter = 0
while True:
    draw_field()
    if counter%2 == 0:
        get_input('X')
    else:
        get_input('O')
    if counter > 3:
        winner = check_winner()
        if winner:
            draw_field()
            print(f"Победил {winner}")
            break
    counter += 1
    if counter > 8:
        print("Победила дружба!")
        break