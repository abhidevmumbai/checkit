  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>api-gateway/static/js/utils.js at master · Snapstick/api-gateway</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="GZP2HQwSMW2coOV7NiRaqV9DfuFUp4BypSFTYUCMxcE=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-f70e4783e00fd4884a9e5e651a43933c9881caa8.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-0d31290d073dea4d8671e2b8c747629aeb074034.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-d76b58e749b52bc47a4c46620bf2c320fabe5248.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-67b55380cff8d6766b298e6935a3c1db7d5c6d5d.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="1212ad79754350a805cefbcd08a3dadf">

        <link data-pjax-transient rel='permalink' href='/Snapstick/api-gateway/blob/637fcc3c2d443c82ae319737d026a6624f11c55b/static/js/utils.js'>
    <meta property="og:title" content="api-gateway"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/Snapstick/api-gateway"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/d09815a34a4c2cd54a48992a5b192198?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="api-gateway - API Management Gateway for all Snapstick API offerings"/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="Snapstick/api-gateway"/>

    <meta name="description" content="api-gateway - API Management Gateway for all Snapstick API offerings" />

  <link href="https://github.com/Snapstick/api-gateway/commits/master.atom?login=abhishekdUI&token=045aa4532f8047dbc37444ba61c19845" rel="alternate" title="Recent Commits to api-gateway:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob linux vis-private env-production  ">
    <div id="wrapper">

      

      
      
      

      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-blacktocat" href="https://github.com/organizations/Snapstick">
  <span class="mega-icon mega-icon-blacktocat"></span>
</a>

    <div class="divider-vertical"></div>

    
  <a href="/notifications" class="notification-indicator tooltipped downwards" title="You have unread notifications">
    <span class="mail-status unread"></span>
  </a>
  <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  ">
            <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">
  <a href="/search/advanced" class="advanced-search-icon tooltipped downwards command-bar-search" id="advanced_search" title="Advanced search"><span class="mini-icon mini-icon-advanced-search "></span></a>

  <input type="text" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" data-username="abhishekdUI" autocapitalize="off">

  <span class="mini-icon help tooltipped downwards" title="Show command bar help">
    <span class="mini-icon mini-icon-help"></span>
  </span>

  <input type="hidden" name="ref" value="commandbar">

  <div class="divider-vertical"></div>
</form>
        <ul class="top-nav">
            <li class="explore"><a href="https://github.com/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="http://help.github.com">Help</a></li>
        </ul>
      </div>

    

  
    <ul id="user-links">
      <li>
        <a href="https://github.com/abhishekdUI" class="name">
          <img height="20" src="https://secure.gravatar.com/avatar/02555227dc56c02dd5251937d49f27f3?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /> abhishekdUI
        </a>
      </li>
      <li>
        <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo">
          <span class="mini-icon mini-icon-create"></span>
        </a>
      </li>
      <li>
        <a href="/settings/profile" id="account_settings"
          class="tooltipped downwards"
          title="Account settings ">
          <span class="mini-icon mini-icon-account-settings"></span>
        </a>
      </li>
      <li>
        <a href="/logout" data-method="post" id="logout" class="tooltipped downwards" title="Sign out">
          <span class="mini-icon mini-icon-logout"></span>
        </a>
      </li>
    </ul>



    
  </div>
</div>

      

      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              


<ul class="pagehead-actions">

    <li class="nspr">
      <a href="/Snapstick/api-gateway/pull/new/master" class="button minibutton btn-pull-request" icon_class="mini-icon-pull-request"><span class="mini-icon mini-icon-pull-request"></span>Pull Request</a>
    </li>

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="GZP2HQwSMW2coOV7NiRaqV9DfuFUp4BypSFTYUCMxcE=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="8599847" />

    <div class="select-menu js-menu-container js-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">
          <span class="mini-icon mini-icon-unwatch"></span>
          Unwatch
        </span>
      </span>

      <div class="select-menu-modal-holder js-menu-content">
        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container">

            <div class="select-menu-item js-navigation-item js-navigation-target ">
              <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="mini-icon mini-icon-watching"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item js-navigation-target selected">
              <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="mini-icon mini-icon-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item js-navigation-target ">
              <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="mini-icon mini-icon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

    <li class="js-toggler-container js-social-container starring-container ">
      <a href="/Snapstick/api-gateway/unstar" class="minibutton js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="mini-icon mini-icon-remove-star"></span>
        <span class="text">Unstar</span>
      </a>
      <a href="/Snapstick/api-gateway/star" class="minibutton js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="mini-icon mini-icon-star"></span>
        <span class="text">Star</span>
      </a>
      <a class="social-count js-social-count" href="/Snapstick/api-gateway/stargazers">0</a>
    </li>

        <li>
          <a href="/Snapstick/api-gateway/fork_select" class="minibutton js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="facebox nofollow">
            <span class="mini-icon mini-icon-branch-create"></span>
            <span class="text">Fork</span>
          </a>
          <a href="/Snapstick/api-gateway/network" class="social-count">0</a>
        </li>


