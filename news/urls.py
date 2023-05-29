from django.urls import path
# Импортируем созданное нами представление
from .views import (
   NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, BaseRegisterView, upgrade_me, CategoryListView, subscribe
)
from django.contrib.auth.views import LoginView, LogoutView

from django.views.decorators.cache import cache_page

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', cache_page(60*10)(NewsList.as_view()), name='news_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', NewsDetail.as_view(), name='news_detail' ),
   #path('create/', create_news, name='news_create'),
   path('create/', cache_page(60*10)(NewsCreate.as_view()) , name='news_create'),
   path('<int:pk>/update/', cache_page(60*10)(NewsUpdate.as_view()), name='news_update'),
   path('<int:pk>/delete/', cache_page(60*10)(NewsDelete.as_view()), name='news_delete'),
   path('login/',
         LoginView.as_view(template_name = 'news/login.html'),
         name='login'),
   path('logout/',
         LogoutView.as_view(template_name = 'news/logout.html'),
         name='logout'),
   path('newsup/',
         BaseRegisterView.as_view(template_name = 'news/newsup.html'),
         name='newsup'),

   path('upgrade/', upgrade_me, name = 'upgrade'),

   path('categories/<int:pk>', cache_page(60*10)(CategoryListView.as_view()), name='category_list'),

   path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),


]



