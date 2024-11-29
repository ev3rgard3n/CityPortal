from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProblemForm

from problems.models import Categories, Problems


def problems(request):
    categories = Categories.objects.all()
    problems = Problems.objects.all()

    # Фильтрация по категориям
    category_filter = request.GET.getlist("category")
    if category_filter:
        problems = problems.filter(category__id__in=category_filter)

    # Сортировка (пример по ID или статусу)
    order_by = request.GET.get("order_by", "id")  # По умолчанию сортировка по ID
    problems = problems.order_by(order_by)

    context = {"title": "Проблемы", "categories": categories, "problems": problems}
    return render(request, "problems/problems.html", context)


def about_problems(request) -> Any:
    return render(request, "problems/about_problems.html")


@login_required
def create_problem(request):
    if request.method == "POST":
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.status = "New"
            problem.save()
            return redirect("problems")
    else:
        form = ProblemForm()
    return render(request, "problems/create_problem.html", {"form": form})
