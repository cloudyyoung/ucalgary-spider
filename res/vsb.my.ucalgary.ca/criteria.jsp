<!DOCTYPE html>





<!-- Copyright 2011-2020. This service is called REGISTER or Visual Schedule Builder.
It is offered by VSB Software Inc and Digarc Inc. Visit: www.vsbuilder.com or www.digarc.com -->
























<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Schedule Builder - University of Calgary</title>
  		<link href="css/selectize.default.css" rel="stylesheet" type="text/css" media="all">
        <link href="css/multiselect.css?v=7515" rel="stylesheet" type="text/css"/>
        <link href="css/weekslider.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/results.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/slider.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/dategrid.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/recman.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/mobilesort.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/timetable.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/planloader.css?v=7515" rel="stylesheet" type="text/css">
		<link href="css/jquery.ui.tooltip.css" rel="stylesheet" type="text/css">
  		
		








		<meta name="robots" content="noindex">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

        <link href="css/font-awesome.min.css?v=7515" rel="stylesheet" type="text/css">
		<link href="mdl/material.min.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/lookmain.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/cbox.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/features.css?v=7515" rel="stylesheet" type="text/css">
        <link href="css/editableText.css?v=7515" rel="stylesheet" type="text/css">

        <link href='https://fonts.googleapis.com/css?family=Roboto:400,500,700' rel='stylesheet' type='text/css'>
        

	<link href="cust/ucg/template_ucg.css?v=7515" rel="stylesheet" type="text/css"/>
<link rel="shortcut icon" type="image/png" href="cust/ucg/favicon.ico" />


		<!-- Custom client JS -->
		<script type="text/javascript" charset="UTF-8" src="cust/ucg/js_ucg.js?v=7515"></script>

		<script type="text/javascript" charset="UTF-8" src="globalsettings.jsp?_=1608335687092"></script>

		<script type="text/javascript" charset="UTF-8" src="js/jquery-1.11.1.min.js"></script>
		<script type="text/javascript" charset="UTF-8" src="mdl/material.js"></script>
		<script type="text/javascript" charset="UTF-8" src="js/unity.js?v=7515"></script>
		<script type="text/javascript" charset="UTF-8" src="js/render.js?v=7515"></script>
		<script type="text/javascript" charset="UTF-8" src="js/render2.js?v=7515"></script>
		<script type="text/javascript" charset="UTF-8" src="js/engine.js?v=7515"></script>
		<!-- <script type="text/javascript" charset="UTF-8" src="js/least.js?v=7515"></script> -->
		<script type="text/javascript" charset="UTF-8" src="js/legend.js?v=7515"></script>
		<script type="text/javascript" charset="UTF-8" src="js/schedule.js?v=7515"></script>
		<!-- <script type="text/javascript" charset="UTF-8" src="js/dragcode.js?v=7515"></script> -->
		<!-- <script type="text/javascript" charset="UTF-8" src="js/gencode.js?v=7515"></script> -->
        <script type="text/javascript" charset="UTF-8" src="js/common.js?v=7515"></script>
        <script type="text/javascript" charset="UTF-8" src="js/editableText.js?v=7515"></script>

       
        

		<!-- Dispatch custom event polyfill for IE -->	
		<script type="text/javascript" charset="UTF-8">
		(function () {
  			if ( typeof window.CustomEvent === "function" ) return false; //If not IE
			
  			function CustomEvent ( event, params ) {
    			params = params || { bubbles: false, cancelable: false, detail: undefined };
    			var evt = document.createEvent( 'CustomEvent' );
    			evt.initCustomEvent( event, params.bubbles, params.cancelable, params.detail );
	    		return evt;
   			}
			
  			CustomEvent.prototype = window.Event.prototype;
			
  			window.CustomEvent = CustomEvent;
		})();
		
		</script>
		<script type="text/javascript" src="js/i8n.jsp?v=95000004&amp;lang=en"></script>
		<script src="js/popup.js"></script>
		<script type="text/javascript" src="js/recman.js?v=7515"></script>
		<script type="text/javascript" src="js/slider.js?v=7515"></script>
		<script type="text/javascript" src="js/dragging.js?v=7515"></script>
        <script type="text/javascript" src="js/guidance.js?v=7515"></script>
        <script type="text/javascript" src="js/auto_suggest.js?v=7515"></script>
        <script type="text/javascript" src="js/profiler.js?v=7515"></script>
        <script type="text/javascript" src="js/multiselect.js?v=7515"></script>
        <script type="text/javascript" src="js/timetable.js?v=7515"></script>
        <script type="text/javascript" src="js/selectordie.js?v=7515"></script>
        <script type="text/javascript" src="js/jquery-ui.js?v=7515"></script>
 		<script type="text/javascript" src="js/jquery-ui-1.10.3.min.js"></script> 
        <!-- This makes the Date Slider moveable using touch: -->
        <script type="text/javascript" src="js/jquery.ui.touch-punch.min.js?v=7515"></script>
        <script type="text/javascript" src="js/accessibility.js?v=7515"></script>
        <script type="text/javascript" src="api/v2/multiselectdata.js?v=95000004"></script>
        <script type="text/javascript" src="js/thumbnail.js?v=7515"></script>
        <!-- Support for Push Course IDs from PeopleSoft -->
        <!-- <script type="text/javascript" src="js/peoplesoftpushedcourses.js?v=7515"></script> -->

		<script type="text/javascript" src="js/dwaudit.js?v=7515"></script>
		<script type="text/javascript" src="js/capp-plan.js?v=7515"></script>
		<script type="text/javascript" src="js/entrance.js?v=7515"></script>
		<script type="text/javascript" src="js/planloader.js?v=7515"></script>

        
        
        <script type="text/javascript">
	        if (breakOutOfIframe && top.location!= self.location) {
	   			top.location = self.location.href;
			}
        </script>

        <script type="text/javascript">


            // Called by body onload
            function init() {
            	document.body.addEventListener('mousedown', function() {
            		document.body.classList.add('using-mouse');
            		document.body.classList.remove('using-tab');
            	});
            	document.body.addEventListener('keydown', function(key) {
            		if (key.keyCode === 9) {
	            		document.body.classList.add('using-tab');
            		} else {
	            		document.body.classList.remove('using-tab');
            		}

            		document.body.classList.remove('using-mouse');
            	});
            	
            	initCriteria();
   				var guidancePromise = GG.guidanceInit(username,terms,"#guidance")
   					.then(function() {
   						return EE.initEntrance({"32203":{"name":"2020 Spring","disableCart":false,"disableEnroll":false,"enrollable":false,"d1":"4480","d2":"4589","ee":"4418"},"32205":{"name":"2020 Summer","disableCart":false,"disableEnroll":false,"enrollable":false,"d1":"4564","d2":"4624","ee":"4418"},"32207":{"name":"2020 Fall","disableCart":false,"disableEnroll":false,"enrollable":false,"d1":"4566","d2":"4749","ee":"4480"},"32211":{"name":"2021 Winter","disableCart":false,"disableEnroll":false,"enrollable":false,"d1":"4750","d2":"4869","ee":"4480"}});
   					})
   					.done(function() {
	            		// We're calling all the code below
            			// after getAcademicPlans is called in case any items are mandatory
                		//initCriteria();
            			if (displayLocationOption) {
	            			initMultiselectors();
            			}
	
                		UU.caseF5();
                		vsbTimer=new VsbTimer(900000,110*1000,120000,false,isAuthenticatedWithSso);
	
    					Profiler.addDuration("filterOutFull", BB.activeState.filters.hideFull);
    					Profiler.addDuration("filterOutWaitlistable", BB.activeState.filters.hideWaitlistable);
    					Profiler.addDuration("filterOutOnline", BB.activeState.filters.hideOnline);
    					Profiler.addDuration("filterOutOnCampus", BB.activeState.filters.hideOnCampus);
    					Profiler.addDuration("filterOutReserved", BB.activeState.filters.hideReserved);
    					Profiler.setParameterState(translateSortToParameter(BB.activeState.sort), true);          
    					
    					GG.guidanceSettle();
            		})
 					.fail(function(){console.log("criteria init failed");});
            }

        </script>
		


        <style>
        
        	#collegeSelector {
				display:none;
			}
        
        
        
        
        	#instructSelector {
				display:none;
			}
        
        
        	.bg_green {
				background-image: url(images/element_open_ps.gif);
			    background-repeat: no-repeat;
 				background-position: 34% 13%;
			}
			.bg_yellow {
				background-image: url(images/element_waitlist_ps.gif);
			    background-repeat: no-repeat;
 				background-position: 34% 13%;
			}
			.bg_red {
				background-image: url(images/element_full_ps.gif);
			    background-repeat: no-repeat;
 				background-position: 34% 13%;
			}
			.bg_orange {
				background-image: url(images/element_reserved_ps.gif);
			    background-repeat: no-repeat;
 				background-position: 34% 13%;
			}
			td.full_indic {
				background-position: 34% 50%;
				width: 20px;
			}
        
        </style>
		
		
		
	</head>
    <body onload="init()" class="welcome show_filters_if_widescreen" id="bodyNode">
    <p id="alertJAWS" role="alert" style="display:none;"></p>
    
    <div class="eeLoadingAnimation">
    	<div class="mdl-spinner mdl-js-spinner is-active"></div>
    	<!-- LOADING <div class="mdl-spinner mdl-js-spinner is-active"></div> -->
    </div>
    
    <div id="bodyContent" class="eeLoading">


<div class="custom_header noprint">










