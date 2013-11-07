# So we got side-tracked (we still need to fill in that null previous) 
# and are implementing the tracking of users via cookies.
# Trying to call response.set_cookie. Importing response from django.http
# Seemed to work but there's no method, set_cookie for 'module'
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
        for field_name, Model, attr in [("image-data", Drawing, 'image'),
                                        ("caption", Caption, 'content')]:
            if field_name in request.POST:
                obj = Model()
                setattr(obj, attr, request.POST[field_name])
                print request.POST[field_name]
        obj.user = user
        obj.save()
    drawing_val = obj.__class__ == Caption
    response = render(request, 'index.html', {'drawing': drawing_val})
    if user_id is None and request.POST:
        response.set_cookie("user_id", user.id)
    return response