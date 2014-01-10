$('document').ready(function(){
	var msgInput = $('#msgInput');

	var socket = io.connect('http://localhost:4000'),
		conversation = $('#conversation');

	// on connection to server, ask for user's name with an anonymous callback
	socket.on('connect', function(){
		// call the server-side function 'adduser' and send one parameter (value of prompt)
		socket.emit('adduser', username);
	});

	// listener, whenever the server emits 'updatechat', this updates the chat body
	socket.on('updatechat', function (data) {
		if(data){
			if(data.type == 'server'){
				conversation.append('<div class="server_msg msg_box box-green"><b>'+data.message + '</b></div>');	
			}else if(data.type == 'client'){
				conversation.append('<div class="client_msg msg_box box-blue"><b>'+data.username + ':</b><div>' + msgParser.init(data.message) + '</div></div>');	
			}
			conversation.scrollTop(conversation[0].scrollHeight);
		}
		return;
	});

	// listener, whenever the server emits 'updateusers', this updates the username list
	socket.on('updateusers', function(data) {
		$('#users').empty();
		$.each(data, function(key, value) {
			$('#users').append('<div>' + key + '</div>');
		});
	});

	// when the client clicks SEND
	$('#chatsend').click( function() {
		var message = msgInput.val();
		if(message != ''){
			// tell server to execute 'sendchat' and send along one parameter
			socket.emit('sendchat', message);
			msgInput.val('');
		}
	});

	// when the client hits ENTER on their keyboard
	msgInput.keypress(function(e) {
		if(e.which == 13) {
			$(this).blur();
			$('#chatsend').click();
			msgInput.focus();
		}
	});

	$('.btnbar').on('click', 'li a', function(){
		var action = $(this).data('action');
		switch(action){
			case 'showSmileys':
				utils.showModal({'title':'Smileys', 'body': $('.smileys').show()});
				break;
			case 'showLink':
				var tag =  $(this).data('tag');
				utils.appendToMsg(tag);
				break;
		}
	});

	$('.modal-dialog .close').bind('click', function(){
		utils.hideModal();
	});
	$('.smileys li').bind('click', function(){
		var smiley = $(this).data('smiley');
		utils.appendToMsg(smiley);
	});
});

var utils = {
	/*Method to show the modal box*/
	showModal: function(config){
		var modal = $('.modal-dialog');
		modal.find('.modal-title').html(config.title);
		modal.find('.modal-body').html('').append(config.body);
		modal.show();
	},
	hideModal: function(){
		$('.modal-dialog').fadeOut();
		msgInput.focus();
	},
	/*Method to append anything to the msg box text*/
	appendToMsg: function(text){
		var msgInput = $('#msgInput');
		var message = msgInput.val();
			message = message + text;
			msgInput.val(message);
	}
}