</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title private">
                <span class="repo-label"><span>private</span></span>
                <span class="mega-icon mega-icon-private-repo"></span>
                <span class="author vcard">
                  <a href="/Snapstick" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">Snapstick</span>
                  </a></span> /
                <strong><a href="/Snapstick/api-gateway" class="js-current-repository">api-gateway</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li><a href="/Snapstick/api-gateway" class="selected" highlight="repo_source repo_downloads repo_commits repo_tags repo_branches">Code</a></li>
    <li><a href="/Snapstick/api-gateway/network" highlight="repo_network">Network</a></li>
    <li><a href="/Snapstick/api-gateway/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/Snapstick/api-gateway/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>

      <li><a href="/Snapstick/api-gateway/wiki" highlight="repo_wiki">Wiki</a></li>


    <li><a href="/Snapstick/api-gateway/graphs" highlight="repo_graphs repo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/Snapstick/api-gateway/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
    
  <div class="tabnav-widget search repo-search ">
    <form accept-charset="UTF-8" action="/Snapstick/api-gateway/search" method="get">
      <span class="fieldwrap">
        <input type="text" name="q" value=""
          placeholder="Search source code&hellip;" tabindex="2" autocapitalize="off" /><button type="submit" class="minibutton empty-icon"><span class="mini-icon mini-icon-search-input"></span></button>
      </span>
      <input type="hidden" id="lang-value" name="l" value="" />
      <input type="hidden" id="start-value" name="start" value="" />
</form>  </div>

  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="mini-icon mini-icon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item js-navigation-target selected">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/Snapstick/api-gateway/blob/master/static/js/utils.js" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <form accept-charset="UTF-8" action="/Snapstick/api-gateway/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-navigation-target js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="GZP2HQwSMW2coOV7NiRaqV9DfuFUp4BypSFTYUCMxcE=" /></div>

                <span class="mini-icon mini-icon-branch-create select-menu-item-icon"></span>
                <div class="select-menu-item-text">
                  <h4>Create branch: <span class="js-new-item-name"></span></h4>
                  <span class="description">from ‘master’</span>
                </div>
                <input type="hidden" name="name" id="name" class="js-new-item-submit" />
                <input type="hidden" name="branch" id="branch" value="master" />
                <input type="hidden" name="path" id="branch" value="static/js/utils.js" />
              </form> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/Snapstick/api-gateway" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/Snapstick/api-gateway/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/Snapstick/api-gateway/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:c4fd5491d3e4890289c68bbff1018db7 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:c4fd5491d3e4890289c68bbff1018db7 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Snapstick/api-gateway" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">api-gateway</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Snapstick/api-gateway/tree/master/static" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">static</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Snapstick/api-gateway/tree/master/static/js" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">js</span></a></span><span class="separator"> / </span><strong class="final-path">utils.js</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="static/js/utils.js" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
        </div>

      <a href="/Snapstick/api-gateway/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/Snapstick/api-gateway/contributors/master/static/js/utils.js">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif?1360648843" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>

    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/Snapstick/api-gateway/blob/637fcc3c2d443c82ae319737d026a6624f11c55b/static/js/utils.js" data-title="api-gateway/static/js/utils.js at master · Snapstick/api-gateway · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>87 lines (78 sloc)</span>
                <span>2.824 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                        <a class="minibutton"
                           href="/Snapstick/api-gateway/edit/master/static/js/utils.js"
                           data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
                  <a href="/Snapstick/api-gateway/raw/master/static/js/utils.js" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/Snapstick/api-gateway/blame/master/static/js/utils.js" class="button minibutton ">Blame</a>
                  <a href="/Snapstick/api-gateway/commits/master/static/js/utils.js" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="data type-javascript js-blob-data">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
