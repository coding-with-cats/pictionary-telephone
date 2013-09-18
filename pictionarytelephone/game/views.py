# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from game.models import Drawing

def play(request):
    if request.POST:
        drawing = Drawing()
        drawing.image = request.POST["image-data"]
        print request.POST["image-data"]
        drawing.save()

    return render(request, 'index.html', {'drawing': True})
