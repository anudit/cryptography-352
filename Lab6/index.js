var path = require('path');
var express = require('express');

const crypto = require('crypto');
const alice = crypto.createDiffieHellman(512);

alice.generateKeys();

let key_exchange_arguments = {
    prime_number :null,
    primitive_root:null,
    x_of_a:null,
    y_of_a:null,
}

key_exchange_arguments.prime_number =alice.getPrime().toString('hex')
key_exchange_arguments.primitive_root=alice.getGenerator().toString('hex')
key_exchange_arguments.x_of_a = alice.getPrivateKey().toString('hex')
key_exchange_arguments.y_of_a = alice.getPublicKey().toString('hex')


app = express();

var http = require('http').Server(app);
var io = require('socket.io')(http);

var port = process.env.PORT || 80;
app.use(express.static(path.join(__dirname, 'public')));


app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

app.get('/keys', function(req, res){
  // console.log(key_exchange_arguments)
  res.json(key_exchange_arguments);

});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
});

http.listen(port, function(){
  console.log('listening on *:' + port);
});
