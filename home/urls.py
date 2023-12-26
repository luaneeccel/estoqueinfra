from django.urls import path
from .views import IndexView, login


urlpatterns =[

    path('', login, name='login'),
    path('home/', IndexView.as_view(), name='index'),



]