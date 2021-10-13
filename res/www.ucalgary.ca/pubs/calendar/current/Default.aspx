<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

  <title>404 - Page Not Found | University of Calgary</title>
  
  <link href="//static.ucalgary.ca/current/global/styles/level-a.css" rel="stylesheet" type="text/css" />
  <link href="//static.ucalgary.ca/current/global/styles/print.css" rel="stylesheet" type="text/css" media="print" />
  
  <script src="//static.ucalgary.ca/current/global/libraries/jquery/jquery-1.11.2.min.js"></script>
  <script type="text/javascript" src="//static.ucalgary.ca/current/global/libraries/modernizr/modernizr.svg.js"></script>
  <script type="text/javascript" src="//static.ucalgary.ca/current/global/libraries/svg-png-polyfill/svgpng.js"></script>

  <script type="text/javascript" src="//static.ucalgary.ca/current/global/scripts/css_browser_selector.js"></script>
  <script type="text/javascript" src="//static.ucalgary.ca/current/global/scripts/uofc.js"></script>
    
  <!--[if IE 6]><link href="//static.ucalgary.ca/current/global/styles/ie/ie6.css" rel="stylesheet" type="text/css" /><![endif]-->
  <!--[if IE 7]><link href="//static.ucalgary.ca/current/global/styles/ie/ie7.css" rel="stylesheet" type="text/css" /><![endif]-->
  <!--[if IE 8]><link href="//static.ucalgary.ca/current/global/styles/ie/ie8.css" rel="stylesheet" type="text/css" /><![endif]-->

  <style type="text/css">

    #oops {
      width: 725px;
      height: 400px;
      position: relative;
      margin: 20px auto;
    }

    #oops #sorry {
      width: 370px;
      position: absolute;
      bottom: 0px; left: 0px;
    }

    #oops #sorry h1 {
      margin: 0;
      color: #e30c00;
      font: bold 60pt 'Proxima Nova',Arial,Helvetica,sans-serif;
      letter-spacing: 6px;
      border-bottom: none;
    }

    #oops #sorry p, #oops #sorry a {
      font: normal 12pt 'Proxima Nova Light',Arial,Helvetica,sans-serif;
    }

    #oops #sorry ul, #oops #sorry li {
      padding: 0;
      margin: 0 0 0 10px;
      font: normal 12pt 'Proxima Nova Light',Arial,Helvetica,sans-serif;
    }

    #oops #sorry a {
      text-decoration: none;
    }

    #oops #sorry a:hover {
      text-decoration: underline;
    }

    #oops #sorry p.alldinos {
      color: #e30c00;
      font: bold 13pt 'Proxima Nova',Arial,Helvetica,sans-serif;
    }

    #oops #rexosaurus {
      width: 335px;
      height: 400px;
      position: absolute;
      bottom: 0px; right: 0px;
      background: url('//static.ucalgary.ca/current/404/images/rexosaurus.jpg');
    }

    #oops #rexosaurus.hovered {
      background-position: -335px 0;
    }

  </style>

  <script type="text/javascript">
  //<![CDATA[

    (function($){
      $(document).ready(function() {

        // Update the user's options list
        if (document.referrer!="") {
          $('#options').prepend('<li>Returning to your <a id="back">previous</a> website location.</li>');
          $("#back").css("cursor","pointer").click(function() {
            parent.history.back();
          });
        }

        // Test for audio support and modify accordingly
        var audioTagSupport = !!(document.createElement('audio').canPlayType);
        if (audioTagSupport) {
          // Audio support available so update Roar link
          $("#letitroar").removeAttr("href title").css("cursor","pointer");
          // Initiate interactive audio functionality
          var dinoroar = $("#dinoroar").get(0);
          $("#letitroar, #rexosaurus").mouseover(function() {
            $("#dinoroar").stop().animate({volume: 1}, 250, function() {
              $("#rexosaurus").addClass("hovered");
              dinoroar.play();
            });
          }).mouseout(function() {
            $("#dinoroar").stop().animate({volume: 0}, 500, function() {
              $("#rexosaurus").removeClass("hovered");
              dinoroar.pause(); dinoroar.currentTime=0;
            });
          });
          // Automatically reset image when done 'Roaring'
          $("#dinoroar").bind('ended', function(){
            $("#rexosaurus").removeClass("hovered");
          });
        }

      });
    })(jQuery);

  //]]>
  </script>
</head>
<body>

<div class="uc-page uc-level-2">
  
