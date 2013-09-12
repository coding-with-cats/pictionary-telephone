# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from game.models import Drawing

def play(request):
	if request.POST:
		drawing = Drawing()
		drawing.image = request.POST["image-data"]
		print request.POST["image-data"]
		drawing.save()
		return redirect('/')
	else:
	    html = """
	    <head>
	    	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
	    	<script src="/static/sketch.js"></script>
	    	<script>
		      $(function() {
		      	var canvas = document.getElementById('tools_sketch');
		        $('#image-form').submit(function() {
          			$('#image-data').val(canvas.toDataURL());
             	});
		      });
		    </script>
	    	<link rel="stylesheet" type="text/css" href="/static/style.css">
	    </head>
	    	<div class="tools">
			  <a href="#tools_sketch" data-tool="marker">Marker</a>
			  <a href="#tools_sketch" data-tool="eraser" data-size="10">Eraser</a>
			</div>
			<canvas id="tools_sketch" width="800" height="300"></canvas>
			<form id="image-form" method="post">
				<input type="hidden" name="image-data" id="image-data" value="">
				<input type="submit" id="submit-button">
			</form>
			<script type="text/javascript">
			  $(function() {
			    $('#tools_sketch').sketch({defaultColor: "#000"});
			  });
			</script>
			"""
	    return HttpResponse(html)