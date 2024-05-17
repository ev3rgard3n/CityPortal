from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request) -> HttpResponse:
    context: dict = {
        "title": "Home",
        "content":"Главная страница"
    }

    return render(request=request, template_name="main/index.html", context=context)


def about(request) -> HttpResponse:
    return HttpResponse("about page")