<div id="uc-header" class="uc-section">
  <div class="identity">University of Calgary</div>
  <ul class="social-media">
    <li class="first rss"><a href="http://contacts.ucalgary.ca/directory/socialmedia/rss" title="RSS">RSS</a></li>
    <li class="facebook"><a href="http://contacts.ucalgary.ca/directory/socialmedia/facebook" title="Facebook">Facebook</a></li>
    <li class="twitter"><a href="http://contacts.ucalgary.ca/directory/socialmedia/twitter" title="Twitter">Twitter</a></li>  
  </ul>
  <ul class="access">
    <li><a href="#uc-splash">Jump to Headline</a></li>
    <li><a href="#uc-navigation">Jump to Navigation</a></li>
    <li><a href="#uc-content">Jump to Content</a></li>
  </ul>
  
  <div class="access">UofC Navigation</div>
  
  <ul id="uc-global-navigation">
    <li class="first"><a href="http://www.ucalgary.ca/">Home</a></li>
    <li><a href="http://www.ucalgary.ca/prospectivestudents/">Prospective Students</a></li>
    <li><a href="http://www.ucalgary.ca/currentstudents/">Current Students</a></li>
    <li><a href="http://www.ucalgary.ca/alumni/">Alumni</a></li>
    <li><a href="http://www.ucalgary.ca/community/">Community</a></li>
    <li><a href="http://www.ucalgary.ca/facultyandstaff/">Faculty &amp; Staff</a></li>
  </ul>
  
  <form id="uc-global-search" action="http://www.ucalgary.ca/search_results.html">
    <div>
      <label for="uc-global-search-field">Search UofC:</label>
      <input type="hidden" name="cx" value="016212948531554246733:h_v_efobwui" />
      <input type="hidden" name="cof" value="FORID:11" />
      <input type="text" id="uc-global-search-field" name="q" />
      <input type="submit" name="sa" id="uc-global-search-submit" value="Search" />
    </div>
  </form>
  
  <ul id="uc-global-references">
    <li class="first"><a href="http://www.ucalgary.ca/it/" title="Information Technologies">IT</a></li>
    <li><a href="http://www.ucalgary.ca/hr/" title="HR">HR</a></li>
    <li><a href="http://my.ucalgary.ca/" title="My UofC Portal">My U of C</a></li>
    <li><a href="http://www.ucalgary.ca/directory/" title="Contact Information and Personnel Directory">Contacts</a></li>
  </ul>
</div>

<div id="uc-splash" class="uc-section">
  <div class="logo">
    <a href="http://www.ucalgary.ca/"><img src="http://static.ucalgary.ca/current/global/images/identity/vertical-crest.svg" alt="The University of Calgary" /></a>
  </div>

  <div class="banner">
    <a href="http://www.ucalgary.ca"><img src="http://static.ucalgary.ca/current/global/images/banner_a1.jpg" width="980" height="370" alt="" /></a>
    <div class="headline">
      <div class="title"><a href="http://www.ucalgary.ca">404 - Page Not Found</a></div>
    </div>
  </div>
</div>

<div id="uc-navigation" class="uc-section">
  <div class="access">Navigation</div>

  <div class="primary">
    <ul class="menu">
      <li class="first activepath"><a href="http://www.ucalgary.ca/" class="active">Home</a></li>
      <li><a href="http://www.ucalgary.ca/prospectivestudents/">Prospective Students</a></li>
      <li><a href="http://www.ucalgary.ca/currentstudents/">Current Students</a></li>
      <li><a href="http://www.ucalgary.ca/alumni/">Alumni</a></li>
      <li><a href="http://www.ucalgary.ca/community/">Community</a></li>
      <li><a href="http://www.ucalgary.ca/facultyandstaff/">Faculty &amp; Staff</a></li>
    </ul>
  </div>
  <div class="secondary">
    <div class="title">Home</div>
    <ul>
      <li class="collapsed"><a href="http://ucalgary.ca/faculties">Faculties</a></li>
      <li><a href="http://ucalgary.ca/departments">Departments &amp; Programs</a></li>
      <li><a href="http://contacts.ucalgary.ca/directory/services/cted">Continuing Education</a></li>
      <li><a href="http://www.ucalgary.ca/research">Research</a></li>
      <li><a href="http://ucalgary.ca/international">International</a></li>
      <li class="collapsed"><a href="http://ucalgary.ca/about">About the University of Calgary</a></li>
      <li class="collapsed"><a href="http://ucalgary.ca/administration">Admin. & Governance</a></li>
      <li><a href="http://contacts.ucalgary.ca/directory/services">Campus Services</a></li>
      
    </ul>
    
  </div>
</div>

