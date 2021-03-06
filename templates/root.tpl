<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>

<div class="d-flex flex-column justify-content-center text-center">
<div>
<img src="https://raw.githubusercontent.com/jdbuenol/ChessMaster/main/docs/chess.png" style="width:300px">
</div>
<div>
<p class="display-2">ChessMaster the invincible AI</p>
</div>
<form action="/new" method="post" class="my-3">
    <b>Start a new Game:</b>
    <input type="submit" value="New Game" class="btn btn-dark" />
</form>
<form action="/upload" method="post" enctype="multipart/form-data" class="my-3">
    <b>Select a file: </b> <input type="file" name="upload"/>
    <input type="submit" value="Start upload" class="btn btn-dark" />
</form>
</div>