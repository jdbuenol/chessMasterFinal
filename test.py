import chess

board =  chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b')

print(list(board.legal_moves)[0])