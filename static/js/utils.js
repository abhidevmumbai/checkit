//Utilities object consisting of generic methods
var utils = {
    //Function to check if the javascript object is empty or not
    isEmpty: function(ob){
       for(var i in ob){ if(ob.hasOwnProperty(i)){return false;}}
      return true;
    },
    /*
    Function to do an AJAX form submit
    url -> Form action, params -> parameters, call_back -> custom function
    */
    ajax_form_submit: function(url, params, call_back){
        $.post(url, params, call_back)
            .error(function(resp) {
                console.error(resp.responseText);
            });
    },
    /*
    Function to slice any string
    stringObj = {'string':'target string','start':'start position', 'limit':'limit', 'space':'flag to truncate from last space'}
    */
    sliceIt: function(stringObj){
        var string = stringObj.string;
        var start = stringObj.start;
        var limit = stringObj.limit;
        var space = stringObj.space;
        var ellipsis = stringObj.ellipsis;
        var ellipsis_str = '...';
        if(!string){ 
            return '';
        }
        if(!ellipsis){
            ellipsis_str = '';
        }
        if(string.length > limit){            
            if(space){
                string = string.substr(start, limit);
                string = string.substr(0,string.lastIndexOf(' ')) + ellipsis_str;//Slices from last space in the string
            }else{
                string = string.substr(start, limit) + ellipsis_str;
            }
        }
        return string;
    },

    encode_utf8: function(s) {
        return unescape(encodeURIComponent(s));
    },

    decode_utf8: function(s) {
        return decodeURIComponent(escape(s));
    },

    /*
        Function to show Modal popup
        msg_options = {'type':'confirm', 'msg':'Are you sure?'}
    */
    showModal: function(msg_options) {
        if(msg_options){
            var type = msg_options.type;
            var msg = msg_options.msg;
            var data = msg_options.data;

            var modal_container = $('#Modal');
            var modal_header = modal_container.find('.modal-header');
            var modal_label = modal_header.find('#ModalLabel');
            var modal_body = modal_container.find('.modal-body');
            var modal_footer = modal_container.find('.modal-footer');

            //Modal message
            modal_body.html('<p>'+ msg +'</p>');

            switch(type){
                case 'confirm': 
                    modal_label.html('Confirm');
                    modal_footer.html('<button class="btn" data-dismiss="modal" aria-hidden="true">No</button><a class="btn btn-primary delete_confirm" href="'+ data.url +'">Yes</a>');
                break;
            }

            $('#Modal').modal('show');
        }else{
            return;
        }
        
    },

    /*
        Function to get all the query string params
    */
    getUrlVars: function(){
        var vars = [], map;
        var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
        for(var i = 0; i < hashes.length; i++){
            map = hashes[i].split('=');
            vars[map[0]] = map[1];       
        }
        return vars;
    },

    /*
        Function to get query string params by name
    */
    getUrlVar: function(name){
        return this.getUrlVars()[name];
    }
};