<div class="demoHeader noprint">
	<div class="headerInside">
		<div class="demoLogo"></div>
	</div>
	<div class="ucg_vsb_logo"></div>
</div>





</div>
<div class="mainframe">


<div class="header_invader header_invader_position noprint">

	<div class="autho_table">
			<span class="autho_logo_prot_cell header_invader_logo_width">
				&nbsp;
			</span>
			<span class="autho_text_cell">
 				
				<span class="autho_text header_invader_text_top">
					
						
						<span title="Not Authenticated">Guest</span>
					
				</span>
				<span class="autho_text header_invader_text_top">
					
				</span>
				
 				<span class="autho_text header_invader_text_top active-term-label" onclick="MENU.menuFunction()" style="cursor:pointer" title="Change term"></span>
			</span>
			<span class="autho_button_cell">
				
				<button class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent sign_in_button " 
					onclick="vsbTimer.doLogin();">
					Sign In
				</button>
				<input class="big_button sign_out_button" type="button" value="Sign Out" onclick="vsbTimer.doLogout('link');"/>
				
				<a href="javascript:void(0);" class="main_menu_button" title="View menu">
					<i class="fa fa-bars"></i>
				</a>
			</span>
	</div>

	<div class="main_menu">
		<div class="menu_item select_term"></div>
		<div class="menu-item-separator"></div>
		<a href="analytics/" class="mi_analytics analytics_link">VSB Analytics</a>
		<a href="analytics/#ajax/settings.jsp?sets=roles" class="mi_settings analytics_link">VSB Settings</a>
		<div class="menu-item-separator"></div>
		<a href="criteria.jsp?src=clear">Start Over</a>
		<div class="menu-item-separator"></div>
		<a href="javascript:void(0)" class="mi_behalf">Advise a Student...</a>
		<div class="menu_item mi_message_box" style="display:none">
		</div>
		<div class="menu_item mi_behalf_start" style="display:none">
			<input type="text" style="width:100%" class="behalf_userid" placeholder="Student ID" title="Student ID"/><br/>
			<input style="margin-top:3px;margin-right:5px" class="big_button behalf_start_button" type="button" value="Start Advising"/>
			<input style="margin-left:3px;" class="big_button behalf_cancel_button" type="button" value="Cancel"/>
		</div>
		<div class="menu_item mi_behalf_change">
			Advising for: <span class="behalf_student">---</span><br/>
			<input style="margin-top:5px;margin-right:3px" class="big_button switch_student_button" type="button" value="Switch" title="Advise a different student"/>
			<input style="margin-left:3px;" class="big_button stop_advising_button" type="button" value="Stop Advising"/></div>
		
		
		<div class="menu-item-separator"></div>
		<div class="menu_item mi_sign_out">
			<button style="width:100%" class="mdl-button mdl-js-button xmdl-button--raised white-background"  
				onclick="vsbTimer.doLogout('link');">
				Sign Out
			</button>
				
		</div>
		<div class="menu_item mi_sign_in">
			<input style="width:100%" class="big_button" type="button" value="Sign In" onclick="vsbTimer.doLogin();"/>
		</div>
		
	</div>
</div>


<div class="navigation noprint"><div class="navigation_buttons">

<div style="width:100%">
<ul>
<li><a href="javascript:void(0)" class="accessible ak_c nav_link link_criteria navselected title_font" onclick="UU.caseViewCriteria();">Select <span class="akl">C</span>ourses</a></li>
<li><a href="javascript:void(0)" class="accessible ak_r nav_link link_results title_font" onclick="UU.caseViewResults();">Schedule <span class="akl">R</span>esults</a></li>

<li><a href="javascript:void(0)" class="accessible ak_f nav_link link_favorites title_font" onclick="UU.caseViewFavorites();">Favourites</a></li>

</ul>

</div></div>


<div style="clear:both;"></div>
</div>

<div style="clear:both;"></div>

<div id="under_header_wrapper">
<div id="under_header">


<table class="pages_table" style="height:1200px">
<tr>

<td id="page_criteria" class="vsb_page disable-get-schedule" style="width:0%">
<div class="page_fader"></div>
<div class="full_page_title title_font first">
Select <span class="akl">C</span>ourses
</div>


<div class="full_page">

<div class="full_page_content" id="tab_degree" style="display:none;">
	<div>
		<button class="mdl-button mdl-js-button mdl-js-ripple-effect search-back-button"
			onclick="RR.changeSelCourseTab('tab_selected');">
				Back
		</button>
	</div>
	<div class="select-course-title">
		Degree Plan
	</div>
	<div class="tab_container">
		<div class="tab_content">
			
			<div id="plan_import_container">
			</div>
		</div>
	</div>
</div>

<div class="full_page_content" id="tab_selected">

<h2 class="visuallyhidden">Select Courses Region</h2>
<p class="visuallyhidden" style="margin-bottom:15px" id="page_add_courses_desc">
Welcome to the Schedule Builder. This is the Select Courses region. To use this software, follow the steps described below. First add courses to the list of courses. This will cause the Results region to show you a list of possible schedules.
</p>

	<div class="mobileRoom hide50"></div>
	<div class="accessOnly accessTermDisp"><h3>Step <span class="bubbleNb1">1</span>: Select Term</h3><div>Choose a term.</div></div>
	<div id="term_region_alt"></div>

	<div class="accessOnly"><h3>Step <span class="bubbleNb2a">2a</span>: Select Campuses</h3>Select your desired course locations.</div>
	<div id="locationRegion" class="locationRegion-cont xhide50">
		<div id="collegeSelector"></div>
		<div id="campusSelector"></div>
		<div id="locationSelector"></div>
		<div id="instructSelector"></div>
	</div>




<div class="accessOnly">
<h3>Step <span class="bubbleNb2">2</span>: Select a Course</h3>
<div>
Begin typing a course code or name that you would like to take.
<br/><br/>Example: <strong>MATH 267</strong> or <strong>ENGL 203</strong>
</div>
</div>

<div id="sel_midrange">
	<div class="bubble" id="step2abubble">
		<div class="tip_top"><i class="fa fa-caret-up"></i></div>
		<div class="bubbletitle hide50" style="float:left">Step <span class="bubbleNb2a">2a</span></div>
	    <div>
	    	<img src="images/step_arrow_north.png" style="float:right" alt="" class="phone step_arrow"/>
		    <div style="float:left;clear:left">Select your desired course locations.</div>
	    	<div style="clear:both"></div>
	    </div>
	    <div class="tip_bottom weakhide"></div>
	</div>


	<div id="message_area">
	</div>

	<div class="bubble" id="step2bubble">
	    <div class="bubbletitle hide50">Step <span class="bubbleNb2">2</span></div>
		Begin typing a course code or name that you would like to take.
    	<img src="images/step_arrow_south.png" style="margin-top: 17px;" alt="" class="pull-right phone step_arrow"/>
		<br/><br/>Example: <strong>MATH 267</strong> or <strong>ENGL 203</strong>
		<div class="tip_bottom"><i class="fa fa-caret-down"></i></div>
    	<div class="clearfix"></div>
	</div>
</div>

<div class="plusBox">
	<div class="visuallyhidden">
		<label for="code_number">Course Code. For example, E N space 1 1 9 and press enter</label>
		<div id="autocomplete-results" aria-live="assertive" aria-atomic="true">
		</div>
	</div>
	
	<div class="sdl_input plusInput">
  		<label for="code_number">Select Course</label>
  		<input class="disable-welcome dont-enable disable-get-schedule" type="text" placeholder="Subject, Title, Instructor..." id="code_number" autocomplete="off"/>
  		
	</div>
	
	<div style="clear:both"></div>
	<div class="crnListWarning importOnlyPlan">
		You cannot manually select courses because you must follow the assigned recommendation.
	</div>
	<div class="crnListWarning crnListWarningInfo noSelectAlert">
		You cannot manually select courses but you can import them from your Course Queue which you can fill in your My Academic Requirements <span class='noSelectAdvice'></span>
	</div>
	<div class="crnListWarning crnListWarningInfo noSelectAlertAdvisor">
		Note that this student acting alone can only select courses from their Academic Requirements by importing them via the Course Queue <span class='noSelectAdvice'></span>
	</div>
	<div class="crnListWarning crnListWarningInfo noSelectAlertGuest">
		Schedule Builder is currently being piloted for only specific users. However, we anticipate this new tool will be available to you sometime in the future. <span class='noSelectAdvice'></span>
	</div>
	
	<!-- Course browsing -->
	
</div>



<div class="plusBoxBelow">
	
</div>


<div id="select-course-filters" class="hide50" style="margin-bottom:10px;">
    <div style="text-align: left; width: 100%">
    </div>
	<div style="text-align: left" >
		<div style="display:flex; align-items: center; height:47px">
		Locations
		<button class="mdl-button mdl-js-button" id="add-location-filter" onclick="
		$('#add-location-filter').hide();
		$('.select-course-filters-input-container').show()"
			style="width:20px; padding: 0 5px; margin-left: 2px; min-width: 0;">+</button>
		<span class="select-course-filters-input-container" style="display:none">
	    	<input style="width: 200px;" type="text" value="" id="select-course-filters-input" placeholder="Select Location">
		</span>
		</div>
    <div class="selected-filters-chips" >
    	<span class="mdl-chip mdl-chip--deletable" id="selectCourseFilterChipTemplate" style="display:none">
    		<span class="mdl-chip__text chip-text">Deletable Chip</span>
    		<button type="button" class="mdl-chip__action">
    			<i class="fa fa-close" aria-hidden="true"></i>
    		</button>
		</span>
    </div>
    </div>
</div>

