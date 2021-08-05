from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from MainApp import views

urlpatterns = [
    path('', views.index, name="home"),  # Вот тут у меня вопрос. Обычно я тут кидаю ссылку на urls конкретного application и там уже их обрабатываю, например include('MainApp.urls').
    path('about/', views.about, name="about"),
    path('items-list/', views.items, name="items-list"),
    path('item-page/<int:id>', views.item_details, name="item-page"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)