</pre>
          </td>
          <td width="100%">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c1">//Utilities object consisting of generic methods</span></div><div class='line' id='LC2'><span class="kd">var</span> <span class="nx">utils</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC3'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c1">//Function to check if the javascript object is empty or not</span></div><div class='line' id='LC4'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">isEmpty</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">ob</span><span class="p">){</span></div><div class='line' id='LC5'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span><span class="p">(</span><span class="kd">var</span> <span class="nx">i</span> <span class="k">in</span> <span class="nx">ob</span><span class="p">){</span> <span class="k">if</span><span class="p">(</span><span class="nx">ob</span><span class="p">.</span><span class="nx">hasOwnProperty</span><span class="p">(</span><span class="nx">i</span><span class="p">)){</span><span class="k">return</span> <span class="kc">false</span><span class="p">;}}</span></div><div class='line' id='LC6'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="kc">true</span><span class="p">;</span></div><div class='line' id='LC7'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">},</span></div><div class='line' id='LC8'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">/*</span></div><div class='line' id='LC9'><span class="cm">    Function to do an AJAX form submit</span></div><div class='line' id='LC10'><span class="cm">    url -&gt; Form action, params -&gt; parameters, call_back -&gt; custom function</span></div><div class='line' id='LC11'><span class="cm">    */</span></div><div class='line' id='LC12'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">ajax_form_submit</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">url</span><span class="p">,</span> <span class="nx">params</span><span class="p">,</span> <span class="nx">call_back</span><span class="p">){</span></div><div class='line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">$</span><span class="p">.</span><span class="nx">post</span><span class="p">(</span><span class="nx">url</span><span class="p">,</span> <span class="nx">params</span><span class="p">,</span> <span class="nx">call_back</span><span class="p">)</span></div><div class='line' id='LC14'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">.</span><span class="nx">error</span><span class="p">(</span><span class="kd">function</span><span class="p">(</span><span class="nx">resp</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">console</span><span class="p">.</span><span class="nx">error</span><span class="p">(</span><span class="nx">resp</span><span class="p">.</span><span class="nx">responseText</span><span class="p">);</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">});</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">},</span></div><div class='line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">/*</span></div><div class='line' id='LC19'><span class="cm">    Function to slice any string</span></div><div class='line' id='LC20'><span class="cm">    stringObj = {&#39;string&#39;:&#39;target string&#39;,&#39;start&#39;:&#39;start position&#39;, &#39;limit&#39;:&#39;limit&#39;, &#39;space&#39;:&#39;flag to truncate from last space&#39;}</span></div><div class='line' id='LC21'><span class="cm">    */</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">sliceIt</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">stringObj</span><span class="p">){</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">string</span> <span class="o">=</span> <span class="nx">stringObj</span><span class="p">.</span><span class="nx">string</span><span class="p">;</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">start</span> <span class="o">=</span> <span class="nx">stringObj</span><span class="p">.</span><span class="nx">start</span><span class="p">;</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">limit</span> <span class="o">=</span> <span class="nx">stringObj</span><span class="p">.</span><span class="nx">limit</span><span class="p">;</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">space</span> <span class="o">=</span> <span class="nx">stringObj</span><span class="p">.</span><span class="nx">space</span><span class="p">;</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">ellipsis</span> <span class="o">=</span> <span class="nx">stringObj</span><span class="p">.</span><span class="nx">ellipsis</span><span class="p">;</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">ellipsis_str</span> <span class="o">=</span> <span class="s1">&#39;...&#39;</span><span class="p">;</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="o">!</span><span class="nx">string</span><span class="p">){</span> </div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s1">&#39;&#39;</span><span class="p">;</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="o">!</span><span class="nx">ellipsis</span><span class="p">){</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">ellipsis_str</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span><span class="p">;</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="nx">string</span><span class="p">.</span><span class="nx">length</span> <span class="o">&gt;</span> <span class="nx">limit</span><span class="p">){</span>            </div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="nx">space</span><span class="p">){</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">string</span> <span class="o">=</span> <span class="nx">string</span><span class="p">.</span><span class="nx">substr</span><span class="p">(</span><span class="nx">start</span><span class="p">,</span> <span class="nx">limit</span><span class="p">);</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">string</span> <span class="o">=</span> <span class="nx">string</span><span class="p">.</span><span class="nx">substr</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nx">string</span><span class="p">.</span><span class="nx">lastIndexOf</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="p">))</span> <span class="o">+</span> <span class="nx">ellipsis_str</span><span class="p">;</span><span class="c1">//Slices from last space in the string</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span><span class="k">else</span><span class="p">{</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">string</span> <span class="o">=</span> <span class="nx">string</span><span class="p">.</span><span class="nx">substr</span><span class="p">(</span><span class="nx">start</span><span class="p">,</span> <span class="nx">limit</span><span class="p">)</span> <span class="o">+</span> <span class="nx">ellipsis_str</span><span class="p">;</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nx">string</span><span class="p">;</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">},</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">encode_utf8</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">s</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nx">unescape</span><span class="p">(</span><span class="nb">encodeURIComponent</span><span class="p">(</span><span class="nx">s</span><span class="p">));</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">},</span></div><div class='line' id='LC49'><br/></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">decode_utf8</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">s</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">decodeURIComponent</span><span class="p">(</span><span class="nx">escape</span><span class="p">(</span><span class="nx">s</span><span class="p">));</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">},</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">/*</span></div><div class='line' id='LC55'><span class="cm">        Function to show Modal popup</span></div><div class='line' id='LC56'><span class="cm">        msg_options = {&#39;type&#39;:&#39;confirm&#39;, &#39;msg&#39;:&#39;Are you sure?&#39;}</span></div><div class='line' id='LC57'><span class="cm">    */</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">showModal</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">msg_options</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="nx">msg_options</span><span class="p">){</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">type</span> <span class="o">=</span> <span class="nx">msg_options</span><span class="p">.</span><span class="nx">type</span><span class="p">;</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">msg</span> <span class="o">=</span> <span class="nx">msg_options</span><span class="p">.</span><span class="nx">msg</span><span class="p">;</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="nx">msg_options</span><span class="p">.</span><span class="nx">data</span><span class="p">;</span></div><div class='line' id='LC63'><br/></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">modal_container</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#Modal&#39;</span><span class="p">);</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">modal_header</span> <span class="o">=</span> <span class="nx">modal_container</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.modal-header&#39;</span><span class="p">);</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">modal_label</span> <span class="o">=</span> <span class="nx">modal_header</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;#ModalLabel&#39;</span><span class="p">);</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">modal_body</span> <span class="o">=</span> <span class="nx">modal_container</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.modal-body&#39;</span><span class="p">);</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kd">var</span> <span class="nx">modal_footer</span> <span class="o">=</span> <span class="nx">modal_container</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.modal-footer&#39;</span><span class="p">);</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c1">//Modal message</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">modal_body</span><span class="p">.</span><span class="nx">html</span><span class="p">(</span><span class="s1">&#39;&lt;p&gt;&#39;</span><span class="o">+</span> <span class="nx">msg</span> <span class="o">+</span><span class="s1">&#39;&lt;/p&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">switch</span><span class="p">(</span><span class="nx">type</span><span class="p">){</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">case</span> <span class="s1">&#39;confirm&#39;</span><span class="o">:</span> </div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">modal_label</span><span class="p">.</span><span class="nx">html</span><span class="p">(</span><span class="s1">&#39;Confirm&#39;</span><span class="p">);</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">modal_footer</span><span class="p">.</span><span class="nx">html</span><span class="p">(</span><span class="s1">&#39;&lt;button class=&quot;btn&quot; data-dismiss=&quot;modal&quot; aria-hidden=&quot;true&quot;&gt;No&lt;/button&gt;&lt;a class=&quot;btn btn-primary delete_confirm&quot; href=&quot;&#39;</span><span class="o">+</span> <span class="nx">data</span><span class="p">.</span><span class="nx">url</span> <span class="o">+</span><span class="s1">&#39;&quot;&gt;Yes&lt;/a&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span><span class="p">;</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC79'><br/></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#Modal&#39;</span><span class="p">).</span><span class="nx">modal</span><span class="p">(</span><span class="s1">&#39;show&#39;</span><span class="p">);</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span><span class="k">else</span><span class="p">{</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span><span class="p">;</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC86'><span class="p">};</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1360648843" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.15657s from fe3.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/Snapstick/api-gateway/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-icon mega-icon-normalscreen"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="mini-icon mini-icon-brightness"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.15726' data-host='fe3'></span>
    
  </body>
</html>

