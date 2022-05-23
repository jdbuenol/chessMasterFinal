import chess

board =  chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')

print(board.fen().split(' ')[0])