<div id="uc-content" class="uc-section">
  <div class="primary"><div class="wrapper">
    <div id="oops">
      <div id="sorry">
        <h1>4-0-Roar</h1>
        <p>Rex searched, but your page is extinct. Much like his biological family. Thanks for bringing that up.</p>
        <p>While Rex <del>hunts down and devours</del> notifies the web team, please consider:</p>
        <p>
          <ul id="options">
            <li>Using the search box at the top of the page to continue your journey.</li>
            <li>Joining Rex in a communal expression of digital angst by standing up (if you're sitting down) and letting out 
              <a id="letitroar" href="http://static.ucalgary.ca/current/404/resources/roar.mp3" title="Download the 4-0-Roar">a massive 4-0-Roar</a>.</li>
          </ul>
        </p>
        <p class="alldinos">Oh, and stay fierce. We are <u>all</u> Dinos.</p>
      </div>
      <div id="rexosaurus">
        <audio id="dinoroar" preload="auto">
          <source src="//static.ucalgary.ca/current/404/resources/roar.ogg" type="audio/ogg">
          <source src="//static.ucalgary.ca/current/404/resources/roar.mp3" type="audio/mpeg">
        </audio>
      </div>
    </div>
  </div></div>

  <div class="secondary"><div class="wrapper">
    <div class="block menu">
      <h2 class="title">THINGS TO DO</h2>
      <div class="content">
        <ul class="menu">
          <li class="leaf first"><a href="http://www.ucalgary.ca/prospectivestudents" title="Study at the university">Study at the university</a></li>
          <li class="leaf"><a href="http://www.ucalgary.ca/careersuofc/" title="Work at the university">Work at the university</a></li>
          <li class="leaf"><a href="http://www.ucalgary.ca/giving" title="Give to the university">Give to the university</a></li>
          <li class="leaf"><a href="http://www.ucalgary.ca/events" title="Attend university events">Attend university events</a></li>
          <li class="leaf"><a href="http://www.ucalgary.ca/map/" title="View campus maps and parking">View campus maps</a></li>
        </ul>
      </div>
    </div>
  </div></div>
</div>

<div id="uc-footer" class="uc-section uc-superfooter">
  <div class="wrapper">
    <div id="uc-footer-info">
      <div class="block">
        <p>University of Calgary<br />
          2500 University Dr. NW<br />
          Calgary, Alberta, Canada<br />
          T2N 1N4
       </p>
       <p>Copyright &copy; 2013<br />
       <a href="http://www.ucalgary.ca/policies/files/policies/Privacy%20Policy_0.pdf">Privacy Policy</a></p> 
      </div>
    </div>
    <div id="uc-footer-links">
      <div class="block">
      <h2>About the U of C</h2>
      <ul>
        <li><a href="http://ucalgary.ca/about/">At a Glance</a></li>
        <li><a href="http://ucalgary.ca/identity/">Identity &amp; Standards</a></li>
        <li><a href="http://www.ucalgary.ca/map/">Campus Maps</a></li>
        <li><a href="http://www.hotelalma.ca/">Hotel Alma</a></li>
        <li><a href="http://www.ucalgary.ca/hr/careers">Careers at the U of C</a></li>
        <li><a href="http://www.ucalgary.ca/events">Events at the U of C</a></li>
      </ul>
      </div>
      <div class="block">
      <h2>Academics</h2>
      <ul>
        <li><a href="http://ucalgary.ca/departments/">Departments &amp; Programs</a></li>
        <li><a href="http://ucalgary.ca/admissions">Undergraduate Studies</a></li>
        <li><a href="http://www.grad.ucalgary.ca/">Graduate Studies</a></li>
        <li><a href="http://ucalgary.ca/international">International Studies</a></li>
        <li><a href="http://conted.ucalgary.ca">Continuing Studies</a></li>
        <li><a href="http://library.ucalgary.ca">Libraries at the U of C</a></li>
      </ul>
      </div>
      <div class="block">
      <h2>Campus Life</h2>
      <ul>
        <li><a href="http://www.godinos.com/">Go Dinos!</a></li>
        <li><a href="http://www.ucalgary.ca/residence/">Residence, Hotel &amp; Conference</a></li>
        <li><a href="http://www.ucalgaryrecreation.ca/">Active Living</a></li>
        <li><a href="http://calgarybookstore.ca/">Bookstore</a></li>
        <li><a href="http://gsa.ucalgary.ca/">Graduate Students' Association</a></li>
        <li><a href="http://www.su.ucalgary.ca/">Students' Union</a></li>
      </ul>
      </div>
      <div class="block">
      <h2>Media &amp; Publications</h2>
      <ul>
        <li><a href="http://ucalgary.ca/news">News</a></li>
        <li><a href="http://ucalgary.ca/mediacentre">Media Relations</a></li>
        <li><a href="http://ucalgary.ca/news/utoday">U Today</a></li>
        <li><a href="http://www.ucalgary.ca/currentstudents/uthisweek">U This Week</a></li>
        <li><a href="http://www.umag.ca">U Magazine</a></li>
        <li><a href="http://www.ucalgary.ca/pubs/calendar/">University Calendar</a></li>
      </ul>
      </div>
    </div>
  </div>
</div>

</div>

</body>
</html>
