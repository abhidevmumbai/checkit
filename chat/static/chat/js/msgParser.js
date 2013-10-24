var smileyBaseURL = '/static/chat/images/smileys/'
var msgParser = {
    msg: '',
    init: function(text){
        this.msg = text;
        this.smileyParser(this.msg);
        this.linkParser(this.msg);
        return this.msg;
    },
    // regex: /([ \n\r\t]):D|:D([ \n\r\t])|(^):D($)/gm
    // regex: /([ \n\r\t]):wub:|:wub:([ \n\r\t])|(^):wub:($)/gm
    smileyParser: function(text){
        var set1 = [
            {
                image: '<img src="' +smileyBaseURL+ 'set1/angry no.gif" alt="Angry" border="0"/>',
                regex: /:x/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/bounce ball.gif" alt="Laugh" border="0"/>',
                regex: /:D/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/shock.gif" alt="" border="0"/>',
                regex: /:shock:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/my love.gif" alt="My love" border="0"/>',
                regex: /:wub:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/rolling on the floor laughing.gif" alt="Rolling on the floor laughing" border="0"/>',
                regex: /:rofl:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/tease.gif" alt="Tease" border="0"/>',
                regex: /:nanananana:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/thinking.gif" alt="Chin scratch" border="0"/>',
                regex: /:chinscratch:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/big laugh.gif" alt="Big laugh" border="0"/>',
                regex: /:lol:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/applause.gif" alt="Applause" border="0"/>',
                regex: /:clap:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/big hug.gif" alt="Big hug" border="0"/>',
                regex: /:hug:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/bla bla.gif" alt="Bla Bla" border="0"/>',
                regex: /:blabla:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/bored.gif" alt="Bored" border="0"/>',
                regex: /:bored:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/bye bye.gif" alt="Bye Bye" border="0"/>',
                regex: /:bye:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/call me.gif" alt="Call me" border="0"/>',
                regex: /:callme:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/cheer up.gif" alt="Cheer up" border="0"/>',
                regex: /:cheerup:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/cheers.gif" alt="Cheers" border="0"/>',
                regex: /:cheers:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/congrats.gif" alt="Congrats" border="0"/>',
                regex: /:congrats:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/cool.gif" alt="Cool" border="0"/>',
                regex: /:cool:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/disappointed.gif" alt="Disappointed" border="0"/>',
                regex: /:disappointed:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/good luck.gif" alt="Good luck" border="0"/>',
                regex: /:luck:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/good morning.gif" alt="Good morning" border="0"/>',
                regex: /:gm:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/good night.gif" alt="Good night" border="0"/>',
                regex: /:gn:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/hear ya.gif" alt="Hear ya" border="0"/>',
                regex: /:hear:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/hello, soldier.gif" alt="Hello, soldier" border="0"/>',
                regex: /:hs:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i don\'t know.gif" alt="I don\'t know" border="0"/>',
                regex: /:idk:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i hate you.gif" alt="I hate you" border="0"/>',
                regex: /:ihu:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i know.gif" alt="I know" border="0"/>',
                regex: /:ik:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i like you.gif" alt="I like you" border="0"/>',
                regex: /:ilk:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i love you too.gif" alt="I love you too" border="0"/>',
                regex: /:loveu2:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i love you.gif" alt="I love you" border="0"/>',
                regex: /:lu:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i miss you.gif" alt="I miss you" border="0"/>',
                regex: /:imu:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i\'m back.gif" alt="I\'m back" border="0"/>',
                regex: /:back:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i\'m mad as hell.gif" alt="I\'m mad as hell" border="0"/>',
                regex: /:mad:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i\'m so bored.gif" alt="I\'m so bored" border="0"/>',
                regex: /:bored:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/i\'m sorry.gif" alt="I\'m sorry" border="0"/>',
                regex: /:sorry:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/it\'s a beautiful thing.gif" alt="It\'s a beautiful thing" border="0"/>',
                regex: /:beautiful:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/it\'s about time.gif" alt="It\'s about time" border="0"/>',
                regex: /:abouttime:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/it\'s all good.gif" alt="It\'s all good" border="0"/>',
                regex: /:allgood:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/it\'s not fair.gif" alt="It\'s not fair" border="0"/>',
                regex: /:notfair:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/looser.gif" alt="Looser" border="0"/>',
                regex: /:looser:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/no.gif" alt="No" border="0"/>',
                regex: /:no:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/please.gif" alt="Please" border="0"/>',
                regex: /:please:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/welcome home.gif" alt="Welcome home" border="0"/>',
                regex: /:welcomehome:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/whatever.gif" alt="Whatever" border="0"/>',
                regex: /:whatever:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/you are welcome.gif" alt="You\'re welcome" border="0"/>',
                regex: /:welcome:/gm
            },{
                image: '<img src="' +smileyBaseURL+ 'set1/you rock.gif" alt="You rock" border="0"/>',
                regex: /:rock:/gm
            }
        ];
        var smileySet = set1;
        /* Smiley Parser */
        for (var i = smileySet.length - 1; i >= 0; --i){
            var modifiedText = undefined;
            while(1) {
                modifiedText = text.replace(smileySet[i].regex, smileySet[i].image);
                if(text == modifiedText) {
                    break;
                } else {
                    text = modifiedText;
                }
            }
        }
        this.msg = text;
    },

    linkParser: function(text){
        /*
            (
             ( # brackets covering match for protocol (optional) and domain
              ([A-Za-z]{3,9}:(?:\/\/)?)   # match protocol, allow in format http:// or mailto:
              (?:[\-;:&=\+\$,\w]+@)?   # allow something@ for email addresses
              [A-Za-z0-9\.\-]+   # anything looking at all like a domain, non-unicode domains
              | # or instead of above
              (?:www\.|[\-;:&=\+\$,\w]+@) # starting with something@ or www.
              [A-Za-z0-9\.\-]+   # anything looking at all like a domain
             )
             ( # brackets covering match for path, query string and anchor
              (?:\/[\+~%\/\.\w\-]*)  # allow optional /path
              ?\??(?:[\-\+=&;%@\.\w]*)  # allow optional query string starting with ? 
              #?(?:[\.\!\/\\\w]*) # allow optional anchor #anchor 
             )? # make URL suffix optional
            )
        */
        var regex =  /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-]*)?\??(?:[\-\+=&;%@\.\w]*)#?(?:[\.\!\/\\\w]*))?)/g,
            urls = text.match(regex),
            urlLen = urls ? urls.length : 0;
        if(urlLen > 0){
            for(var i=0; i<urlLen; i++){
                console.log(urls[i]);
                text = text.replace(urls[i], '<a href="' +urls[i]+ '" target="_blank">' +urls[i]+ '</a>');
            }
            this.msg = text;
        }
    }

}