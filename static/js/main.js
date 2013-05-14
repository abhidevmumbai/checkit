$(document).ready(function(){
    //Add this class to display tooltips on any element
    $('.tool_tip').tooltip();
    
    /*Game Delete button to show Delete confirmation*/
	$('.appDelbtn').bind('click', function(e){
		e.preventDefault;
		var url = $(this).data('url');
		utils.showModal({'type':'confirm', 'msg':'Are you sure you want to delete this app?', 'data':{'url': url}});
	});

    /*Game Delete button to Delete app*/
    $('#Modal').on('click', '.delete_confirm', function(e){
    	e.preventDefault();
    	var url = $(this).attr('href');
        $.ajax({
            url: url,
            type: "GET",
            success: function(response){
                var csrf_token = JSON.parse(response).csrf_token;
                console.log(csrf_token);
                $.ajax({
                    url: url,
                    type: "POST",
                    headers: {"X-CSRFToken": csrf_token},                          
                    success: function(response){
                        console.log('Entry deleted.');
                        //$('#delete_confirm').modal('hide');
                        window.location.reload();
                    }
                });   
            }
        });
    });
    switchWallpapers();
});

function switchWallpapers(){
    var splash = $('.splash_view .splash'),
        len = 4,
        wall_no = 2;
    setInterval(function(){
        splash.animate({opacity: 0}, 'slow', function() {
            $(this).css({'background-image': 'url(../static/img/splash/collage'+ wall_no +'.jpg)'}).animate({opacity: 1});
            if(wall_no < len){
                wall_no++;
            }else{
                wall_no = 1;
            }
        });
    }, 5000);
}