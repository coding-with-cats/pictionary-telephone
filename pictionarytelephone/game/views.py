# Create your views here.
from django.http import HttpResponse

def play(request):
	    html = """
	    	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
	    	<script src="/static/sketch.js"></script>
	    	<div class="tools">
			  <a href="#tools_sketch" data-tool="marker">Marker</a>
			  <a href="#tools_sketch" data-tool="eraser">Erase Everything</a>
			</div>
			<canvas id="tools_sketch" width="800" height="300"></canvas>
			<script type="text/javascript">
			  $(function() {
			    $('#tools_sketch').sketch({defaultColor: "#000"});
			  });
			</script>
			"""
	    return HttpResponse(html)