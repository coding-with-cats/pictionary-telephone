from django.http import HttpResponse
from django.shortcuts import redirect, render
from game.models import Drawing, Caption, User

def play(request):
    obj = None
    user_id = None
    if request.POST:
        if "user_id" in request.COOKIES:
            user_id = request.COOKIES["user_id"]
            user = User.objects.get(id=user_id)
        else:
            user = User()
            user.save()
        if "image-data" in request.POST:
            obj = Drawing()
            obj.image = request.POST["image-data"]
        elif "caption" in request.POST:
            obj = Caption()
            obj.content = request.POST["caption"]
        if "previous-id" in request.POST:
            obj.previous_id = request.POST["previous-id"]

        obj.user = user
        obj.save()
    is_drawing = obj.__class__ == Caption
    response = render(request, 'index.html', {'drawing': is_drawing, 'obj': obj})
    if user_id is None and request.POST:
        response.set_cookie("user_id", user.id)
    return response


def history(request):
    response = render(request, 'history.html')
    return response