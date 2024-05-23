from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request) -> HttpResponse:
    context: dict = {
        "title": "Home - Главная страница",
        "content": "Городской портал"
    }

    return render(request=request, template_name="main/index.html", context=context)


def about(request) -> HttpResponse:

    context: dict = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": """Добро пожаловать на городской портал Ижевска! Мы - команда преданных профессионалов, работающих для улучшения жизни наших горожан. Наша цель - создать пространство, где каждый житель Ижевска может найти актуальную информацию, участвовать в обсуждениях и оставлять заявки для рассмотрения администрацией.

\nНаша миссия\n
Мы стремимся к тому, чтобы город Ижевск стал еще более комфортным и привлекательным для жизни. Мы поддерживаем принципы открытости, прозрачности и ответственности в работе с нашими жителями.

\nКак мы работаем\n
На нашем портале вы можете оставить заявку на рассмотрение администрацией. Мы обещаем внимательно изучить каждое обращение и предпринять необходимые действия для решения возникшей проблемы или вопроса.

\nВаш вклад\n
Мы приглашаем каждого жителя Ижевска принять участие в улучшении нашего города. Ваши идеи, предложения и замечания помогут нам сделать Ижевск лучше для всех.

\nПрисоединяйтесь к нам на городском портале Ижевска и вместе мы сделаем наш город еще прекраснее! """
    }
    return render(request, template_name="main/about.html", context=context)