<h3 class="accessOnly">List of Courses:</h3>

<div class="crnListWarning tooManyResults">
	The generated schedule results are truncated because the input is too broad. To ensure all results are considered, pin down or toggle off some of your preferred classes.
</div>

<div id="requirements" style="position:relative">

	<div id="size-tester">Sample Sizer</div>

	<div class="loadingDiv flap_loading" id="flap_loading">Retrieving schedule...</div>

	<div class="requirementDiv2 rbox" id="templateCourse2" style="display:none;">
		<div class="rbox-header" style="display:none;">
			<div class="rbox-header-cont clearfix2">
				<span class="block_piece_indicator_cont" title="Course belongs to a block of courses"><span class="block_piece_indicator">&nbsp;</span></span>
				<span class="rbox-wheader">
					<span class="wildcard-title requirementTitle1">Subject or Title </span>
					<span class="wildcard-title requirementTitle2" style="display:none">Catalog Number: </span>
					<span class="wildcard-title requirementTitle3" style="display:none">Attribute: </span>
				</span>
				<div class="clearfix2" style="float:right;">
					<div class="reqInfo">Choose a course from the following list:</div>
					<div class="optionsSelect"></div>
				</div>
			</div>
		</div>


		<div class="cbox-margin">
			<div class="cbox-toggle">
				<label class="Dmdl-checkbox Dmdl-js-checkbox Dmdl-js-ripple-effect dynID" for="cnf_toggle">
					<input type="checkbox" id="cnf_toggle" class="Dmdl-checkbox__input ignore_check dynID" checked>
					<span class="cbox-label"></span>
				</label>
			</div>
			<div class="cbox"> <!-- Add 'roomy' to classes to stretch content, 'expanded' to pre-expand -->
				<table cellpadding="0" cellspacing="0" style="width: 100%" class="cbox-expand-region">
					<tr>
						<td style="width: 10%">
							<div class="cbox-cn">
								COMM<br/>217
							</div>
						</td>
						<td class="cbox-header">
							<span class="leftnclear cbox-title">Financial Accounting</span>
							<span class="cnf_req_state">Required or Recommended</span>
							<span class="course_state"></span>
							<span class="leftnclear cbox-subtitle">
								<!-- <span class="cnf_consider dynID" id="tipConsiderX">Considering 3 of 5 Classes</span>&nbsp;&nbsp; -->
								<span class="cnf_campus_info">Walnut Creek Campus</span></span>
							
							<span class="cnf_dropdown cbox-dropdown-cont leftnclear" onkeydown="return avoidChange(event);" onkeypress="return avoidChange(event);" onkeyup="return avoidChange(event);" onclick="event.stopPropagation();">
								<!-- <div class="dh_locker_hotspot" onclick="UU.caseToggleDropLock($(this).parents('.requirementDiv2').data('cnfid'));">&nbsp;</div> -->
								<!-- <img src="images/padlock.gif" style="vertical-align:middle;" class="dropdownLockImg" alt="Padlock" title="The specific class you are to take for this course has been assigned to you by an advisor"/> -->
								<select class="cbox-dropdown cbox-dropdown-normal dropdownSelect" title="Select your intentions with this course">
									<option value="al">Try all classes</option>
									<!-- <option value="ig">Ignore this course</option>  -->
									<option value="ss" class="cnf_specific_option">Try specific classes...</option>
								</select>
								<img src="images/pin.png" style="vertical-align:middle;cursor:pointer;margin:-2px 0px" class="dropdownPinImg" alt="Push Pin"/>
								<img src="images/padlock.gif" style="vertical-align:middle;margin:-2px 0px" class="dropdownLockImg" alt="Padlock" title="The specific class you are to take for this course has been assigned to you by an advisor"/>
								<div class="cnf_class_lock_tip Dmdl-tooltip mdl-tooltip--top dynID" for="tipClsLockX">Lock this class</div>
								<button aria-label="lock class" class="class_locker_button mdl-button mdl-js-button mdl-button--icon dynID" id="tipClsLockX" onclick="UU.caseToggleDropLock($(this).parents('.requirementDiv2').data('cnfid'));" style="margin:-6px 0 -6px 0;">
									<i class="class_unlocked fa fa-unlock-alt"></i>
									<i class="class_locked fa fa-lock"></i>
								</button>
							</span>
						</td>

						<td class="cbox-option cnf_lock" style="width: 3%" onclick="event.stopPropagation();">
							<div class="cnf_locker_tip Dmdl-tooltip mdl-tooltip--top dynID" for="tipLockX">Lock this course</div>
							<button aria-label="lock course" class="cnf_locker_button mdl-button mdl-js-button mdl-button--icon dynID" id="tipLockX">
								<i class="cnf_unlocked fa fa-unlock-alt"></i>
								<i class="cnf_locked fa fa-lock"></i>
							</button>
						</td>
						<td class="cbox-option" style="width: 3%" onclick="event.stopPropagation();">
							<div class="cnf_trash_tip Dmdl-tooltip mdl-tooltip--top dynID" for="tipTrashX">Drop this course</div>
							<button aria-label="Remove class" class="cnf_trash_button mdl-button mdl-js-button mdl-button--icon dynID" id="tipTrashX">
								<img class="cbox-trash-icon" src="images/trash.svg"/>
								<img class="cbox-trash-icon-open" src="images/trash_open.svg"/>
								<i class="fa fa-undo cbox-trash-icon-undo"></i>
							</button>
						</td>
						<td class="cbox-option cbox-expander" style="width: 3%">
							<div class="Dmdl-tooltip mdl-tooltip--top dynID cnf_tip_expand" for="tipExpandX">Click to {} more options and information on {}</div>
							<button aria-label="Expand class detail" class="mdl-button mdl-js-button mdl-button--icon dynID" id="tipExpandX">
								<i class="fa fa-angle-down"></i>
							</button>
						</td>

					</tr>
				</table>
				<div class="cbox-warnings">
					<i class="fa fa-exclamation-triangle"></i> This course has no classes still open for enrollment
				</div>
				<div class="cbox-expansion" style="display:none">

					<div class="cbox-row clearfix2 cnf_desc">
						<span class="cbox-row-title">Description:</span>
						<span class="cbox-row-content cnf_desc_desc"> This course is designed to familiarize the students with the processes
							involved in the design, planning, and construction of dramatic motion picture sets. </span>
						<div style="clear: both"></div>
					</div>

					<div class="cbox-row clearfix2 cnf_reqs">
						<span class="cbox-row-title">Requirements:</span>
						<span class="cbox-row-content cnf_req"> ACT English 18-19 or COMPASS English 70-80. </span>
					</div>

					<div class="core_names_cont2 cbox-row clearfix2">
						<span class="cbox-row-title">Attributes:</span>
						<span class="core_names cbox-row-content">HON, CORE</span>
					</div>

					<div class="cbox-row clearfix2 cnf_cross_listed">
						<span class="cbox-row-title">Cross Listed Courses:</span>
						<span class="cbox-row-content cnf_cross_listed_desc"> MATH 101, CHEM 303 </span>
					</div>

					<div class="cbox-row clearfix2 noselect selectAllNoneContainer">
						<span class="cbox-row-title">Campuses:</span>
						<div style="clear:both"></div>
						<span class="campus_checkboxes clearfix2">
							<span class="cbox-selitem">
								<label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect cbox-checkbox" for="checkbox-X1">
									<input type="checkbox" id="checkbox-X1" class="mdl-checkbox__input" checked/>
									<span class="cbox-selitem-label">Sir George Williams</span>
								</label>
							</span>
						</span>
						<div class="cbox-allnone cnf_campuses_allnone">
							<button class="Dmdl-button mdl-js-button mdl-js-ripple-effect selectAll">Select All</button>
							<button class="Dmdl-button mdl-js-button mdl-js-ripple-effect selectNone">Select None</button>
						</div>
					</div>

					<div class="cbox-row noselect">
						<span class="cbox-row-title clearfix2">Period:</span>
						<div style="clear: left"></div>
						<select class="cbox-select select_period">
							<option>Period A</option>
							<option>Period B</option>
						</select>
					</div>

					<div class="cbox-row noselect">
						<span class="cbox-row-title clearfix2">Section:</span>
						<div style="clear: left"></div>
						<select class="cbox-select select_usn">
							<option>Item A</option>
							<option>Item B</option>
						</select>
					</div>

					<div class="cbox-row clearfix2 noselect selectAllNoneContainer cnf_modes">
						<span class="cbox-row-title">Include classes that are:</span>
						<div style="clear:both"></div>
						<span class="mode_checkboxes">
							<span class="cbox-selitem">
								<label class="Dmdl-checkbox Dmdl-js-checkbox Dmdl-js-ripple-effect cbox-checkbox dynID" for="cb_online">
									<input type="checkbox" id="cb_online" class="Dmdl-checkbox__input dynID" checked/>
									<span class="cbox-selitem-label">Online</span>
								</label>
							</span>
							<span class="cbox-selitem">
								<label class="Dmdl-checkbox Dmdl-js-checkbox Dmdl-js-ripple-effect cbox-checkbox dynID" for="cb_on_camp">
									<input type="checkbox" id="cb_on_camp" class="Dmdl-checkbox__input dynID" checked/>
									<span class="cbox-selitem-label">On Campus</span>
								</label>
							</span>
							<span class="cbox-selitem">
								<label class="Dmdl-checkbox Dmdl-js-checkbox Dmdl-js-ripple-effect cbox-checkbox dynID" for="cb_lod">
									<input type="checkbox" id="cb_lod" class="Dmdl-checkbox__input dynID" checked/>
									<span class="cbox-selitem-label">Learn on demand</span>
								</label>
							</span>
						</span>
						<div class="cbox-allnone">
							<button class="Dmdl-button mdl-js-button mdl-js-ripple-effect selectAll">Select All</button>
							<button class="Dmdl-button mdl-js-button mdl-js-ripple-effect selectNone">Select None</button>
						</div>
					</div>

					<div class="cbox-row clearfix2 noselect cnf_classes selectAllNoneContainer">
						<span class="cbox-row-title">Classes:</span>
						<div style="clear:both"></div>
						<span class="class_checkboxes">
							<span class="cbox-selitem cbox-classitem">
								<label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect cbox-checkbox" for="checkbox-Y1">
									<input type="checkbox" id="checkbox-Y1" class="mdl-checkbox__input class_chk" checked>
									<span class="cbox-selitem-label full">Lec A</span>
								</label>
								<div class="cbox-hover-pin">Pin</div>
							</span>
							<span class="cbox-selitem cbox-classitem">
								<label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect cbox-checkbox" for="checkbox-Y2">
									<input type="checkbox" id="checkbox-Y2" class="mdl-checkbox__input class_chk" checked>
									<span class="cbox-selitem-label waitlisted">Lec B</span>
								</label>
								<div class="cbox-hover-pin">Pin</div>
							</span>
						</span>
						<div class="cbox-allnone">
							<button class="Dmdl-button mdl-js-button mdl-js-ripple-effect selectAll">Select All</button>
							<button class="Dmdl-button mdl-js-button mdl-js-ripple-effect selectNone">Select None</button>
						</div>
					</div>

					<div class="cbox-row clearfix2 cnf_subj_note">
						<span class="cbox-row-title">Subject Notes:</span>
						<span class="cbox-row-content cnf_subj_note_desc"> abc </span>
					</div>

					<div class="cbox-row clearfix2 cnf_cattrs">
						<span class="cbox-row-title">Course Attributes:</span>
						<span class="cbox-row-content cnf_cattr">Value1, Value2</span>
					</div>

					<div class="cnf_custom_attrs">
						<div class="cbox-row clearfix2 cnf_attrs">
							<span class="cbox-row-title">Attribute1:</span>
							<span class="cbox-row-content cnf_attr">Value1</span>
						</div>
						<div class="cbox-row clearfix2 cnf_attrs">
							<span class="cbox-row-title">Attribute2:</span>
							<span class="cbox-row-content cnf_attr">Class1, Class3: Value1</span>
							<span class="cbox-row-content cnf_attr">Class2: Value2</span>
						</div>
					</div>
					
					<div class="cbox-row clearfix2 cnf_class_notes">
						<span class="cbox-row-title">Class Remarks:</span>
						<span class="cbox-row-content cnf_class_notes_desc"> abc </span>
					</div>

				</div>
			</div>
		</div>

	</div>

