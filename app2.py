from flask import Flask, jsonify, request, render_template
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

app = Flask(__name__)

# ------------------------------------------[ home ]-----------------------------------------------------------
@app.route('/')
def home():
    return render_template('home.html')

# ------------------------------------------[ category ]-----------------------------------------------------------
@app.route('/singleplayer')
def singleplayer():
    games = [
        {
            'name': 'HangmanGame',
            'url': '/HangmanGame'
        },
        {
            'name': 'Wordle',
            'url': '/Wordle'
        },
        {
            'name': 'GuessingNumberGame',
            'url': '/GuessingNumberGame'
        }
    ]
    return render_template('category.html', title='Single Player Games', games=games)

@app.route('/multiplayer')
def multiplayer():
    games = [
        {
            'name': 'HexaPown',
            'url': '/hexapown'
        },
        {
            'name': 'TicTacToe',
            'url': '/TicTacToe'
        }
    ]
    return render_template('category.html', title='Two Player Games', games=games)

# ------------------------------------------[ Games ]-----------------------------------------------------------

@app.route('/HangmanGame')
def hangman():
    return render_template('hangman.html')

@app.route('/Wordle')
def wordle():
    return render_template('wordle.html')

@app.route('/GuessingNumberGame')
def guessing_number():
    return render_template('guessing_number.html')

@app.route('/hexapown')
def hexapown():
    return render_template('hexapown.html')

@app.route('/TicTacToe')
def tictactoe():
    return render_template('tictactoe.html')