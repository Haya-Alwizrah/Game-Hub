from games.hangman import HangmanGame
from games.wordle import Wordle
#from guessing_number import GuessingNumberGame
from games.hexapown import HexaPown
from games.tic_tac_toe import TicTacToe

hg = HangmanGame()
wo = Wordle()
#gn = GuessingNumberGame()
hp = HexaPown()
ttt = TicTacToe()

print("Welcome to the game hub")

while True:
    print("choose from the menu: (1,2) type 'exit' to exit the game hub")
    print("1) Single PLayer Games\n2) TwoPlayers Games")
    x = input()

    if x.isdigit():
        x = int(x)
        if x == 1:
            print("Choose from the menu:")
            print("1) Hangman\n2) Wordle\n3) Guessing Number" )
            y = int(input())
            if y == 1:
                hg.start()
            elif y == 2:
                wo.start()
            elif y == 3:
                #gn.start()
                pass
            else:
                print("Invalid Input")

        elif x == 2:
            print("Choose from the menu:")
            print("1) HexaPown\n2) Tic Tac Toe")
            z = int(input())
            if z == 1:
                hp.start()
            elif z == 2:
                ttt.start()
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")

    elif x.lower() == 'exit':
        print("Exiting the game hub")
        break
    else:
        print("Invalid Input")