</div>

    <div class="reg_generate">

      <input title="" class="big_button" type="button" name="do_search" value="Generate Schedules" onclick="UU.caseViewResults();" id="do_search"/>


<div style="margin-top:9px;position:relative">
	<div class="bubble" id="step3bubble" style="display:none">
		<div class="tip_top"><i class="fa fa-caret-up"></i></div>
	    <img src="images/step_arrow_north.png" alt="Up arrow for step instructions" class="pull-right phone step_arrow"/>
	    <div class="bubbletitle hide50">Step <span class="bubbleNb3">3</span></div>
	    Once the desired courses are listed, click the 'Generate Schedules' button.
	    <div class="clearfix"></div>
	</div>
</div>


    </div>


<div class="bottomAdvice noprint"></div>

<div class="enrollmentEncouragement noprint"></div>

<div class="bottomLinks noprint">

	
	
	<a href="javascript:void(0);" onclick="custReturnToStudentCentre();" id="linkReturnToStudentCentre">
		<img id="return_icon" src="images/return.gif" style="vertical-align:middle" alt="Return icon"/> Return to Student Center
	</a>
   	<a class="hideIfDisableCart disable-get-schedule" href="javascript:void(0);" onclick="custViewMyShoppingCart();">
    	<img id="schedule_icon" src="images/cart.gif" style="vertical-align:middle" alt="Cart icon"/> View My Enrollment Course Cart
    </a>
    
	
	
</div>

<div class="bottomLinks noprint hide50">

      <a href="javascript:void(0)" onclick="clearSearch();" title="Reset the contents on this page">
      	<img src="images/broom.png" style="vertical-align:middle" height="18" width="18" alt="Clear search icon"> Start Over
      </a>

    

    

	

	
	






      <a href="http://www.youtube.com/embed/o-1b9Xcqwzw?modestbranding=1" target="_blank">
          <img src="images/video.png" style="vertical-align:middle" alt="Video icon"/> Video 1: Selecting Courses (5min)
      </a>
      <a href="http://www.youtube.com/embed/7Gb4OzZDojA?modestbranding=1" target="_blank">
          <img src="images/video.png" style="vertical-align:middle" alt="Video icon"/> Video 2: Browsing Results (4min)
      </a>
      <a href="http://www.youtube.com/embed/sWIH1iP_jAM?modestbranding=1" target="_blank">
          <img src="images/video.png" style="vertical-align:middle" alt="Video icon"/> Video 3: How to Register (4min)
      </a>
      <a href="https://www.ucalgary.ca/registrar/registration/schedule-builder" target="_blank">
          <img src="images/question.png" style="vertical-align:middle" alt="Help icon"/> Instructions
      </a>








</div>
<div><span class="fullscreen-results-total-schedules"></span></div>
<button class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--raised mdl-button--accent welcome-search-continue"
	onclick="PAGES.exitFullScreenSearch()" disabled>
	View Schedules
</button>

</div>

<div class="full_page_content" id="tab_search" style="display:none;">
	<div>
		<button class="mdl-button mdl-js-button mdl-js-ripple-effect search-back-button"
			onclick="RR.changeSelCourseTab('tab_selected');">
				Back
		</button>
	</div>
	<div class="select-course-title">
		Advanced Course Search
	</div>
	<div class="tab_container">
		<div class="tab_content">
			<!DOCTYPE html>










<div id="advanced_search_html">
<div class="course-browsing">
	<div class="course-browsing-search">
		<table>
			<tbody>
				
				
				
				
				<tr>
					<td colspan="2">
						<div class="cb_filter_row clearfix2">
							<div class="cb_filter_text">
								Selected campuses only 
								<span id="miniCamsSelected"></span>
							</div>
							<div class="cb_filter_switch">
								<label class="mdl-switch mdl-js-switch mdl-js-ripple-effect" for="cb_selected_campuses_only" >
									<span class="mdl-switch__label"></span>
									<input id="cb_selected_campuses_only" type="checkbox" class="mdl-switch__input" checked="checked"> 
								</label>
							</div>
						</div>
					</td>
				</tr>
				
				
				<tr id="cb_acad_career_row">
					<th>Academic Career:</th>
					<td>
						<select id="cb_acad_career">
							<option value="" label=""></option>
							<!-- Filled by writeObjectIntoSelect -->
						</select>
					</td>
				</tr>
				
				
				<tr id="cb_course_external_subject_row">
					<th>Course Subject:</th>
					<td>
						<select id="cb_course_external_subject">
							<option value="" label=""></option>
							<!-- Filled by writeObjectIntoSelect -->
						</select>
					</td>
				</tr>
				
				
				<tr>
					<th>Academic Group:</th>
					<td>
						<select id="cb_academic_group">
							<option value="" label=""></option>
							<!-- Filled by writeObjectIntoSelect -->
						</select>
					</td>
				</tr>
				
				<tr id="cb_course_attribute_row">
					<th>Course Attribute:</th>
					<td>
						<select id="cb_course_attribute" required>
							<option value="" selected></option>
							<!-- Filled by writeObjectIntoSelect -->
						</select>
					</td>
				</tr>
				<tr>
					<th>Course Attribute Value:</th>
					<td>
						<select id="cb_course_attribute_value">
							<option value="" label=""></option>
						</select>
					</td>
				</tr>
				
				<tr id="cb_requirement_designation_row">
					<th>Requirement Designation:</th>
					<td>
						<select id="cb_requirement_designation">
							<option value="">All Requirement Designation</option>
							<!-- Filled by writeObjectIntoSelect -->					
						</select>
					</td>
				</tr>
				
				
				<tr id="cb_session_row">
					<th>Period:</th>
					<td>
						<select id="cb_session">
							<option value="" label=""></option>
							<!-- Filled by writeObjectIntoSelect -->
						</select>
					</td>
				</tr>
				
				<tr>
					<th>Keywords:</th>
					<td>
						<input id="cb_search_term" type="text" class="fancy-input" placeholder="Subject, Title, Instructor...">
					</td>
				</tr>
				<tr>
					<td colspan="2">
						<button style="width:100%" id="course-browsing-search-btn" 
							class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent">
							SEARCH
						</button>
						<div style="clear:both"></div>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
	<div class="course-browsing-results">
		<div id="cb_search_results" class="course-browsing-results-listing sdl-scrollbars">
			<table class="cb-results_table" id="cb-results_table">
				<!-- Filled with cbSearchCourses2 function -->
			</table>
		</div>
		<div class="search-tab-footer">
			<label class="mdl-switch mdl-js-switch mdl-js-ripple-effect" for="cb_show_selected_only_cbx">
				<input id="cb_show_selected_only_cbx" type="checkbox" class="mdl-switch__input" disabled="disabled">
				<span class="mdl-switch__label cb_switch_text">View selected only</span>
			</label>
			
		</div>
	</div>




	<div style="clear:both"></div>
