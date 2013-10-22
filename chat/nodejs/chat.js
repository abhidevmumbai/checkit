var port = 4000;
var http = require('http');
var server = http.createServer().listen(port);
var io = require('socket.io').listen(server);
var cookie_reader = require('cookie');
var querystring = require('querystring');
var usernames = {};

var redis = require('socket.io/node_modules/redis');
var sub = redis.createClient();

//Subscribe to the Redis chat channel
sub.subscribe('chat');

//Configure socket.io to store cookie set by Django
io.configure(function(){
    io.set('authorization', function(data, accept){
        if(data.headers.cookie){
            data.cookie = cookie_reader.parse(data.headers.cookie);
            return accept(null, true);
        }
        return accept('error', false);
    });
    io.set('log level', 1);
});

io.sockets.on('connection', function (socket) {
    
    //Grab message from Redis and send to client
    sub.on('message', function(channel, message){
        socket.send(message);
    });
    
    socket.emit('updatechat', {'type':'server', 'message': 'Welcome to Node chat!!!'});
    
    // when the client emits 'sendchat', this listens and executes
    socket.on('sendchat', function(data){
        // we tell the client to execute 'updatechat' with 2 parameters
        io.sockets.emit('updatechat', {'type':'client', 'username': socket.username, 'message': data});
    });

    //When the client emits 'adduser', this listens and executes
    socket.on('adduser', function(username){
        // we store the username in the socket session for this client
        socket.username = username;
        // add the client's username to the global list
        usernames[username] = username;
        // echo to client they've connected
        socket.emit('updatechat', {'type': 'server', 'message': 'you have connected'});
        // echo globally (all clients) that a person has connected
        socket.broadcast.emit('updatechat', {'type':'server', 'message': username + ' has connected'});
        // update the list of users in chat, client-side
        io.sockets.emit('updateusers', usernames);
    });

    // when the user disconnects.. perform this
    socket.on('disconnect', function(){
        // remove the username from global usernames list
        delete usernames[socket.username];
        // update list of users in chat, client-side
        io.sockets.emit('updateusers', usernames);
        // echo globally that this client has left
        socket.broadcast.emit('updatechat', {'type':'server', 'message': socket.username + ' has disconnected'});
    });

    
});
