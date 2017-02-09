from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Lesson


def hello_world_view(request):
    """ Стандартный ответ на запрос. Возвращается со статусом 200 """
    return HttpResponse()


def hello_world_string(request):
    """ Передача данных в теле ответа """
    return HttpResponse("Hello World")


def hello_world_403(request):
    """ Передача данных, и установка своего кода ответа. """
    return HttpResponse("Hello world", status=403)


def lesson_list_view(request):
    """ Рендеринг списка уроков. """
    return render(
        request,
        'lesson__list.html',
        {
            'lesson_queryset': Lesson.objects.all()
        }
    )


def lesson_retrieve_view(request, pk):
    """ Рендеринг конкретного урока """
    return render(
        request,
        'lesson__retrieve.html',
        {
            'lesson': get_object_or_404(Lesson.objects.all(), pk=pk)
        }
    )
