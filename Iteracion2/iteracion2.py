import chess

#Diccionario de valores materiales
white_dictionary = {
    "P" : 10, # Peon blanco
    "N" : 30, # Caballo blanco
    "B" : 30, # Alfil blanco
    "R" : 50, # Torre blanco
    "Q" : 90, # Reina blanco
    "K" : 900, # Rey blanco
    "p" : -10, # Peon negro
    "n" : -30, # Caballo negro
    "b" : -30, # Alfil negro
    "r" : -50, # Torre negra
    "q" : -90, # Reina negra
    "k" : -900 # Rey negro
}

# Ahora vamos a tener una matriz por cada ficha dónde tiene sus pesos, o sea en qué parte del tablero tiene mas valor.

# Matrices de valores
positions_dictionary = {
    "P" : [0, 0, 0, 0, 0, 0, 0, 0,
        5, 5, 5, 5, 5, 5, 5, 5,
        1, 1, 2, 3, 3, 2, 1, 1,
        0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5,
        0, 0, 0, 2, 2, 0, 0, 0,
        0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5,
        0.5, 1, 1, -2, -2, 1, 1, 0.5,
        0, 0, 0, 0, 0, 0, 0, 0],

    "N" : [-5, -4, -3, -3, -3, -3, -4, -5,
        -4, -2, 0, 0, 0, 0, -2, -4,
        -3, 0, 1, 1.5, 1.5, 1, 0, -3,
        -3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3,
        -3, 0, 1.5, 2, 2, 1.5, 0, -3,
        -3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3,
        -4, -2, 0, 0.5, 0.5, 0, -2, -4,
        -5, -4, -3, -3, -3, -3, -4, -5],

    "B" : [-2, -1, -1, -1, -1, -1, -1, -2,
        -1, 0, 0, 0, 0, 0, 0, -1,
        -1, 0, 0.5, 1, 1, 0.5, 0, -1,
        -1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1,
        -1, 0, 1, 1, 1, 1, 0, -1,
        -1, 1, 1, 1, 1, 1, 1, -1,
        -1, 0.5, 0, 0, 0, 0, 0.5, -1,
        -2, -1, -1, -1, -1, -1, -1, -2],

    "R" : [0, 0, 0, 0, 0, 0, 0, 0,
        0.5, 1, 1, 1, 1, 1, 1, 0.5,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        0, 0, 0, 0.5, 0.5, 0, 0, 0],

    "Q" : [-2, -1, -1, -0.5, -0.5, -1, -1, -2,
        -1, 0, 0, 0, 0, 0, 0, -1,
        -1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1,
        -0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5,
        0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5,
        -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1,
        -1, 0, 0.5, 0, 0, 0, 0, -1,
        -2, -1, -1, -0.5, -0.5, -1, -1, 2],
        
    "K" : [-3, -4, -4, -5, -5, -4, -4, -3,
        -3, -4, -4, -5, -5, -4, -4, -3,
        -3, -4, -4, -5, -5, -4, -4, -3,
        -3, -4, -4, -5, -5, -4, -4,  -3,
        -2, -3, -3, -4, -4, -3, -3, -2, 
        -1, -2, -2, -2, -2, -2, -2, -1, 
        2, 2, 0, 0, 0, 0, 2, 2, 
        2, 3, 1, 0, 0, 1, 3, 2],
    "p" : [0, 0, 0, 0, 0, 0, 0, 0,
        0.5, 1, 1, -2, -2, 1, 1, 0.5,
        0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5,
        0, 0, 0, 2, 2, 0, 0, 0,
        0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5,
        1, 1, 2, 3, 3, 2, 1, 1,
        5, 5, 5, 5, 5, 5, 5, 5,
        0, 0, 0, 0, 0, 0, 0, 0],
    "n" : [-5, -4, -3, -3, -3, -3, -4, -5,
        -4, -2, 0, 0.5, 0.5, 0, -2, -4,
        -3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3,
        -3, 0, 1.5, 2, 2, 1.5, 0, -3,
        -3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3,
        -3, 0, 1, 1.5, 1.5, 1, 0, -3,
        -4, -2, 0, 0, 0, 0, -2, -4,
        -5, -4, -3, -3, -3, -3, -4, -5],
    "b" : [-2, -1, -1, -1, -1, -1, -1, -2,
        -1, 0.5, 0, 0, 0, 0, 0.5, -1,
        -1, 1, 1, 1, 1, 1, 1, -1,
        -1, 0, 1, 1, 1, 1, 0, -1,
        -1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1,
        -1, 0, 0.5, 1, 1, 0.5, 0, -1,
        -1, 0, 0, 0, 0, 0, 0, -1,
        -2, -1, -1, -1, -1, -1, -1, -2],
    "r" : [0, 0, 0, 0.5, 0.5, 0, 0, 0,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        -0.5, 0, 0, 0, 0, 0, 0, -0.5,
        0.5, 1, 1, 1, 1, 1, 1, 0.5,
        0, 0, 0, 0, 0, 0, 0, 0],
    "q" : [-2, -1, -1, -0.5, -0.5, -1, -1, 2,
        -1, 0, 0, 0, 0, 0.5, 0, -1,
        -1, 0, 0.5, 0.5, 0.5, 0.5, 0.5, -1,
        -0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, 0,
        -0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5,
        -1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1,
        -1, 0, 0, 0, 0, 0, 0, -1,
        -2, -1, -1, -0.5, -0.5, -1, -1, -2],
    "k" : [2, 3, 1, 0, 0, 1, 3, 2,
        2, 2, 0, 0, 0, 0, 2, 2,
        -1, -2, -2, -2, -2, -2, -2, -1,
        -2, -3, -3, -4, -4, -3, -3, -2,
        -3, -4, -4, -5, -5, -4, -4,  -3,
        -3, -4, -4, -5, -5, -4, -4, -3,
        -3, -4, -4, -5, -5, -4, -4, -3,
        -3, -4, -4, -5, -5, -4, -4, -3]
}