</div>
</div>
		</div>
	</div>
	<div>
		<input type="button" class="big_button" id="cbSelectCourses" value="Select Courses" disabled="disabled"/>
	</div>
</div>

</div>

<div class="page_whiteout"></div>
</td> <!-- end of page_criteria -->


<td id="page_results" class="vsb_page" style="width:63.5%">

<div class="left_gradient nomobile"></div>
<div class="right_gradient nomobile"></div>
<div class="page_fader"></div>

<div class="full_page_title title_font">
	<a id="page_criteria_expander" href="javascript:void(0);" title="Collapse Select Courses" class="expander chevron_left disable-get-schedule"></a>
	
	<a id="page_favorites_expander" href="javascript:void(0);" title="Expand Favourites" class="expander chevron_right disable-get-schedule"></a>
	
	<div class="left_gradient">
	</div>
	<div class="right_gradient">
	</div>
	<span class="results_page_title">Schedule <span class="akl">R</span>esults</span>
</div>
<div class="full_page">
<div class="full_page_content">

<h2 class="visuallyhidden" style="margin-left:6px;">Results Region</h2>
<div class="mobile_sort_filter mobileonly hide50">
	
	<button type="button" id="forfavorite" class="btn btn-mid fav_link disable-get-schedule" onclick="UU.caseFavoriteResult();return false;" title="Save as Favourite">Favorite</button>
	 
	<button type="button" id="xfortips" class="btn btn-mid tip_link disable-get-schedule" onclick="SLIDER.showTip();return false;" title="Tips">Tips</button>

	<button type="button" id="forsort" class="btn btn-mid disable-get-schedule">Sort</button>
	<div style="clear:both"></div>
</div>

<p id="alertJAWSresult" role='alert' style='display:none;'></p>

<div id="flap_loading2" class="flap_loading">
	&nbsp;
	<span id="procStatus">Generating Schedules...</span>
</div>

<div id="flap_pause_results">
	<div class="resultMax pause_max">0</div>
	<div class="pause_found">schedule results</div>
	<div class="pause_view_results" style="display:none">
		<input type="button" class="big_button" value="View Results" onclick="UU.caseViewResults();if (fullOnViewResults) {$('.chevron_left').click();}"/>
	</div>
	<div class="pause_results_tip">
		<strong>Tip:</strong> <span>Select courses to generate schedule results.</span>
		<div style="clear:both"></div>
	</div>
</div>

<div class="results-top noprint">
	<div class="results-legend">
		<div class="results-legend-switch-container" title="View detailed information on each class by showing the timetable's legend">
 			<label class="results-legend-switch-label"  for="results-legend-switch">Legend</label>
 			<div class="mdl-switch-force-focus" style="width: 37px;">
				<label id="results-legend-switch-label" class="mdl-switch mdl-js-switch mdl-js-ripple-effect" 
					for="results-legend-switch">
					<input id="results-legend-switch" type="checkbox" 
						class="mdl-switch__input focusable disable-no-crf disable-get-schedule" onclick="UU.caseToggleLegend()"> 
					<span class="mdl-switch__label"></span>
				</label>
			</div>
		</div>
	</div>
	<div class="tips-button" title="Display helpful tips" style="position:relative">
		<button class="mdl-button mdl-js-button disable-no-crf disable-get-schedule" id="fortips" onclick="SLIDER.showTip();return false;">
			Tips
		</button>
		<div class="tips_counter"><span class="tips_counter_nb">0</span></div>
	</div>
	
	<div class="results-sort">
	<div class="reg_sort">

		<h3 class="accessOnly">Sorting</h3>

		

		 
		<span class="sorting-checkbox-container" title="Choose how to sort your schedule results">
		<label for="sort_by" class="label_font">Sort by:</label>&nbsp;&nbsp;
		<select class="disable-no-crf disable-get-schedule" id="sort_by" name="sort_by" onchange="UU.caseChangeSort(this.value);" onkeydown="return avoidChange(event);" onkeypress="return avoidChange(event);" onkeyup="return avoidChange(event);">
		<option value="none">Select...</option>
		<option value="daysoff">Most days off</option>
		<option value="morning">Mornings</option>
		<option value="midday">Mid-day classes</option>
		<option value="evening">Evenings</option>
		<option value="timeatschool">Time off campus</option>
		<option value="timeinclass">Most on-campus</option>
		
		
		
		
		</select>
		</span>
		
		
	</div>
	</div>
	
	
	
	<div class="results-filter" title="Filter out schedules">
		<button class="mdl-button mdl-js-button disable-no-crf disable-get-schedule" id="forfilter" onclick="SLIDER.showTip();return false;">
			Filters <span id="filtersCount"></span>
		</button>
	</div>
	

	
	<div style="display:flex;justify-content:space-evenly;flex-wrap:wrap;">
		
		<div class="rowfilter reg_filter" id="hide_full_tip">
			<div class="filteroption">
				<label for="hide_full">Full classes</label>
				<span class="hide50">
				
					(<span class="fullText" style="font-weight: bold;">&bull;</span>)
				
				</span>
			</div>
			<div class="mdl-switch-force-focus switch">
				<label id="hide_full_label" class="mdl-switch mdl-js-switch mdl-js-ripple-effect" 
					for="hide_full">
					<input id="hide_full" type="checkbox" 
						class="mdl-switch__input focusable"
						value="hide" onclick="UU.caseChangeHideFull(this);"> 
					<span class="mdl-switch__label"></span>
				</label>
			</div>
		</div>
		<div class="mdl-tooltip" data-mdl-for="hide_full_tip">Allow schedule results containing full classes</div>
		
		

		
		


		
		
		


		

		
		
	</div>
</div>

<div class="reg_parent" style="display:none">

<p class="accessOnly" id="page_results_desc">
This is the Results region. Showing result <span class="resultIndex">0</span> of <span class="resultMax">0</span>. This shows you a list of all the possible schedules using your list of courses. Navigate through the results. You may sort and filter the results using the tools in this region. When you have found your preferred schedule, use the provided class numbers to enroll for the classes. You may also use the Select Courses region to change the list of courses.
</p>

<div class="reg_row1_enroll noprint" style="display:none;">
	<h2 class="reg_title noprint">
		<span class="title_act1">Getting Schedule</span>
		<span class="title_act2">Validating Your Enrollment Course Cart</span>
	</h2>
</div>

