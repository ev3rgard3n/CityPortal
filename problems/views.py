from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProblemForm
from loguru import logger

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


def about_problems(request, id):
    problem = get_object_or_404(Problems, pk=id)
    return render(request, "problems/about_problems.html", {"problem": problem})


@login_required
def create_problem(request):
    try:
        if request.method == "POST":
            form = ProblemForm(request.POST, request.FILES)
            logger.debug(f"{form = }")
            if form.is_valid():
                problem = form.save(commit=False)
                problem.user = request.user  # Привязываем проблему к текущему пользователю
                problem.status = "Новая"
                problem.save()
                return redirect("problems:index")  # Перенаправление после создания
            logger.debug(form.errors)
        else:
            form = ProblemForm()
        return render(request, "problems/create_problem.html", {"form": form})
    except Exception as e:
        logger.opt(exception=e).error("Проблема при создании проблемы")

        return render(request, "problems/create_problem.html", {"form": form})