# Esta función evalua cual es la posición actual del tablero.

def evaluate_position(board):
    FEN = board.fen().split(" ")[0]
    board_value = 0
    current_position = 0
    for x in FEN:
        if x in white_dictionary:
            board_value += white_dictionary[x]
            if x in ['r', 'b', 'n', 'p', 'k', 'q']:
                board_value -= positions_dictionary[x][current_position]
            else:
                board_value += positions_dictionary[x][current_position]
            current_position += 1
        elif x == '/':
            pass
        else:
            current_position += int(x)
    return board_value

# La siguiente función contiene el algoritmo min max que es la que nos devolverá el movimiento con el minimo costo, o sea el que más nos beneficiará.

def mini_max(board, depth, max_depth, white, alpha, beta):
    if depth > max_depth:
        print("OOPS! SOMETHING WENT WRONG")
        exit()
    if depth == max_depth:
        return evaluate_position(board)
    current_best_move = ""
    if white:
        current_best_move_value = -10000
        for possible_move in list(board.legal_moves):
            board.push_uci(str(possible_move))
            move_value = mini_max(board, depth + 1, max_depth, not white, alpha, beta)
            if move_value > current_best_move_value:
                current_best_move_value = move_value
                current_best_move = str(possible_move)
            board.pop()
            if move_value > alpha:
                alpha = move_value
            if beta <= alpha:
                break
    else:
        current_best_move_value = 10000
        for possible_move in list(board.legal_moves):
            board.push_uci(str(possible_move))
            move_value = mini_max(board, depth + 1, max_depth, not white, alpha, beta)
            if move_value < current_best_move_value:
                current_best_move_value = move_value
                current_best_move = str(possible_move)
            board.pop()
            if move_value < beta:
                beta = move_value
            if beta <= alpha:
                break

    if depth == 0:
        return current_best_move
    else:
        return current_best_move_value

'''

Ahora si la ejecución principal del servicio.

Ejemplos de movimientos validos:
-d2d4
-e2e3
-f1b5
-b5c6

'''
def predict_best_move(FEN, player, depth):
    board = chess.Board(FEN + ' ' + player + ' KQkq - 0 1')
    best_move = mini_max(board, 0, depth, player=="w", -10000, 10000)
    return "Your best move is " + str(best_move)