<div class="reg_row1 noprint noselect">
	<button type="button" id="forfilter_desktop" class="btn btn-mid hide50">Filter</button>

	<div class="reg_flip">
		<table class="flip_table">
			<tr>
				<td>
        			<a class="results-action-first" title="First Result">
						<i class="nav-first results-nav-btn results-nav-disabled" aria-hidden="true"></i>
        			</a>
        		</td>
				<td>
					<a class="results-action-previous" title="Previous Result">
						<i class="nav-prev results-nav-btn results-nav-disabled" aria-hidden="true"></i>
					</a>
				</td>
				<td class="results-nav">
					<div class="results-with-schedules">
						<div>
							Result
						</div>
						<div>
					    	<span class="results-current-schedule">0</span>
					       	of
					       	<span class="results-total-schedules">0</span>
				        </div>
					</div>
				</td>
				<td>
					<a class="results-action-next" title="Next Result">
						<i class="nav-next results-nav-btn results-nav-disabled" aria-hidden="true"></i>
					</a>
				</td>
				<td>
					<a class="results-action-last" title="Last Result">
						<i class="nav-last results-nav-btn results-nav-disabled" aria-hidden="true"></i>
					</a>
				</td>
			</tr>
			<tr id="result_page_message" style="display:none;">
        			<td colspan="5" style="font-weight:bold;color:#00BB00;" ><div role="alert" tabindex="0" id="favalert">Saved to Favorites</div></td>
        		</tr>
		</table>
        <span class="cohort_info"></span>
	</div>

	<div class="reg_links nomobile hide50">

			<div class="leftnclear backToSearchLink"><a href="javascript:void(0)" onclick="UU.caseViewCriteria();" title="Back to search"><img style="vertical-align: middle" src="images/search.gif" alt="Back to search icon"/>&nbsp;Back to search</a></div>
			
			<div class="leftnclear"><a href="javascript:void(0)" id="addToFavorites" onclick="UU.caseFavoriteResult();"><img style="vertical-align:middle;width:16px;" src="images/add_fav.svg" alt="Favorite your schedule"/>&nbsp;Save as Favourite</a></div>
			
			
			
			
				<div class="leftnclear" id="xcreateShareLink"><a href="javascript:void(0)" onclick="ShareLinkController.createLink();"><img style="vertical-align:middle;width:16px;" src="images/link.svg" alt="Create Share link icon"/>&nbsp;Share</a></div>
			
			
			<div class="leftnclear"><a class="printLink" href="javascript:void(0)" title="Print printer-friendly schedule" onclick="clickPrint()"><img style="vertical-align:middle;width:16px" src="images/print.svg" alt="Print Schedule "/>&nbsp;Print</a></div>

			<!--<div class="leftnclear"><a href="javascript:void(0)" id="testThumb">Test Thumbnail</a></div> -->
			<div class="leftnclear"><a href="#" onclick="SLIDER.showTip();return false;" class="tip_link disable-get-schedule"><img style="vertical-align:middle;width:18px" src="images/lightbulb_bl.svg" alt="show tips icon"/>&nbsp;Tips</a></div>
	</div>

				<!-- Added by prakash start for mobile sort -->
					<div class="centerparent">
							<div id="popup" class="popup-wrapper center hide">
								<div class="popup-content">
									<div class="popup-title">
										<button type="button" class="filteconfrim popup-close hide50">X</button>
										<h3>Sort by:</h3>
									</div>
									<div class="popup-body">

										<input type="radio" id="nonemobile"
											onclick="UU.caseChangeSort(this.value);" name="sb" value="none"><label class="under"
											for="nonemobile">None</label>
										
										<input type="radio" id="daysoffmobile"
											onclick="UU.caseChangeSort(this.value);" name="sb" value="daysoff"><label class="under"
											for="daysoffmobile">Most days off</label>
										
										<input type="radio" id="morningmobile"
											onclick="UU.caseChangeSort(this.value);" name="sb" value="morning"><label class="under"
											for="morningmobile">Mornings</label>
										
										<input type="radio" id="middaymobile"
											onclick="UU.caseChangeSort(this.value);" name="sb" value="midday"><label class="under"
											for="middaymobile">Mid-day classes</label>
										
										<input type="radio" id="eveningmobile"
											onclick="UU.caseChangeSort(this.value);" name="sb" value="evening"><label class="under"
											for="eveningmobile">Evenings</label>
										
										<input type="radio"
											id="timeatschoolmobile" onclick="UU.caseChangeSort(this.value);"
											name="sb" value="timeatschool"><label class="under"
											for="timeatschoolmobile">Time off campus</label>
										
										<input type="radio" id="timeinclassmobile"
											onclick="UU.caseChangeSort(this.value);" name="sb"
											value="timeinclass"><label class="under"
											for="timeinclassmobile">Most on-campus</label>
										
										
										
										

									</div>
								</div>
							</div>


	<div id="popuptips" class="popup-wrapper center hide">
		<div class="popup-content">
			<div class="tips-previous nomobile">
				<button class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect"
					onclick="SLIDER.sliderChange(false);" aria-label="Previous Tip">
  					<i class="fa fa-arrow-left"></i>
				</button>
			</div>
			<div class="popup-body">
				<div class="tips-image">
					<img id="slider_tip_img" src="images/tip_drag.png" alt="Tiny screenshot to accompany tip text">
				</div>
				<div class="popup-title">
					Block out times
				</div>
				<div class="popup-subtitle">
					<span class="slider_tip_text">
						Loading...
					</span>
				</div>
				<div class="filter-popup-buttons">
					<button
						class="mdl-button mdl-js-button mdl-button--accent popup-close">
						Close
					</button>
					<button
						class="mdl-button mdl-js-button mdl-button--accent popup-close"
							 onclick="SLIDER.sliderChange(true);">
						Next
					</button>
				</div>
				<div class="tips-carousel">
				</div>
			</div>
			<div class="tips-next nomobile">
				<button class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect"
					onclick="SLIDER.sliderChange(true);" aria-label="Next Tip">
  					<i class="fa fa-arrow-right"></i>
				</button>
			</div>
		</div>
	</div>


							<div id="popupfilter" class="popup-wrapper center hide">
								<div class="popup-content">
									<div class="popup-title">
										<button type="button" class="filteconfrim xpopup-close hide50">X</button>
										Filters
									</div>
									<div class="popup-body">

										<div class="popup-subtitle">
											Show me schedules containing:
										</div>
										
										<div class="rowfilter">
											<div class="filteroption">
												<label for="hide_fullmobile">Full classes</label>
												<span class="hide50">
												
													(<span class="fullText" style="font-weight: bold;">&bull;</span>)
												
												</span>
											</div>
											<div class="mdl-switch-force-focus switch">
												<label id="hide_fullmobile_label" class="mdl-switch mdl-js-switch mdl-js-ripple-effect" 
													for="hide_fullmobile">
													<input id="hide_fullmobile" type="checkbox" 
														class="mdl-switch__input focusable"
														value="hide" onclick="UU.caseChangeHideFull(this);"> 
													<span class="mdl-switch__label"></span>
												</label>
											</div>
										</div>
										
										

										
										


										
										
																				


										

										
										
										

									<div class="filter-popup-buttons">
										<button class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent popup-close focusable" 
											style="min-width: 60%;">
											Done
										</button>
									</div>

									</div>
								</div>
							</div>
							<div style="clear:both"></div>
				</div>
</div>

<div class="reg_flip_results">


<div class="reg_row2 printable" id="flip_area">
	<div class="reg_schedule">
		<div class="reg_schedule1 noselect">
			<!-- Filled by schedule.js -->
		</div>
		<div class="reg_schedule2 noselect">
			<!-- Filled by schedule.js -->
		</div>
		<div class="reg_legend-container mobile">
			<div class="mobile-legend">
				<button class="mdl-button mdl-js-button mobile-legend-button" onclick="RR.toggleLegend()">
		  			<span>Legend</span>
		  			<span style="display:flex;"><i class="fa fa-angle-down mobile-legend-icon"></i></span>
				</button>		
			</div>
		</div>
<div class="buttonsUnderTimetable noprint">
<div class="reg_row2_2">
	<div class="reg-info" style="margin-bottom:10px;">
		<div id="crnListWarnings"></div>
		<div id="crnListInfos"></div>
		<div id="crnListCrns"></div>
		<div id="crnListHelp"></div>
	</div>
	<div class="bottom-buttons-2">
		
		
			<button class="mdl-button mdl-js-button mdl-button--raised white-background disable-no-results disable-no-crf" onclick="UU.caseFavoriteResult();" aria-label="Favorite your schedule">
				Save as Favourite
			</button>
		
		<div class="schedule-buttons">
		</div>
	</div>
	<div class="bottom-buttons">
		<div>
			<button class="mdl-button mdl-js-button disable-no-results disable-no-crf" onclick="clickPrint()">
	  			Print
			</button>
			
			
			<span id="createShareLink"> 
				<button class="mdl-button mdl-js-button disable-no-results disable-no-crf" onclick="UU.caseShareLink();//ShareLinkController.createLink();">
		  			Share
				</button>
			</span>
			
			
		</div>
	</div>
</div>
</div>
</div>
<div class="reg_legend-container desktop">
	<div class="reg_legend">

		<h3 class="visuallyhidden">Legend</h3>
		
		<div class="printed_by printonly">Printed by: <span class="alt_autho_text">Guest</span></div>

		<div class="legend_box /*mdc-elevation--z1*/" id="legend_box">
			<!-- Filled by legend.js -->
		</div>
		
		<div id="legend_checkout" class="clearfix2 noprint">
			<input class="big_button button_cancel_schedule" type="button" onclick="cancelScheduleClick();" value="&#9664; Cancel"/>
			<input class="big_button button_do_actions" type="button" onclick="doActionsClick();" title="Review actions before proceeding. Click to perform all the actions listed above" value="Do Actions"/>
			<input class="big_button button_return" type="button" value="Return to 'Select Courses'"/>

			<div class="reg_final_bubble" style="display:none;clear:both;text-align:right">
				<div style="display:inline-block">
					<div class="bubble">
						<div class="tip_top"><i class="fa fa-caret-up"></i></div>
	    				<img src="images/step_arrow_north.png" alt="Up arrow for step instructions" class="pull-right phone step_arrow"/>
					    Click this button to view the latest state of your courses.
					    <div class="tip_bottom" style="display:none" id="post_checkout_tip"><i class="fa fa-caret-down"></i></div>
    					<div class="clearfix"></div>
					</div>
				</div>
			</div>
			
			<input class="big_button button_post_checkout" onclick="custButtonPostCheckout();" type="button" value="Proceed to Enrollment Course Cart"/>
		</div>

		<div id="legend_headers" class="noprint">

			<div class="course_legend_header">
				Class
			</div>
			<div class="course_action_header">
				<span class="title_act1">Action</span>
				<span class="title_act2">Result</span>
			</div>
			<div class="course_option_header">
				Options
			</div>
			<div class="course_result_header">
				Result
			</div>

		</div>

	</div>
</div>

	<div style="clear:both"></div>

</div>


</div>

<div id="no_results_message_div">
	<span role="alert" style="font-size:20px;color:#CC3333;">No Results</span><br/>
	<br/>There are no schedule combination(s) with the selected courses.  
	<br/><br/>
	<div class="noResultsIdea">
    	<table>
    		<tr>
    			<td><img src="images/lightbulb_yl.svg" height="48" width="48" alt="Light bulb icon"></td>
    			<td><strong>Tip:</strong> <span class="noResultsIdeaText">TEMP</span></td>
        	</tr>
    	</table>
	</div>
</div>
<div id="no_cnfs_div">
	<span role="alert" style="font-size:20px;color:#CC3333;">No Courses Selected</span><br/>
	<br/>Select at least one course to see potential schedules here.
</div>


</div>


