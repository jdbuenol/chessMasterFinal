from tensorflow import keras
from Iteracion5.q_network import Q_model
from Iteracion5.chess_env import *
from Iteracion5.board_conversion import *
import numpy as np
import chess

def play_against_nn(FEN, model, player, move):
    env = ChessEnv()
    env.board = chess.Board(FEN + " " + player + " KQkq - 0 1")
    bm = ""
    try:
        player_move = chess.Move.from_uci(move)
        if(not player_move in list(env.board.legal_moves)):
            return FEN, "Invalid move"
        env.board.push(player_move)
    except:
        return FEN, "Invalid move"
    q_model= Q_model(keras.models.load_model("./Iteracion5/" + model))
    p, v = q_model.predict([env.board])
    sorted_moves = np.sort(p)[-1]
    if player == 'b':
        while(not num2move[np.where(p[0] == sorted_moves[-1])[0][0]] in list(env.board.legal_moves)):
            sorted_moves = np.delete(sorted_moves, -1)
        nn_move = num2move[np.where(p[0] == sorted_moves[-1])[0][0]]
    else:
        while(not num2move[np.where(p[0] == sorted_moves[0])[0][0]] in list(env.board.legal_moves)):
            sorted_moves = np.delete(sorted_moves, 0)
        nn_move = num2move[np.where(p[0] == sorted_moves[0])[0][0]]
    env.board.push(nn_move)
    return env.board.fen().split(' ')[0], f"Player moved {str(player_move)} - NN moved {str(nn_move)}"

'''
env = ChessEnv()
q_model = Q_model(keras.models.load_model("./checkpoint3"))

p, v = q_model.predict([env.board])

best_move = np.argmax(p, axis=None)
move = num2move[best_move]
print("BEST_MOVE:", move) 
'''