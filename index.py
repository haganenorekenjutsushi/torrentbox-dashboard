#!/usr/bin/env python
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import psutil
import socket
import datetime
import re
import config

print "Content-type: text/html"
print 
print """
<!doctype html>
<html><head>
    <meta charset="utf-8">
    <title>Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="Carlos Alvarez - Alvarez.is">

    <!-- Le styles -->
    <link href="assets/css/bootstrap.css" rel="stylesheet">
    <link href="assets/css/main.css" rel="stylesheet">
    <link href="assets/css/font-style.css" rel="stylesheet">
    <link href="assets/css/flexslider.css" rel="stylesheet">
    
	<script type="text/javascript" src="http://code.jquery.com/jquery-latest.js"></script>

    <style type="text/css">
      body {
        padding-top: 60px;
      }
    </style>

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le fav and touch icons -->
    <link rel="shortcut icon" href="assets/ico/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="assets/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="assets/ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="assets/ico/apple-touch-icon-57-precomposed.png">

  	<!-- Google Fonts call. Font Used Open Sans & Raleway -->
	<link href="http://fonts.googleapis.com/css?family=Raleway:400,300" rel="stylesheet" type="text/css">
  	<link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">

<script type="text/javascript">
$(document).ready(function () {

    $("#btn-blog-next").click(function () {
      $('#blogCarousel').carousel('next')
    });
     $("#btn-blog-prev").click(function () {
      $('#blogCarousel').carousel('prev')
    });

     $("#btn-client-next").click(function () {
      $('#clientCarousel').carousel('next')
    });
     $("#btn-client-prev").click(function () {
      $('#clientCarousel').carousel('prev')
    });
    
});

 $(window).load(function(){

    $('.flexslider').flexslider({
        animation: "slide",
        slideshow: true,
        start: function(slider){
          $('body').removeClass('loading');
        }
    });  
});

</script>


    
  </head>
  <body>
  
  	<!-- NAVIGATION MENU -->

    <div class="container">

	  <!-- FIRST ROW OF BLOCKS -->     
      <div class="row">

      <!-- SICKRAGE BLOCK -->
        <div class="col-sm-3 col-lg-3">
        	<a href="//%(ip)s:8081">
      		<div class="dash-unit">
	      		<dtitle>TV Downloads</dtitle>
	      		<hr>
				<div class="thumbnail">
					<img src="assets/img/sickrage.png" alt="SickRage"  style="height:150px">
				</div><!-- /thumbnail -->
				<h1>SickRage</h1>
				<h3>TV Downloads</h3>
				<br>
			</div>
			</a>
        </div>

      <!-- CouchPotato BLOCK -->
        <div class="col-sm-3 col-lg-3">
        	<a href="//%(ip)s:5050">
      		<div class="dash-unit">
	      		<dtitle>Movie Downloads</dtitle>
	      		<hr>
				<div class="thumbnail">
					<img src="assets/img/couchpotato.png" alt="SickRage" style="height:150px">
				</div><!-- /thumbnail -->
				<h1>CouchPotato Server</h1>
				<h3>Movie Downloads</h3>
				<br>
			</div>
			</a>
        </div>

      <!-- Plex BLOCK -->
        <div class="col-sm-3 col-lg-3">
        	<a href="//%(ip)s:32400/web/">
      		<div class="dash-unit">
	      		<dtitle>Media Centre</dtitle>
	      		<hr>
				<div class="thumbnail">
					<img src="assets/img/plex.jpg" alt="SickRage" class="img-circle" style="height:150px">
				</div><!-- /thumbnail -->
				<h1>Plex</h1>
				<h3>Media Centre</h3>
				<br>
			</div>
			</a>
        </div>

      <!-- Transmission BLOCK -->
        <div class="col-sm-3 col-lg-3">
        	<a href="//%(ip)s:9091">
      		<div class="dash-unit">
	      		<dtitle>Torrents</dtitle>
	      		<hr>
				<div class="thumbnail">
					<img src="assets/img/transmission.png" alt="SickRage"  style="height:150px">
				</div><!-- /thumbnail -->
				<h1>Transmission</h1>
				<h3>Torrents</h3>
				<br>
			</div>
			</a>
        </div>

     
      </div><!-- /row -->
      
     <!-- SECOND ROW OF BLOCKS -->     
      <div class="row">

      	<!-- DONUT CHART BLOCK -->
        <div class="col-sm-3 col-lg-3">
      		<div class="dash-unit">
		  		<dtitle>CPU Usage</dtitle>
		  		<hr>
	        	<div id="cpu" data-value="%(CPUUsage)d"></div>
	        	<h2> %(CPUUsage).1f%%</h2>
			</div>
        </div>
      	 <!-- DONUT CHART BLOCK -->
        <div class="col-sm-3 col-lg-3">
      		<div class="dash-unit">
		  		<dtitle>RAM Usage</dtitle>
		  		<hr>
	        	<div id="ram" data-value="%(RAMUsage)d"></div>
	        	<h2> %(RAMUsage).1f%% used</h2>
            <h3> %(RAMFree).dMB free</h3>
			</div>
        </div>

         <!-- DONUT CHART BLOCK -->
        <div class="col-sm-3 col-lg-3">
      		<div class="dash-unit">
		  		<dtitle>Disk Usage</dtitle>
		  		<hr>
	        	<div id="disk" data-value="%(DiskUsage)d"></div>
	        	<h2>%(DiskUsage).1f%% used</h2>
            <h3>%(DiskFree)dGB free</h3>
			</div>
        </div>

        <div class="col-sm-3 col-lg-3">

      <!-- LOCAL TIME BLOCK -->
      		<div class="half-unit">
	      		<dtitle>Local Time</dtitle>
	      		<hr>
		      		<div class="clockcenter">
			      		<digiclock>12:45:25</digiclock>
		      		</div>
			</div>

      <!-- SERVER UPTIME -->
			<div class="half-unit">
	      		<dtitle>Server Uptime</dtitle>
	      		<hr>
	      		<div class="cont">
					<p><img src="assets/img/up.png" alt=""> <bold>Up</bold> | %(uptime)ss</p>
				</div>
			</div>

        </div>
	  </div>
      
      
	</div> <!-- /container -->
	<div id="footerwrap">
      	<footer class="clearfix"></footer>
      	<div class="container">
      		<div class="row">
      			<div class="col-sm-12 col-lg-12">
      			<p><img src="assets/img/logo.png" alt=""></p>
      			<p>Blocks Dashboard Theme - Crafted With Love - Copyright 2013</p>
      			</div>

      		</div><!-- /row -->
      	</div><!-- /container -->		
	</div><!-- /footerwrap -->


    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script type="text/javascript" src="assets/js/bootstrap.js"></script>
	<script type="text/javascript" src="assets/js/lineandbars.js"></script>
    
	<script type="text/javascript" src="assets/js/dash-charts.js"></script>
	<script type="text/javascript" src="assets/js/gauge.js"></script>
	
	<!-- NOTY JAVASCRIPT -->
	<script type="text/javascript" src="assets/js/noty/jquery.noty.js"></script>
	<script type="text/javascript" src="assets/js/noty/layouts/top.js"></script>
	<script type="text/javascript" src="assets/js/noty/layouts/topLeft.js"></script>
	<script type="text/javascript" src="assets/js/noty/layouts/topRight.js"></script>
	<script type="text/javascript" src="assets/js/noty/layouts/topCenter.js"></script>
	
	<!-- You can add more layouts if you want -->
	<script type="text/javascript" src="assets/js/noty/themes/default.js"></script>
    <!-- <script type="text/javascript" src="assets/js/dash-noty.js"></script> This is a Noty bubble when you init the theme-->
	<script type="text/javascript" src="http://code.highcharts.com/highcharts.js"></script>
	<script src="assets/js/jquery.flexslider.js" type="text/javascript"></script>

    <script type="text/javascript" src="assets/js/admin.js"></script>
  
</body></html> """ % {"CPUs": psutil.cpu_count(), 
  "RAM": psutil.virtual_memory().total/1024/1024, 
  "CPUUsage":  psutil.cpu_percent(interval=1), 
  "RAMUsage":psutil.virtual_memory().percent, 
  "RAMFree":psutil.virtual_memory().available/1024/1024, 
  "ip":[(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1],
  "DiskUsage": psutil.disk_usage(config.diskUsagePath).percent,
  "DiskFree":  psutil.disk_usage(config.diskUsagePath).free/1024/1024/1024,
  "uptime":  re.sub('\.\d*$','',str(datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())))
}