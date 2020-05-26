
def draw_board(char_list):
    print("\n\tTic-Tac-Toe")
    print("\t--------------")
    print("\t||"+" "+char_list[0] +" "+ "||"+char_list[1]+" "+ "||" +char_list[2]+"||")
    print("\t--------------")
    print("\t||"+" "+char_list[3] +" "+ "||"+char_list[4]+" "+ "||" +char_list[5]+"||")
    print("\t--------------")
    print("\t||"+" "+char_list[6] +" "+ "||"+char_list[7]+" "+ "||" +char_list[8]+"||")
    print("\t--------------")


def get_player_input(player_char, char_list):
    while True:
        player_move = int(input(player_char +":" + "Where would you like to place your piece (1-9): "))
        if(player_move>0 and player_move<10):
            if char_list[player_move - 1] == '_' :
                return player_move
            else:
                print("That spot has already been chosen.  Try again.")
        else:
            print("That is not a spot on the oard. Try again.")


            

    








player1 = 'X'
player2 = 'Y'
n_list = ['1','2','3','4','5','6','7','8','9']
c_list = ['_']*8
c_list.append('O')


draw_board(c_list)
draw_board(n_list)
move = get_player_input(player1,c_list)
print(move)