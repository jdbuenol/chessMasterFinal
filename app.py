from bottle import route, run, template, request
from Iteracion6.recognize import predict_chessboard
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
    return template('./templates/image.tpl', fen=FEN)
    #return 'OK ' + predict_chessboard(io.BufferedReader(file), model, {})

@route('/new', method='POST')
def new_game():
  FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
  return template('./templates/image.tpl', fen=FEN)

print("App is running at: http://localhost:8081/")
run(host='localhost', port=8081)