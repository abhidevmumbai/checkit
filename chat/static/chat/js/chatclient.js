

$('document').ready(function(){
	var msgInput = $('#msgInput'),
		conversation = $('#conversation');

	var ws = new WebSocket("ws://127.0.0.1:8080/");

	// on connection to server, ask for user's name with an anonymous callback
	ws.onopen = function(event) {
	  // The connection was opened
	  // call the server-side function 'adduser' and send one parameter (value of prompt)
	  var msg = {
		  	from: "client",
		  	type: "adduser",
		  	message: username
		};
	  ws.send(JSON.stringify(msg));
	}; 
	ws.onclose = function(event) { 
	  // The connection was closed
	  conversation.append('<div class="server_msg msg_box box-green"><b>'+event.data + '</b></div>');
	}; 
	ws.onmessage = function(event) {
		// New message arrived
		var data = JSON.parse(event.data);
		if(data){
			switch(data.type) {
				// listener, whenever the server emits 'updatechat', this updates the chat body
				case "updatechat":
					if(data.from == 'server'){
						conversation.append('<div class="server_msg msg_box box-green"><b>'+data.message + '</b></div>');	
					}else if(data.from == 'client'){
						conversation.append('<div class="client_msg msg_box box-blue"><b>'+data.username + ':</b><div>' + msgParser.init(data.message) + '</div></div>');	
					}
					break;

				// listener, whenever the server emits 'updateusers', this updates the username list
				case "updateusers":
					$('#users').empty();
					$.each(data.message, function(key, value) {
						$('#users').append('<div>' + value + '</div>');
					});
					break;
			}

			conversation.scrollTop(conversation[0].scrollHeight);
		}
		return;
	}; 
	ws.onerror = function(event) { 
	  // There was an error with your WebSocket
	  conversation.append('<div class="server_msg msg_box box-green"><b>'+event.data + '</b></div>');
	};
	
	// when the client clicks SEND
	$('#chatsend').click( function() {
		var message = msgInput.val();
		if(message != ''){
			// tell server to execute 'sendchat' and send along one parameter
			var msg = {
				from: "client",
				type: "sendchat",
				message: message
			}
			ws.send(JSON.stringify(msg));
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
