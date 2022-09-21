# Создайте программу для игры в ""Крестики-нолики"".

tictactoe = list(range(1,10))
def XsOs_board(tictactoe):
    for i in range(3):
        print ("|", tictactoe[0+i*3], "|", tictactoe[1+i*3], "|", tictactoe[2+i*3], "|")
def player_input(player_move):
    valid = False
    while not valid:
        player_tap = input("Определите " + player_move+"? ")
        try:
            player_tap = int(player_tap)
        except:
            print ("Некорректный ввод")
            continue
        if player_tap >= 1 and player_tap <= 9:
            if (str(tictactoe[player_tap-1]) not in "XO"):
                tictactoe[player_tap-1] = player_move
                valid = True
            else:
                print ("Это поле занято")
        else:
            print ("Некорректный ввод")
def check_win(tictactoe):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if tictactoe[each[0]] == tictactoe[each[1]] == tictactoe[each[2]]:
            return tictactoe[each[0]]
    return False
def main(tictactoe):
    counter = 0
    win = False
    while not win:
        XsOs_board(tictactoe)
        if counter % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(tictactoe)
            if tmp:
                print (tmp, "ПОБЕДА")
                win = True
                break
        if counter == 9:
            print ("Ничья")
            break
    XsOs_board(tictactoe)
main(tictactoe)