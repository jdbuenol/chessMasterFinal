from tensorflow import keras
from q_network import Q_model
from chess import Board
from board_conversion import *
import numpy as np

board = Board()
white_player = Q_model(keras.models.load_model("./checkpoint17"))
black_player = Q_model(keras.models.load_model("./checkpoint16"))
turn = True

while(not board.is_game_over()):
    if(turn):
        turn = False
        p, v = white_player.predict([board])
        sorted_moves = np.sort(p)[-1]
        while(not num2move[np.where(p[0] == sorted_moves[-1])[0][0]] in list(board.legal_moves)):
            sorted_moves = np.delete(sorted_moves, -1)
        board.push(num2move[np.where(p[0] == sorted_moves[-1])[0][0]])
        print("W:", num2move[np.where(p[0] == sorted_moves[-1])[0][0]])
    else:
        turn = True
        p, v = black_player.predict([board])
        sorted_moves = np.sort(p)[-1]
        while(not num2move[np.where(p[0] == sorted_moves[0])[0][0]] in list(board.legal_moves)):
            sorted_moves = np.delete(sorted_moves, 0)
        board.push(num2move[np.where(p[0] == sorted_moves[0])[0][0]])
        print("B:", num2move[np.where(p[0] == sorted_moves[0])[0][0]])
    print(board)