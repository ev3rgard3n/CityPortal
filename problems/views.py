from typing import Any
from django.shortcuts import render


def problems(request) -> Any :
    return render(request, "problems/problems.html")

def about_problems(request) -> Any:
    return render(request, "problems/about_problems.html")