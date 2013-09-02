<!DOCTYPE html>
<html>
<?php
if($_POST["browserdata"]) {
	//Process dump of browser data and display thank you
} else {
	//display diagnostic page
?>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
		<title>Diagnostic Page</title>
		<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.0.min.js"></script>
		<script type="text/javascript">
			var obj = {};
			
			function runTests() {
				var transitionEndEvtName = whichTransitionEvent();
				obj.ua = navigator.userAgent;
				obj.transitionEndEvt = transitionEndEvtName;
				$(document).on(transitionEndEvtName, function(evt) {
					obj.transitionElement = {
						tagName: (document == evt.target) ? 'DOCUMENT' : evt.target.tagName,
						id: evt.target.id
					};
					printResult();
				});
				$('#testbox').addClass('transTest');
			}
			
			function printResult() {
				$('#results').append(JSON.stringify(obj));
			}
			
			function whichTransitionEvent(){
			    var t;
			    var el = document.createElement('fakeelement');
			    var transitions = {
			      'transition':'transitionend',
			      'OTransition':'oTransitionEnd',
			      'MozTransition':'transitionend',
			      'WebkitTransition':'webkitTransitionEnd'
			    }
			
			    for(t in transitions){
			        if( el.style[t] !== undefined ){
			            return transitions[t];
			        }
			    }
			}
			
		</script>
		<style>
			#testbox {
				transition: width 2s;
				-webkit-transition: width 2s;
				-moz-transition: width 2s;
				-o-transition: width 2s;
				-ms-transition: width 2s;
				border: solid 1px;
				width: 10px;
			}
			
			#testbox.transTest {
				width: 100px;
			}
		</style>
	</head>
	<body>
		<input type="button" onclick="runTests();" value="Run Tests" />
		<p id="results"></p>
		<div id="testbox" style=""></div>
	</body>
<?
}
?>
</html>
