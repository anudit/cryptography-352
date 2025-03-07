var path = require('path');
var express = require('express');
app = express();

var http = require('http').Server(app);
var io = require('socket.io')(http);

var port = process.env.PORT || 80;
app.use(express.static(path.join(__dirname, 'public')));


app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
});

http.listen(port, function(){
  console.log('listening on *:' + port);
});
