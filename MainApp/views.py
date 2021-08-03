from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    name = "Юрченко Е.В."
    text = f"<h1>Изучаем django</h1><strong>Автор</strong>: <i>{name}</i>"
    return HttpResponse(text)

def about(request):
    return HttpResponse("Юрченко Е.В.")