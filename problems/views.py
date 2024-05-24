from typing import Any
from django.shortcuts import render

from problems.models import Categories


def problems(request) -> Any :
    categories = Categories.objects.all()
    context = {
        "title" : "Проблемы",
        "categories": categories
    }
    return render(request, "problems/problems.html", context=context)

def about_problems(request) -> Any:
    return render(request, "problems/about_problems.html")