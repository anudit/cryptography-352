var socket = null;
var crypt = null;

window.onload = async (event) => {

    crypt = new JSEncrypt({ default_key_size: 512 })

    document.querySelector('#privateKey').value = crypt.getPrivateKey()
    document.querySelector('#publicKey').value = crypt.getPublicKey()

    socket = io();

    $('form').submit(function(e){
        if (e){
            e.preventDefault();
        }
        let msg = document.querySelector('#msg').value;
        let rpc = document.querySelector('#recPublicKey').value;
        if (msg == ''){
            alert('Empty Message');
        }
        else if (rpc == ''){
            alert('Empty Receiver Public Key');
        }
        else{
            socket.emit('chat message', enc(rpc, msg));
        }

    });

    socket.on('chat message', function(msg){

        $('#messages').append($('<li>').text(dec(msg)));
        window.scrollTo(0, document.body.scrollHeight);

    });


};

function enc(_key, _msg ){
    var r = new JSEncrypt();
    r.setPrivateKey(_key);
    return r.encrypt(_msg);
}

function dec(_msg){
    return crypt.decrypt(_msg);
}
