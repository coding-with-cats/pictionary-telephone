# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from game.models import Drawing, Caption

def play(request):

    if request.POST:
        for field_name, Model, attr in [("image-data", Drawing, 'image'),
                                        ("caption", Caption, 'content')]:
            if field_name in request.POST:
                obj = Model()
                setattr(obj, attr, request.POST[field_name])
                print request.POST[field_name]
                obj.save()


    return render(request, 'index.html', {'drawing': False})
