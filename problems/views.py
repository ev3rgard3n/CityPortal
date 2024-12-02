from loguru import logger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required


from .forms import ProblemForm, AdminProblemForm, CategoryForm
from problems.models import Categories, Problems


def problems(request):
    categories = Categories.objects.all()
    problems = Problems.objects.all()

    # Фильтрация по категориям
    category_filter = request.GET.getlist("category")
    if category_filter:
        problems = problems.filter(category__id__in=category_filter)

    # Сортировка (пример по ID или статусу)
    # По умолчанию сортировка по ID
    order_by = request.GET.get("order_by", "id")
    problems = problems.order_by(order_by)

    context = {"title": "Проблемы",
               "categories": categories, "problems": problems}
    return render(request, "problems/problems.html", context)


def about_problems(request, id):
    problem = get_object_or_404(Problems, pk=id)
    return render(request, "problems/about_problems.html", {"problem": problem})


@login_required
def create_problem(request):
    try:
        if request.method == "POST":
            form = ProblemForm(request.POST, request.FILES)
            logger.debug(f"{form=}")
            if form.is_valid():
                problem = form.save(commit=False)
                problem.user = request.user  # Привязываем проблему к текущему пользователю
                problem.status = "Новая"
                problem.save()
                # Перенаправление после создания
                return redirect("problems:index")
            logger.debug(form.errors)
        else:
            form = ProblemForm()
        return render(request, "problems/create_problem.html", {"form": form})
    except Exception as e:
        logger.opt(exception=e).error("Проблема при создании проблемы")

        return render(request, "problems/create_problem.html", {"form": form})


@staff_member_required
def admin_edit_problem(request, pk):
    problem = get_object_or_404(Problems, pk=pk)
    if request.method == 'POST':
        form = AdminProblemForm(request.POST, request.FILES, instance=problem)
        if form.is_valid():
            form.save()
            logger.info("Проблема успешно сохранена")
            return redirect('problems:index')  # После успешного сохранения
        logger.debug(form.errors)
    else:
        form = AdminProblemForm(instance=problem)
    return render(request, 'problems/admin_edit_problem.html', {'form': form, 'problem': problem})


@staff_member_required
def admin_add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('problems:index')  # Оставить на той же странице
    else:
        form = CategoryForm()
    return render(request, 'problems/admin_add_category.html', {'form': form})