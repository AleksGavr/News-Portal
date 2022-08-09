from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *


def index(request):
    return HttpResponse('Hello, World')
# class AuthorList(ListView):
#     # Указываем модель, объекты которой мы будем выводить
#     model = Author
#     # Поле, которое будет использоваться для сортировки объектов
#     # ordering = 'name'
#     # Указываем имя шаблона, в котором будут все инструкции о том,
#     # как именно пользователю должны быть показаны наши объекты
#     template_name = 'newsapp/authors.html'
#     # Это имя списка, в котором будут лежать все объекты.
#     # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
#     context_object_name = 'Authors'
#     # queryset = Author.objects.all()
#
# # Create your views here.