<div class="reg_welcome">
	<div class="welcome_holder">
		<div class="welcome_title">
			Instructions
		</div>
		<div class="welcome_subtext">
			
			
			We're excited to have you try our new scheduling tool! This tool is for <strong>planning and initial registration purposes to generate schedule options</strong>. To use this tool for registration, make sure you log in to your Student Centre (<a href='https://my.ucalgary.ca' target='_blank'>my.ucalgary.ca</a>) to complete your course registration initialization, review your enrollment appointment and ensure that you do not have any holds on your account. <br/><br/> <strong>TIPS:</strong> <ul> <li><strong>Know your courses</strong> before using the scheduling tool</li> <li><strong>Meet with a <a href='https://ucalgary.ca/registrar/registration/advising' target='_blank'>faculty advisor</a></strong> to ensure that you've picked the right courses and you're on track with your degree</li> <li><strong>Use the "Search for Classes" advanced search tool</strong> in your Student Centre to find web-based courses, informal topic classes or courses offered at specific sites, day of week, or time of day</li> <li>Make sure you <strong>understand your course requirements</strong> - this tool will not check your prerequisites or reserve capacities until <strong>after</strong> you have attempted registration</li><li>Use your Student Centre to ?Edit? or ?Swap? courses and sections once you are already registered in courses</li> </ul> <strong>ONLINE REGISTRATION HELP:</strong> Visit <a href='https://www.ucalgary.ca/registrar/registration/schedule-builder' target='_blank'>ucalgary.ca/registrar/registration/schedule-builder</a> for access to our video tutorial, FAQs and detailed registration information. <br/><br/> <strong>TECHNICAL ASSISTANCE:</strong> Contact IT support at <a href='mailto:itsupport@ucalgary.ca'>it@ucalgary.ca</a> or call at <a href='tel:4032205555'>403.220.5555</a> or <a href='tel:18883423802'>1.888.342.3802</a>
		</div>
	</div>
	<div class="welcome_cont_but">
		<input type="button" class="big_button" value="Continue" onclick="UU.caseWelcomeContinue();"/>
	</div>
</div>

<div class="reg_term">
	<button class='mdl-button mdl-js-button welcome-back' onclick="UU.caseWelcomeBack();">BACK</button>
	<div class="welcome_holder"></div>
	<div class="welcome_title2">
	Select Term
	</div>
	<div class="welcome_term_input_notice"></div>
	<div class="welcome_term_subtext">
		To begin, select a term:
	</div>
	<div class="sorry_msg sorry_no_terms" style="display:none">
		<i class="fa fa-exclamation-triangle"></i> Sorry, there are no terms available to you at this time.
	</div>
	<div class="sorry_msg sorry_wrong_campus" style="display:none">
		<i class="fa fa-exclamation-triangle"></i> Sorry, your campus is not presently enabled for this system.
	</div>
	<div class="sorry_msg sorry_blocked_user">
		<i class="fa fa-exclamation-triangle"></i> Your schedule is unavailable for viewing at this time.
	</div>
	<div id="welcomeTerms"></div>
 </div>

<div class="reg_recommendation">
	<button class='mdl-button mdl-js-button welcome-back' onclick="UU.caseWelcomeBack();">BACK</button>
	<button class='mdl-button mdl-js-button welcome-back welcome-doubleback' onclick="UU.caseWelcomeDoubleBack();" style="display:none">BACK</button>
	<div class="welcome_holder"></div>
	<div class="welcome_title2">
	You have a Recommendation/Plan/Assigned Blocks
	</div>
	<div class="welcome_subtext courseCount" id="recommendedShow" style="display:none;">Your advisor has <span id="recommendedCount">a</span> recommendation for you:</div>
	<div id="suggestedResult"></div>
	<div class='skip-rec-div'>
		<button class="mdl-button mdl-js-button" id="skip_rec" onclick="UU.caseWelcomeDone(false, true);">
			Skip
		</button>	
	</div>
	
</div>

</div>
</div>
</td> <!-- end of page_results -->






<td id="page_favorites" class="vsb_page disable-get-schedule" style="width:0%">
<div class="page_fader"></div>
<div class="full_page_title title_font">
Favourites
<span id="favCount"></span>
</div>
<div class="full_page">
<div class="full_page_content">


	<div id="tab_favorites">
		<h2 class="visuallyhidden">Favourites Region</h2>
		<p class="accessOnly" style="margin-bottom:15px">This is the Favourites region. If you select a favourite you can rename it, load it, or delete it.</p>
		<h3 class="visuallyhidden">List of Favourites</h3>

		<div class="thumbnail_window">Loading...</div>

		<table style="width:100%;margin:6px 0px">
		<tr>
		<td class="tab-col">
			<button class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent load_button"
				title="Load favourite into Select Courses region"
				onclick="UU.caseLoadFavorite();UU.caseViewResults();" disabled="disabled" >
				&#x25c4; Load
			</button>
		</td>
		<td class="tab-col">
		<div class="fav_title_edit">
		<div class="editable_text_div" id="editable_text">&nbsp;</div>
		<label for="text_editor" class="visuallyhidden">Title of Favorite</label>
		<input type="text" class="text_editor_div" id="text_editor" maxlength="20">
		<a href="javascript:void(0);" class="edit_pencil" id="pencil1" title="Click to edit title"></a>
		<div class="favorite_date_time" id="fav-date-time1">Feb. 20, 3:45</div>
		</div>
		</td>
		<td class="tab-col">
			<button class="mdl-button mdl-js-button mdl-button--raised white-background delete_button"
				style="float:right" 
		 		onclick="UU.caseDeleteFavorite();" 
		 		title="Delete favourite"
		 		disabled="disabled" >
				Delete
			</button>
			<div style="clear:both"></div>
		</td >
		</tr>
		</table>

		<div class="preview_schedule">
			<!-- Filled by schedule.js -->
		</div>
		<div class="preview_message do_select saved_notice">
		No Favourite Selected
		</div>
		
		<div class="warning_fav_notsignedin">
		<strong>Warning:</strong> Favourites will be lost if you close your browser
		</div>
		

	</div>

	<!-- Recommendations tab -->
	<div id="tab_recommendations" style="display:none;min-height:700px">
		<div id="page_rec_list">

		  <div class="rec_container">
		  <div class="rec_container">
		    <div class="sdl_input rec_search">
		      <label for="rec_search_input">Search for Recommendation</label>
		      <input type="text" id="rec_search_input" placeholder="Title, Description, Student ID..."
		      	title="Search by Recommendation ID, Student ID, Advisor, Title, Course..."/>
		    </div>
		  </div>
		
		    <div class="switch-field">
		      
		      	<input type="radio" id="switch_left" name="switch_2" value="all" checked/>
		      	<label for="switch_left">All</label>
		      
		      <input type="radio" id="switch_center" name="switch_2" value="created" />
		      <label for="switch_center">Created by me</label>
		      <input type="radio" id="switch_right" name="switch_2" value="modified" />
		      <label for="switch_right">Modified by me</label>
		    </div>
		    <div class="rec-advising-warning">
		    	Only displaying recommendations in <span class="active-term-label"></span>
		    	
		    </div>
		  </div>
		  <div class="rec_results_top"></div>
		  <div class="rec_results_noterm saved_notice">
		  	No Term Selected
		  </div>
		  <div class="rec_results">
		    <div class="rec_result" style="display:none" title="Edit Recommendation">
		      <div class="rec_icon">
		        <i class="fa fa-calendar" aria-hidden="true"></i>
		      </div>
		      <div class="rec_info">
		        <div class="rec_info_item recr-id">R-2124</div>
		        <div class="rec_info_item recr-created">Mar 31</div>
		      </div>
		      <div class="rec_result_details">
		        <div class="rec_detail_item recr-advisor">Advisor Name</div>
		        <div class="rec_detail_item recr-students">Assigned Students</div>
		        <div class="rec_detail_item recr-title">Title</div>
		      </div>
		      <div class="rec_search_highlight">
			    <div class="rec_search_highlight_title">
		      	</div>
			    <div class="rec_search_highlight_text">
			    </div>
		      </div>
		    </div>
		  </div>
          <div class="rec_results_count">
		  </div>

		  <div class="rec-bot-tools">
		    <button class="small_button rec-but-new" title="Send current schedule as a recommendation to one or more students">Create Recommendation</button>
		    <button class="rec-import-csv small_button" title="Import Recommendations by CSV" style="padding: 5px;height: 33px;">
		    	<img src="images/csv.gif" height="16" width="16" alt="Import from CSV"/>
		    </button>
		  </div>
		</div>
		<div id="page_rec_edit" style="display:none">



			<div class="rec-top-buttons">
			  <button class='rec-top-btn small_button rec-but-back' title="Back to list of recommendations">
			    <i class="fa fa-reply" aria-hidden="true"></i>
			  </button>
			  <!--
			  <div class='top-rt-btns'>
			    <button class='rec-top-btn small_button rec-but-prev'><i class="fa fa-angle-left" aria-hidden="true" title="View previous recommendation"></i>
			    </button>
			    <button class='rec-top-btn small_button rec-but-next'><i class="fa fa-angle-right" aria-hidden="true" title="View next recommendation"></i>
			    </button>
			  </div>
			   -->
			  <div class='top-rt-btns'>
			  	<h3 class="rec-header">
			  	Recommendation
				</h3>
			  </div>
			  <div style="clear:both">
			  </div>
			</div>

			<div id="page_rec_edit_form">

			<!--
			<div class="rec-row">
			  <div class="rec-row-label">
			    ID
			  </div>
			  <div class="rec-row-desc rec-row-desc-wide">
			    <span class="recf-id">R-1001</span>
			  </div>
			</div>
			 -->

			<div class="rec-row">
			  <div class="rec-row-label rec-label">
			  	From
			    <!-- <i class="fa fa-user" aria-hidden="true"></i> -->
			  </div>
			  <div class="rec-row-desc">
			    <span class="recf-creator">---</span>
			  </div>
			</div>


			<div class='rec-tbl-cont'>
			  <div class='rec-row-label rec-label'>
			    To
			  </div>

			  <div class='rec-row-desc fancy-input rec-scrol-div' style='padding:0'>
			    <div class="rec-name-item">
			      <label class="rec-student-tooltip" title="">
			        <input type="checkbox" />Jill Smith March 31</label>
			    </div>
			  </div>
			</div>


			<div class="rec-row">
			  <div class="rec-row-desc rec-add">
			    <input type="text" value="" class="rec-add-input" placeholder="Student ID" title="You may add multiple IDs">
			  </div>
			  <div class="rec-add-button">
			    <button class="small_button" title="Add Student ID(s)">Add</button>
			  </div>
			  <div class="rec-grp-button">
			    <button class="small_button" title="Select from Student Group" style="padding: 5px;">
			    	<i class="fa fa-group"></i>
			    </button>
			  </div>
			  <div class="rec-csv-button">
			    <button class="small_button" title="Import Student IDs from CSV" style="padding: 5px;">
			    	<img src="images/csv.gif" height="16" width="16" alt="Import from CSV"/>
			    </button>
			  </div>
			</div>
			<div id="recAddWarning">
			</div>

			<div class="rec-row">
			  <div class="rec-row-desc">
			    <table class="rec-user-actions" cellpadding="0" cellspacing="0">
			      <tr>
			        <td>
			          <button class="small_button recb-select-all" title="Select/Deselect all students">Select All</button>
			        </td>
			        <td>
			          <button class="small_button recb-remove" title="Remove selected students from list">Remove</button>
			        </td>
			        <td>
			          <button class="small_button recb-splice" title="Duplicate this recommendation and move the selected students to the new recommendation">Splice to New</button>
			        </td>
			        <!--
			        <td>
			          <button class="small_button recb-advise">Advise</button>
			        </td>
			         -->
			      </tr>
			    </table>
			  </div>
			</div>

			<div class='rec-row-label rec-label'>
			  Title
			</div>
			<div class="rec-row-desc">
			  <input class="rec-title fancy-input" type="text" placeholder="Title of Recommendation" />
			</div>

			<div class='rec-row-label rec-label'>
			  Message
			</div>
			<div class="rec-row-desc">
				<textarea rows="4" class="rec-message fancy-input" maxlength="1000" placeholder="Message to the students..."></textarea>
			</div>
			<div class="rec-recent" style="display:none">
			  <table cellpadding="0" cellspacing="0">
			    <tr>
			      <td class="rec-label-cell" style="padding-left:5px">
			        Recent
			      </td>
			      <td>
			        <select>
			          <option>Once</option>
			          <option>Twice</option>
			        </select>
			      </td>
			    </tr>
			  </table>
			</div>

			<div class="rec-option" title="Force the students using this software to follow this recommendation">
			  <label>
			    <input type="checkbox" class="recf-compulsory"/>Mandatory</label>
			</div>
			<div class="rec-option" title="Allow students to select courses beyond those in this recommendation">
			  <label>
			    <input type="checkbox" class="recf-lock-select"/>Permit additional courses</label>
			</div>

			<div class="rec-tags">
			  <table cellpadding="0" cellspacing="0">
			    <tr>
			      <td class="rec-label-cell rec-label" title="Add tags to help categorize or organize recommendations">
			        Tags
			      </td>
			      <td>
			        <input id="input-rec-tags-add" type="text" value="" class="recf-tags" />
			      </td>
			    </tr>
			  </table>
			</div>

			<div class="rec-tags rec-groups-row">
			  <table cellpadding="0" cellspacing="0">
			    <tr>
			      <td class="rec-label-cell rec-label" title="Advisors must belong to at least one of the specified security groups to have permission to modify/delete this recommendation. Groups and their user assignments can be changed in VSB Settings.">
			        Groups
			      </td>
			      <td>
			        <input id="input-rec-groups-add" type="text" value="" class="recf-groups" />
			      </td>
			    </tr>
			  </table>
			</div>

			<div class="rec-disabled-message">
				You do not have permission to edit this recommendation.
			</div>
			<div class="rec-bottom">
			  <button class="small_button rec-but-save">Save</button>
			  <button class="small_button rec-but-duplicate">Duplicate</button>
			  <button class="small_button rec-but-delete">Delete</button>
			  <button class="small_button rec-but-cancel">Cancel</button>
			</div>

		</div>
		</div>

	</div>

