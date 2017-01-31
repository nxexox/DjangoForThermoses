from django.http import HttpResponse
from django.shortcuts import render


def hello_world_view(request):
    """ Стандартный ответ на запрос. Возвращается со статусом 200 """
    return HttpResponse()


def hello_world_string(request):
    """ Передача данных в теле ответа """
    return HttpResponse("Hello World")


def hello_world_403(request):
    """ Передача данных, и установка своего кода ответа. """
    return HttpResponse("Hello world", status=403)
