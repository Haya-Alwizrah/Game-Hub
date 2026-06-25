import random

class HexaPown:
    def __init__(self):
        self.reset()

    def reset(self):
        """
        Reset the game to its initial state.
        """
        self.board = [
            ["X", "X", "X"],
            [" ", " ", " "],
            ["O", "O", "O"]
        ]
        self.winner = None
        self.player = random.choice(["X", "O"])

    def _players_position(self) -> tuple[list[tuple], list[tuple]]:
        """
        Returns the positions of both players on the board.
        Returns:
            tuple: A tuple containing two lists, one for player X's positions and one for player O's positions.
        """
        x_position = []
        o_position = []
        for i, row in enumerate(self.board):
            for j, column in enumerate(row):
                if column == "X":
                    x_position.append((i,j))
                elif column == "O":
                    o_position.append((i,j))
        return x_position, o_position

    def _inside_board(self, i:int, j:int)-> bool:
        """
        Check if the given position is inside the board.
        Args:
            i (int): Row index.
            j (int): Column index.
            
        Returns:
            bool: True if the position is inside the board, False otherwise.
        """
        return 0 <= i < 3 and 0 <= j < 3

    def available_moves(self)-> dict[tuple, list[tuple]]:
        """
        Returns a dictionary of available moves for the current player.
        Returns:
            dict: A dictionary where keys are the positions of movable pieces and values are lists of available moves.
        """
        x_position, o_position = self._players_position()
        if self.player == "X":
            move_dirction = 1
            position = x_position
            enemy = "O"
        else:
            move_dirction = -1
            position = o_position
            enemy = "X"

        available_moves = {}

        for i,j in position:
            available_moves[(i,j)] = []

            new_i, new_j = i+move_dirction, j
            if self._inside_board(new_i, new_j) and self.board[new_i][new_j] == " ":
                available_moves[(i,j)].append((new_i, new_j))

            for z in (1,-1):
                new_i, new_j = i+move_dirction, j+z
                if self._inside_board(new_i, new_j) and self.board[new_i][new_j] == enemy:
                    available_moves[(i,j)].append((new_i, new_j))

            if len(available_moves[(i, j)]) == 0:
                del available_moves[(i, j)]

        return available_moves

    def _check_winner(self, available_moves: dict[tuple, list[tuple]]) -> str:
        """
        Check if there is a winner in the game.
        Args:
            available_moves (dict): A dictionary of available moves for the current player.
        Returns:
            str: The winner of the game, or None if there is no winner.
        """
        if "X" in self.board[2]:
            return "X"
        elif "O" in self.board[0]:
            return "O"
        elif len(available_moves) == 0:
            return "O" if self.player == "X"else "X"
        else:
            return None

    def move(self, from_pos: tuple[int, int], to_pos: tuple[int, int]) -> bool:
        """
        Move a piece from one position to another.
        Args:
            from_pos (tuple): The position of the piece to move.
            to_pos (tuple): The position to move the piece to.
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        available_moves = self.available_moves()

        if from_pos not in available_moves or to_pos not in available_moves[from_pos]:
            return False
    
        old_i , old_j = from_pos
        new_i , new_j = to_pos

        self.board[old_i][old_j] = " "
        self.board[new_i][new_j] = self.player

        self.player = "O" if self.player == "X" else "X"

        return True
    
    def get_state(self)-> dict:
        """
        Get the current state of the game.
        Returns:
            dict: A dictionary containing the current board, player, winner, and movable pieces.
        """
        available_moves = self.available_moves()
        winner = self._check_winner(available_moves)
        movable_pieces = [list(pos) for pos in available_moves.keys()]
        
        return {
            'board': self.board,
            'player': self.player,
            'winner': winner,
            'movable_pieces': movable_pieces
        }
    

# For testing in console -------------------------------------------------------------------
    def start(self):
        """ Start the game in console mode.
        This method runs a loop that continues until there is a winner.
        It prompts the user for input to make moves and displays the current state of the board.
        """
        self._print_board()
        while self.winner == None:
            
            available_moves = self.available_moves()
            self.winner = self._check_winner(available_moves)

            if self.winner != None:
                print(f"Player '{self.winner}' wins!")
            else:
                print(available_moves)
                from_row = int(input("from row: "))
                from_col = int(input("from col: "))
                to_row = int(input("to row: "))
                to_col = int(input("to col: "))
                self._move((from_row, from_col),(to_row, to_col))
                self._print_board()

    def _print_board(self):
        """
        Print the current state of the board to the console.
        """
        for i in self.board:
            print(i)

'''
Reflection:
What was the most challenging part?
- Integrating the game logic with the Flask

Which concept did you enjoy the most?
- Designing and implementing the logic for calculating available moves for each piece

What would you improve if you had more time?
- I would scale the project up to develop a Chess game
- Add option to play aganist AI with MinMax algorithm
'''