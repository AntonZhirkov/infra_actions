from django.http import HttpResponse


def index(request):
    return HttpResponse('Workflow спасибо!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
