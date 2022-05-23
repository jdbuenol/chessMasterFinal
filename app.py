from bottle import route, run, template, request
from Iteracion6.recognize import predict_chessboard
from Iteracion2.iteracion2 import predict_best_move
from Iteracion5.main import play_against_nn
from tensorflow.keras import models
import os
import io

@route('/')
def index():
    return template('./templates/root.tpl')

@route('/upload', method='POST')
def do_upload():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'
    file = upload.file
    model = models.load_model('./Iteracion6/nn/model.tf')
    FEN = predict_chessboard(io.BufferedReader(file), model, {})
    return template('./templates/image.tpl', fen=FEN, bm="")
    #return 'OK ' + predict_chessboard(io.BufferedReader(file), model, {})

@route('/new', method='POST')
@route('/new')
def new_game():
  FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
  return template('./templates/image.tpl', fen=FEN, bm="")

@route('/best', method='POST')
def predict_best():
    player = request.forms['player']
    depth = request.forms['depth']
    FEN = request.forms['fen']
    best_move = predict_best_move(FEN, player, int(depth))
    return template('./templates/image.tpl', fen=FEN, bm=best_move)

@route('/nn', method='POST')
def fight_nn():
    player = request.forms['player']
    FEN = request.forms['fen']
    model = request.forms['model']
    move = request.forms['move']
    FEN, moves = play_against_nn(FEN, model, player, move)
    return template('./templates/image.tpl', fen=FEN, bm=moves)

print("App is running at: http://localhost:8081/")
run(host='localhost', port=8081)