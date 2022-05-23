<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>

<div class="d-flex flex-column justify-content-center text-center">
<div>
<img src="https://raw.githubusercontent.com/jdbuenol/ChessMaster/main/docs/chess.png" style="width:300px">
</div>
<div>
<p class="display-2">ChessMaster the invincible AI</p>
</div>
<div>
%if bm != "":
<div>{{bm}}</div>
%end
<img src="http://fen-to-image.com/image/32/{{fen}}">
</div>
<div class="d-flex justify-content-center text-center my-2" style="gap: 100px;">
<div class="d-flex flex-column">
<p class="display-6">PREDICT BEST MOVE</p>
<form action="/best" method="post" class="my-3 form-group">
    <label for="player">Whose turn is it?</label>
    <select name="player" id="player" class="form-control my-2">
    <option value="w">WHITE</option>
    <option value="b">BLACK</option>
    </select>
    <label for="depth">Depth of predict (5 recommended, more could take a few minutes)</label>
    <input class="form-control my-2" type="number" step="1" placeholder="5" name="depth" id="depth">
    <input type="text" class="d-none" name="fen" id="fen" value="{{fen}}">
    <button class="my-2 btn btn-dark">PREDICT</button>
</form>
</div>
<div>
<p class="display-6">FIGHT AGAINST A NN</p>
</div>
</div
</div>