</div>
</div>
<div class="page_whiteout"></div>
<div class="fav-bottom" style="position:absolute;top:100%"></div>
</td>




</tr>
</table>


<div id="guidance_wrapper">
<div id="guidance">
	<span class="guidanceText"></span>
</div>
</div>


<div style="clear:both"></div>






</div> <!-- end of under_header -->
</div> <!-- end of under_header_wrapper -->

<!--<div>
<canvas id="thumbtest" width="100" height="100" style="border:0px solid #000000;display:none;">
</canvas>
</div> -->

</div> <!-- mainframe. Opened in the header -->
<div class="custom_footer">













<div id="footerWrap" class="noprint">
	<div style="float:left;">
		<div class="footer-item-l">Copyright &#xa9; <script type="text/javascript">date = new Date(); document.write(date.getFullYear());</script></div>
		<div class="footer-item-l"><a target="_blank" href="http://www.ucalgary.ca/policies/files/policies/privacy-policy.pdf">Privacy Policy</a></div>
		<div class="footer-item-l"><a target="_blank" href="https://ucalgarysurvey.qualtrics.com/SE/?SID=SV_2lcAqNmIryzHpZ3">Website feedback</a></div>
	</div>
	<div style="float:right;text-align:right">
		<div class="footer-item-l">University of Calgary</div>
		<div class="footer-item-l">2500 University Drive NW</div>
		<div class="footer-item-l">Calgary, AB &nbsp;&nbsp; T2N 1N4</div>
		<div class="footer-item-l">CANADA</div>
	</div>
    <div style="clear:both"></div>
</div>




</div>

<!-- Active sessions: 1322 -->
</div>

<div id="noticePopup" class="popup-wrapper center hide">
	<div class="popup-content">
		<div class="popup-title">
			<h3>Notice</h3>
		</div>
		<div class="popup-body">
			<!-- Content will get put here -->
		</div>
		<div id="popupNoticeButtons"></div>
	</div>
</div>


<div id="sharePopup" class="popup-wrapper center hide" style="position:absolute;z-index:999">
	<div class="popup-content">
		<div class="popup-title">
			<button type="button" class="filteconfrim popup-close hide50">X</button>
		<h3>Export to Calendar</h3>
		</div>
		<div class="popup-body">
			<div style="padding: 0px 5px 5px 5px;">This will send all the events of the schedule your are currently viewing to your Calendar.<br/><br/> 
				<span style="font-weight:500">Warning:</span> If you need to change or remove these events you will need to do it manually using your Calendar
			</div>
			<div id="notificationCal" style="display:none;">Your schedule has been saved to the calendar.</div>
			<div id="calenderbutton" style="text-align:center;padding-top:10px">
				<button id="googleShare" class="mdl-button mdl-js-button" onclick="vsbTimer.doLogin();">Google Calendar</button>
				<button id="outLookShare" class="mdl-button mdl-js-button" onclick="vsbTimer.doLogin();">Outlook Calendar</button>
				<button id="iCal" class="mdl-button mdl-js-button" onclick="vsbTimer.doLogin();" style="text-transform:none;">iCal</button>
			</div>
		</div>
	</div>
</div>



<div class="planloader" style="display: none">
	<div class="imp-dialog0">
		<div class="imp-dialog">
			<div class="imp-list">
				<div class="imp-list-title">Courses on plan:</div>
				<div class="imp-list-courses">
					<div class="imp-list-course">ART 1110</div>
					<div class="imp-list-course">CMT 3660</div>
					<div class="imp-list-course">DET 2830</div>
				</div>
			</div>
			<div class="imp-chooser">

				<div class="imp-choice imp-template" style="padding-left: 0px">
					<div class="imp-choice-shadow">
						<div class="imp-choice-header">
							<div class="imp-choice-plus">+</div>
							<div class="imp-choice-title">Choose from one of the
								following options:</div>
						</div>

						<div class="imp-option-scroll">
							<div class="imp-option imp-template">
								<div class="imp-option-row">
									<div class="imp-option-num">
										<div style="display: table; height: 100%">
											<div style="display: table-cell; vertical-align: middle;"
												class="imp-option-num-txt">1</div>
										</div>
									</div>
									<div class="imp-option-text">CHEM 1020</div>
								</div>
							</div>

							<div class="imp-option">
								<div class="imp-option-row">
									<div class="imp-option-num">
										<div style="display: table; height: 100%">
											<div style="display: table-cell; vertical-align: middle;">
												2</div>
										</div>
									</div>
									<div class="imp-option-text">CHEM 1040</div>
								</div>
							</div>
						</div>

					</div>
				</div>

			</div>
		</div>
	</div>

	<div class='imp-accept'>
		<input class="big_button cancel_plan_button" type="button" value="Cancel" />
		<input class="big_button clear_plan_button" type="button" value="Reset Choices" />
		<input class="big_button import_plan_button" type="button" value="Import Plan" />
	</div>
</div>


<div style="position:absolute;top:0px;left:0px;color:black;background-color:white;display:none;" id="console">Hello</div>
<div style="position:absolute;top:40px;left:0px;color:black;background-color:white;display:none;" id="console2">Hello</div>


    <!-- SUGGESTION CONTAINER -->
    	<div id='suggestion_box' class='accessible ak_o' role='listbox' aria-label="course search suggestion list">
    		<div id='suggestion_container' style="max-height:300px;overflow-y:auto;" class="sdl-scrollbars"></div>
    	</div>
    <!-- END SUGGESTION CONTAINER -->

<div class="popupl-overlay"></div>
<div class="check_media"></div>
<!-- <canvas id="thumbtest" width="100" height="100" style="border:0px solid #000000;"> -->



</body>
</html>
