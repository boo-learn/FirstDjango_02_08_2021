from django.http import Http404
from django.shortcuts import render, HttpResponse

ITEMS = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def index(request):
    context = {
        "name": "Евгений",
        "surname": "Юрченко",
        "hobbies": ["programming", "bike", "sleep"]
    }
    return render(request, "index.html", context)


def about(request):
    name = 'Михаил'
    second_name = 'Викторович'
    surname = 'Никитенко'
    tel = '8-999-999-99-99'
    email = 'xm4dn355x@gmail.com'
    return HttpResponse(f'Имя: <b>{name}</b><br>Отчество: <b>{second_name}</b><br>'
                        f'Фамилия: <b>{surname}</b><br>Телефон: <b>{tel}</b><br>'
                        f'e-mail: <b>{email}<b>')


def items(request):
    context = {"items": ITEMS}
    return render(request, "items_list.html", context)


def item_details(request, id):
    for item in ITEMS:
        if item['id'] == id:
            context = {
                "item": item
            }
            return render(request, "item_page.html", context)
    raise Http404
